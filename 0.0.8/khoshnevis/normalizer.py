import re
from .quote import DOUBLE_QUOTE_REGEX, SINGLE_QUOTE_REGEX
from .persian import PERSIAN_REGEX
from parsivar import Tokenizer
from parsivar import Normalizer
from .dictionary import characters
from .normalizer_utils import clean_url, extra_clean_txt, fix_spaces, site_names
from .emoji_remover import de_emojify


class normalizer(object):
    def __init__(self):
        self.my_normalizer = Normalizer(statistical_space_correction=True)
        self.ar2fa_digits = self.make_trans("٠١٢٣٤٥٦٧٨٩٪", "۰۱۲۳۴۵۶۷۸۹٪")
        self.fa2en_digits = self.make_trans("۰۱۲۳۴۵۶۷۸۹٪", "0123456789%")
        self.my_tokenizer = Tokenizer()

    def make_trans(self, list_a, list_b):
        return {ord(a): b for a, b in zip(list_a, list_b)}


    def multiple_replace(self, text, chars_to_mapping):
        pattern = "|".join(map(re.escape, chars_to_mapping.keys()))
        return re.sub(pattern, lambda m: chars_to_mapping[m.group()], str(text))

    def normalize(self, text, zwnj="\u200c",
                tokenized_fu=False,
                clean_url_fu=False,
                extra_clean_txt_fu=True,
                remove_emoji_fu=False):
        ## getting a list all url in text
        url_list = re.findall("http\S+",text)
        ## replace the urls with a soecial charcter
        for i in url_list:
            text = text.replace(i, "fucCAHRkh")
        ## remove newline characters
        text = text.replace("\n", " ").replace("\t", " ")
        ## transform half space characters into standard form
        text = re.sub(r"\u200c+", "\u200c", text)
        text = text.replace('ـ', '')
        ## fixing spaces in text including spaces around punctuation
        text = fix_spaces(text)
        ## transform persian alphabet ti it's standard form
        if len(characters) > 0:
            text = self.multiple_replace(text, characters)

        ## changing arabic numbers to persian
        text = text.translate(self.ar2fa_digits)
        ## changing single/double quotes 
        text = SINGLE_QUOTE_REGEX.sub("'", text)
        text = DOUBLE_QUOTE_REGEX.sub('"', text)

        ## Allow only english and persian characters
        text = re.sub(PERSIAN_REGEX, " ", text)
        ## andle spaces around half spaces
        text = text.replace(f" {zwnj} ", f"{zwnj}")
        text = text.replace(f"{zwnj} ", f"{zwnj}")
        text = text.replace(f" {zwnj}", f"{zwnj}")

        ## removing emojis
        if remove_emoji_fu:
            text = de_emojify(text)
        ## remove URLS
        if clean_url_fu:
            text = clean_url(text)
        ## handle extra cleaning: remove repetitive punctuation
        if extra_clean_txt_fu:
            text = extra_clean_txt(text)

        ## handle half spaces
        text = self.my_normalizer.normalize(text)

        ## replacing spacial character with actual url
        for i in url_list:
            text = text.replace("fucCAHRkh", i)

        ## replace special website names
        text = site_names(text)
        ## tokenizing text
        if tokenized_fu:
            return self.my_tokenizer.tokenize_words(text)
        return text


