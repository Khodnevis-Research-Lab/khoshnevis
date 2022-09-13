import re
from parsivar import Normalizer


class Space:
    def __init__(self):
        self.parsivar = Normalizer(statistical_space_correction=True)

    def format_punc(self, text):
        text = re.sub("""((?<=[A-Za-z\d()])\.(?=[A-Za-z]{2})|(?<=[A-Za-z]{2})\.(?=[A-Za-z\d]))""", '. ', text)
        text = re.sub("""((?<=[A-Za-z\d()]),(?=[A-Za-z]{2})|(?<=[A-Za-z]{2}),(?=[A-Za-z\d]))""", ', ', text)
        text = re.sub("""((?<=[A-Za-z\d{}])\.(?=[A-Za-z]{2})|(?<=[A-Za-z]{2})\.(?=[A-Za-z\d]))""", '. ', text)
        text = re.sub("""((?<=[A-Za-z\d{}]),(?=[A-Za-z]{2})|(?<=[A-Za-z]{2}),(?=[A-Za-z\d]))""", ', ', text)
        text = re.sub("""((?<=[A-Za-z\d[]])\.(?=[A-Za-z]{2})|(?<=[A-Za-z]{2})\.(?=[A-Za-z\d]))""", '. ', text)
        text = re.sub("""((?<=[A-Za-z\d[]]),(?=[A-Za-z]{2})|(?<=[A-Za-z]{2}),(?=[A-Za-z\d]))""", ', ', text)
        text = re.sub(r'(?<=[،؟;:?!])(?=\S)', r' ', text)  # add space after punctuations
        text = re.sub(r'\s([،؟.,;:?!"](?:\s|$))', r'\1', text)  # remove space before punctuations
        text = re.sub(r"\s?(\(.*?\))\s?", r" \1 ", text)  # Add space before and after ( and )
        text = re.sub(r"\s?(\[.*?])\s?", r" \1 ", text)  # Add space before and after [ and ]
        # Remove space after & before '(' and '['
        text = re.sub(r'(\s([?,.!"]))|(?<=[\[(])(.*?)(?=[)\]])', lambda x: x.group().strip(), text)
        text = re.sub(r'[.,;:?!]+(?=[.,;:?!])', '', text)  # Replace multiple punctuations with last one
        # text = re.sub(r'(?<=-)\s*|\s*(?=-)', '', text)  # Remove space before and after hyphen
        # text = re.sub(r'(?<=/)\s*|\s*(?=/)', '', text)  # no space before or after the forward slash /
        # text = re.sub('([&@])', r' \1 ', text)  # Space before and after of "&" and "@"
        text = re.sub(' +', ' ', text)  # Remove multiple space
        return text

    def format_halfspace(self, text):
        return self.parsivar.normalize(text)
