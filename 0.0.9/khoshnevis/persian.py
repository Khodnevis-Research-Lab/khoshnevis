import re


PERSIAN_ALPHA = "ءآئابتثجحخدذرزسشصضطظعغفقلمنهوپچژکگیە"  # noqa: E501
PERSIAN_DIGIT = "۰۱۲۳۴۵۶۷۸۹"


ZWNJ = "\u200c"
PUNK = '\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\]\^\_\`\{\|\}\~\«\»\؟\:\×\٬\٫\﷼\٪\،'

PERSIAN = (
    "a-zA-Z0-9" +
    PERSIAN_ALPHA +
    PERSIAN_DIGIT +
    ZWNJ +
    PUNK
)

PERSIAN_REGEX = r"[^" + PERSIAN + "+]"
