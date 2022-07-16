import re
from parsivar import Tokenizer
my_tokenizer = Tokenizer()
import string
from os import path

def clean_url(text):
    allowed_char = string.ascii_letters + string.digits + ':/@_-. '
    # removing html tags
    text = re.sub('<.*?>', '', text)
    # removing normal(without space urls)
    text = re.sub(
        r'(?:(?:http|https)://)?([-a-zA-Z\d.]{2,256}\.[a-z]{2,4})\b(?:/[-a-zA-Z\d@:%_+.~#?&/=]*)?', "", text)
    # removing urls that contains space
    result = ''.join(char for char in text if char in allowed_char)
    result = result.replace('  ', '')
    result = result.split(':')
    for phrase in result:
        p = phrase
        if '//' in p:
            if f'https :{p}' in text:
                text = text.replace(f'https :{p}', '')
            elif f'http :{p}' in text:
                text = text.replace(f'http :{p}', '')
        elif '@' in p and p in text:
            text = text.replace(p, '')
    return text


def extra_clean_txt(txt):
    """
    This function solves two common problem of generated texts:
        1) outputs like: ",,,,Some text,,,,,,,Some text,,,,,"
        2) outputs like: "8 % A 7 % DB % 8 C % DA % AF % d 9 % 88 %"
    """
    text = re.sub(r'(?<=[?!,،:/])\s+(?=[?!,،:/])', '', txt)
    r = re.compile(r'([.,،/#!$%^&*;:{}=_`~()-])[.,،/#!$%^&*;:{}=_`~()-]+')
    out1 = r.sub(r'\1', text)
    return re.sub("%(.*)%", " ", out1)

def fix_spaces(text):
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
    text = re.sub(r'(?<=-)\s*|\s*(?=-)', '', text)  # Remove space before and after hyphen
    text = re.sub(r'(?<=/)\s*|\s*(?=/)', '', text)  # no space before or after the forward slash /
    text = re.sub('([&@])', r' \1 ', text)  # Space before and after of "&" and "@"
    text = re.sub(' +', ' ', text)  # Remove multiple space
    return text

def site_names(txt):
    sites = ['دیجی کالا', 'دیجیمگ', 'کجارو', 'دیجی کالا مگ', 'چهطور', 'زومجی', 'فیدیبو', 'تکفارس', 'زومیت', 'موویمگ', 'گیمفا', 'انزل وب', 'غذالند', 'هنر آنلاین', 'چوک', 'دلتاپیام', 'تابناک', 'دیجیکالا']
    for i in sites:
        txt = txt.replace(i, " ")
    return txt
    # if "وبسایت":
    #     print(1)
    #     txt1 = re.sub("وبسایت (\w+)", "ؤؤؤؤ", txt)
    #     return txt1
    # if "وب‌سایت" in txt:
    #     print(2)
    #     return re.sub("وب‌سایت(\w+)", "وب‌سایت", txt)
    # if "وب سایت" in txt:
    #     print(3)
    #     return re.sub("وب سایت (\w+)", "وب سایت", txt)
    # if "سایت" in txt:
    #     print(4)
    #     return re.sub("سایت (\w+)", "ؤؤؤ", txt)
