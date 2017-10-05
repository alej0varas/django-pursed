import os
import re
import sys
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


version = '0.9'


setup(
    name='django-pursed',
    version=version,
    url='https://github.com/alej0varas/django-pursed',
    license='GPL v3',
    description='A simple wallet django application',
    long_description=read_file('README.rst'),
    author='Alexandre Varas',
    author_email='alej0varas@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)
