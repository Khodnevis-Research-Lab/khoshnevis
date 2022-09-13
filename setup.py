
import codecs
from os import path
from setuptools import setup


setup(
	name='khoshnevis',
	version='0.1.5',
	description='Khodnevis Normalizer',
	author='khodnevisAI',
	author_email='khodnevis.group@gmail.com',
	url='https://www.khodnevisai.com/',
	long_description=codecs.open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	packages=['khoshnevis'],
 	keywords=['python', 'persian', 'normalizer', 'text'],
	classifiers=[
		'Topic :: Text Processing',
		'Natural Language :: Persian',
		'Programming Language :: Python :: 3',
	],
	install_requires=['parsivar==0.2.3', 'demoji==1.1.0'],
)