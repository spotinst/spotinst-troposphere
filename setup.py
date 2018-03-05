# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup, find_packages
import spotinst

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spotinst-troposphere',

    version=spotinst.__version__,

    description='A Troposphere custom resource for Spotinst elastigroup',
    long_description='This package will allow you to work with spotinst and troposphere',

    # The project's main homepage.
    url='https://github.com/spotinst/spotinst-troposphere',

    # Author details
    author='Spotinst',
    author_email='service@spotinst.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='spotinst spot instances aws ec2 cloud infrastructure development elastigroup troposphere',
    packages=["spotinst"],
    install_requires=['requests']
)
