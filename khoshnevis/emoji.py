import re
import demoji


class Emoji:

    def __init__(self):
        pass

    def demoji(self, text):
        return re.sub(' +', ' ', demoji.replace(text, ""))
