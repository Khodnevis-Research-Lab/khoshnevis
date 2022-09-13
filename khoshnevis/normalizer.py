import re
from .space import Space
from .emoji import Emoji
from .URL import URL
from .dictionary import characters
from .dictionary import DOUBLE_QUOTE_REGEX, SINGLE_QUOTE_REGEX
from .dictionary import PERSIAN_REGEX
from .dictionary import hamze
# from .ending import Ending


class Normalizer:

    def __init__(self):
        self.__ar2fa_digits = self.__make_trans("٠١٢٣٤٥٦٧٨٩٪", "۰۱۲۳۴۵۶۷۸۹٪")
        self.__fa2en_digits = self.__make_trans("۰۱۲۳۴۵۶۷۸۹٪", "0123456789%")
        self.__emoji = Emoji()
        self.__space = Space()
        self.__url = URL()
        # self.__ending = Ending()

    def __make_trans(self, list_a, list_b):
        return {ord(a): b for a, b in zip(list_a, list_b)}

    def __multiple_replace(self, text, chars_to_mapping):
        pattern = "|".join(map(re.escape, chars_to_mapping.keys()))
        return re.sub(pattern, lambda m: chars_to_mapping[m.group()], str(text))

    def __site_names(self, txt):
        sites = ['دیجی کالا', 'دیجیمگ', 'کجارو', 'دیجی کالا مگ', 'چهطور', 'زومجی', 'فیدیبو', 'تکفارس', 'زومیت',
                 'موویمگ', 'گیمفا', 'انزل وب', 'غذالند', 'هنر آنلاین', 'چوک', 'دلتاپیام', 'تابناک', 'دیجیکالا',
                 "ویرگول", "چطور"]
        for i in sites:
            txt = txt.replace(i, " ")
        return txt

    def normalize(self, text, zwnj="\u200c",
                  clean_url=True,
                  remove_emoji=True):

        text = self.__site_names(text)

        if clean_url:
            text = self.__url.clean_url(text)

        # remove newline characters
        text = text.replace("\n", " ").replace("\t", " ")

        # transform half __space characters into standard form
        text = re.sub(r"\u200c+", "\u200c", text)
        text = text.replace('ـ', '')

        # transform persian alphabet ti it's standard form
        if len(characters) > 0:
            text = self.__multiple_replace(text, characters)

        # changing arabic numbers to persian
        text = text.translate(self.__ar2fa_digits)

        # changing single/double quotes
        text = SINGLE_QUOTE_REGEX.sub("'", text)
        text = DOUBLE_QUOTE_REGEX.sub('"', text)

        # Allow only english and persian characters
        text = re.sub(PERSIAN_REGEX, " ", text)

        # handle __spaces around half __spaces
        text = text.replace(f" {zwnj} ", f"{zwnj}")
        text = text.replace(f"{zwnj} ", f"{zwnj}")
        text = text.replace(f" {zwnj}", f"{zwnj}")

        # removing __emojis
        if remove_emoji:
            text = self.__emoji.demoji(text)

        text = self.__space.format_punc(text)

        # # remove uncompleted last sentence
        # if endings:
        #     if text.count(".") > 0:  # This added for instagram caption empty return problem.
        #         text = self.__ending.endings(text)

        text = self.__multiple_replace(text, hamze)

        text = self.__space.format_halfspace(text)

        text = self.__space.format_punc(text)

        return text
