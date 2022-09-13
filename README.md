
Khoshnevis (خوشنويس)
====

Python package for **normalizing** Persian text.

+ Text Cleaning
+ URL Remover
+ Emoji Remover
+ Text Tokenization
+ Punctuation Space Correction
+ Half Space Correction (using [Parsivar](https://github.com/ICTRC/Parsivar))
+ Standardize Alphabet
+ [NLTK](http://nltk.org/) compatible
+ Python 3 support



## Usage

```python
>>> from khoshnevis import Normalizer

>>> normalizer = Normalizer()

>>> normalizer.normalize(text="استفاده از نیم‌فاصله متن را زیبا مي كند", zwnj="\u200c", 
                         clean_url=False, remove_emoji=False)
```

```bibtex
text (str): input text
zwnj (str, optional): Zero-width non-joiner character. Defaults to "\u200c".
clean_url (bool, optional): removes all URLs from text. Defaults to True.
remove_emoji (bool, optional): removes all emojis from the text. Defaults to True.
```

## Installation
The latest stable version of Hazm can be installed through `pip`:

	pip install khoshnevis

## Citation info
```bibtex
@misc{khoshnevis,
  author = {HamidReza Attar, Milad Lotfi, Saied Alimoradi},
  title = {Khoshnevis, a Python library for Persian text preprocessing},
  year = {2022},
  url= {https://www.khodnevisai.com/},
}
```