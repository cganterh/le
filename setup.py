"""Setup script for tcadbot."""

from setuptools import setup, find_packages

from codecs import open
from os import path

current_directory = path.dirname(__file__)
absolute_directory = path.abspath(current_directory)
readme_path = path.join(absolute_directory, 'README.md')

with open(readme_path, encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tcadbot',
    version='1.0.0',
    description='A simple chatbot for telegram.',
    long_description=long_description,
    url='https://github.com/cganterh/tcadbot',
    author='Cristóbal Ganter',
    author_email='cganterh@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Chat',
    ],

    keywords='python python3 telegram-bot chatbot',
    packages=find_packages(),

    install_requires=[
        'python-telegram-bot ~= 6.0',
        'requests ~= 2.17',
    ],

    entry_points={
        'console_scripts': [
            'tcadbot=tcadbot.run:run',
        ],
    },
)
