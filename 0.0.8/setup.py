
import codecs
from os import path
from setuptools import setup


setup(
	name='khoshnevis',
	version='0.0.8',
	description='Khodnevis Normalizer',
	author='khodnevisAI',
	author_email='khodnevis.group@gmail.com',
	url='https://www.khodnevisai.com/',
	long_description="A Python library for Persian text preprocessing.",
	long_description_content_type='text/markdown',
	packages=['khoshnevis'],
 	keywords=['python', 'persian', 'normalizer', 'text'],
	classifiers=[
		'Topic :: Text Processing',
		'Natural Language :: Persian',
		'Programming Language :: Python :: 3',
	],
	install_requires=['parsivar==0.2.3'],
)