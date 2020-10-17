
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()



setup(
    name='crosspotipy',
    version='dirkfunk',
    description='Huh?',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="@plamere",
    author_email="paul@echonest.com",
    url='https://youtu.be/QireHzmMVvA?t=203',
    install_requires=[
        'requests>=2.20.0',
        'six>=1.10.0',
    ],
    packages=['crosspotipy'])