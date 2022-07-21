import re
from .quote import DOUBLE_QUOTE_REGEX, SINGLE_QUOTE_REGEX
from .persian import PERSIAN_REGEX
from parsivar import Tokenizer
from parsivar import Normalizer
from .dictionary import characters
from .normalizer_utils import clean_url, extra_clean_txt, fix_spaces
from .emoji_remover import de_emojify


class normalizer(object):
    """A Python class for Persian text preprocessing.
    """

    def __init__(self):
        self._my_normalizer = Normalizer(statistical_space_correction=True)
        self._ar2fa_digits = self._make_trans("٠١٢٣٤٥٦٧٨٩٪", "۰۱۲۳۴۵۶۷۸۹٪")
        self._fa2en_digits = self._make_trans("۰۱۲۳۴۵۶۷۸۹٪", "0123456789%")
        self._my_tokenizer = Tokenizer()

    def _make_trans(self, list_a, list_b):
        return {ord(a): b for a, b in zip(list_a, list_b)}


    def _multiple_replace(self, text, chars_to_mapping):
        pattern = "|".join(map(re.escape, chars_to_mapping.keys()))
        return re.sub(pattern, lambda m: chars_to_mapping[m.group()], str(text))

    def normalize(self, text, zwnj="\u200c",
                tokenized=False,
                clean_url=False,
                extra_clean=True,
                remove_emoji=False):
        """This function is used to normalize persian text

        Args:
            text (str): input text
            zwnj (str, optional): Zero-width non-joiner character. Defaults to "\u200c".
            tokenized (bool, optional): returns tokenized version of the cleaned text. Defaults to False.
            clean_url (bool, optional): removes all URLs from text. Defaults to False.
            extra_clean (bool, optional): removes repetitive punctuations. Defaults to True.
            remove_emoji (bool, optional): removes all emojis from the text. Defaults to False.

        Returns:
            text: Normalized text
        """
        # getting a list all url in text
        url_list = re.findall("http\S+",text)
        # replace the urls with a special character
        for i in url_list:
            text = text.replace(i, "fucCAHRkh")
        # remove newline characters
        text = text.replace("\n", " ").replace("\t", " ")
        # transform half space characters into standard form
        text = re.sub(r"\u200c+", "\u200c", text)
        text = text.replace('ـ', '')
        # fixing spaces in text including spaces around punctuation
        text = fix_spaces(text)
        # transform persian alphabet ti it's standard form
        if len(characters) > 0:
            text = self._multiple_replace(text, characters)

        # changing arabic numbers to persian
        text = text.translate(self._ar2fa_digits)
        # changing single/double quotes 
        text = SINGLE_QUOTE_REGEX.sub("'", text)
        text = DOUBLE_QUOTE_REGEX.sub('"', text)

        # Allow only english and persian characters
        text = re.sub(PERSIAN_REGEX, " ", text)
        # handle spaces around half spaces
        text = text.replace(f" {zwnj} ", f"{zwnj}")
        text = text.replace(f"{zwnj} ", f"{zwnj}")
        text = text.replace(f" {zwnj}", f"{zwnj}")

        # removing emojis
        if remove_emoji:
            text = de_emojify(text)
        # remove URLS
        if clean_url:
            text = clean_url(text)
        # handle extra cleaning: remove repetitive punctuation
        if extra_clean:
            text = extra_clean_txt(text)

        # handle half spaces
        text = self._my_normalizer.normalize(text)

        # replacing spacial character with actual url
        for i in url_list:
            text = text.replace("fucCAHRkh", i)

        # tokenizing text
        if tokenized:
            return self._my_tokenizer.tokenize_words(text)
        return text