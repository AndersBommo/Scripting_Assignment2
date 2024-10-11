# setup.py
from setuptools import setup, find_packages
# Define the package setup configuration
setup(
    name='morning_greetings',  # Name of the package
    version='1.0',  # Version of the package
    packages=find_packages(),  # Automatically find and include all packages in the directory
    description='A Python package for sending personalized Good Morning messages',  # Brief description of the package
    install_requires=[],  # Dependencies for the package (empty here since there are none)
    
    # Define the entry point for command-line usage
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',  # Creates a 'morning_greetings' command to run the main() function
        ]
    },
)
