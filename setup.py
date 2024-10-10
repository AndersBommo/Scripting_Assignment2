# setup.py
from setuptools import setup, find_packages 

setup(
    name='morning_greetings',
    version='1.0',
    packages=find_packages(),
    description='A Python package for sending personalized Good Morning messages',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',
        ]
    },
)
