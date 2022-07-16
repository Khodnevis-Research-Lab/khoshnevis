import re

LATIN_WITH_SPECIAL_REGEX = re.compile(
    r"(\b(?!URL|EMAIL|PHONE|NUMBER|CUR|LATIN\b)[0-9a-zA-Z]+)"
)

LATIN_REGEX = re.compile(
    r"([0-9a-zA-Z]+)"
)

LATIN_SPACES_REGEX = re.compile(
    r"([0-9a-zA-Z])"
)
