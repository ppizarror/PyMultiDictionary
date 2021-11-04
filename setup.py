"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

SETUP DISTRIBUTION
Create setup for PyPI.
"""

from setuptools import setup, find_packages
import PyMultiDictionary

# Load readme
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

# Load requirements
with open('requirements.txt', encoding='utf-8') as f:
    requirements = []
    for line in f:
        requirements.append(line.strip())

requirements_docs = requirements.copy()
requirements_docs.extend([
    'sphinx',
    'sphinx-autodoc-typehints>=1.2.0',
    'sphinx-rtd-theme'
])

requirements_tests = requirements.copy()
requirements_tests.extend([
    'codecov',
    'nose'
])

# Setup library
setup(
    name=PyMultiDictionary.__module_name__,
    version=PyMultiDictionary.__version__,
    author=PyMultiDictionary.__author__,
    author_email=PyMultiDictionary.__email__,
    description=PyMultiDictionary.__description__,
    long_description=long_description,
    url=PyMultiDictionary.__url__,
    project_urls={
        'Bug Tracker': PyMultiDictionary.__url_bug_tracker__,
        'Documentation': PyMultiDictionary.__url_documentation__,
        'Source Code': PyMultiDictionary.__url_source_code__
    },
    license=PyMultiDictionary.__license__,
    platforms=['any'],
    keywords=PyMultiDictionary.__keywords__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python',
        'Topic :: Multimedia',
        'Topic :: Text Processing'
    ],
    include_package_data=True,
    packages=find_packages(exclude=['test']),
    python_requires='>=3.6, <4',
    install_requires=requirements,
    extras_require={
        'docs': requirements_docs,
        'test': requirements_tests
    },
    setup_requires=[
        'setuptools',
    ],
    options={
        'bdist_wheel': {'universal': False}
    }
)
