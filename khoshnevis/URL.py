import re
import string


class URL:

    def __init__(self):
        pass

    def clean_url(self, text):
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
        return re.sub(' +', ' ', text)
