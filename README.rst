
=================
PyMultiDictionary
=================

.. image:: https://img.shields.io/badge/author-Pablo%20Pizarro%20R.-lightgray.svg
    :target: https://ppizarror.com
    :alt: @ppizarror

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License MIT

.. image:: https://img.shields.io/badge/python-3.7+-red.svg
    :target: https://www.python.org/downloads
    :alt: Python 3.7+

.. image:: https://badge.fury.io/py/PyMultiDictionary.svg
    :target: https://pypi.org/project/PyMultiDictionary
    :alt: PyPi package

.. image:: https://img.shields.io/github/actions/workflow/status/ppizarror/PyMultiDictionary/ci.yml?branch=master
    :target: https://github.com/ppizarror/PyMultiDictionary/actions/workflows/ci.yml
    :alt: Build status
    
.. image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2Fppizarror%2FPyMultiDictionary.svg?type=shield
    :target: https://app.fossa.com/projects/git%2Bgithub.com%2Fppizarror%2FPyMultiDictionary?ref=badge_shield
    :alt: FOSSA Status

.. image:: https://codecov.io/gh/ppizarror/PyMultiDictionary/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ppizarror/PyMultiDictionary
    :alt: Codecov

.. image:: https://img.shields.io/github/issues/ppizarror/PyMultiDictionary
    :target: https://github.com/ppizarror/PyMultiDictionary/issues
    :alt: Open issues

.. image:: https://img.shields.io/pypi/dm/PyMultiDictionary?color=purple
    :target: https://pypi.org/project/PyMultiDictionary
    :alt: PyPi downloads

.. image:: https://static.pepy.tech/personalized-badge/PyMultiDictionary?period=total&units=international_system&left_color=grey&right_color=lightgrey&left_text=total%20downloads
    :target: https://pepy.tech/project/PyMultiDictionary
    :alt: Total downloads
    
.. image:: https://img.shields.io/badge/buy%20me%20a-Ko--fi-02b9fe
    :target: https://ko-fi.com/ppizarror
    :alt: Buy me a Ko-fi

PyMultiDictionary is a dictionary module for Python 3+ to get meanings, translations,
synonyms and antonyms of words in 20 different languages. It uses educalingo.com,
synonym.com, and Merriam-Webster for getting meanings, translations, synonyms, and antonyms.

Supported languages
-------------------

- Bengali (**bn**)
- German (**de**)
- English (**en**)
- Spanish (**es**)
- French (**fr**)
- Hindi (**hi**)
- Italian (**it**)
- Japanese (**ja**)
- Javanese (**jv**)
- Korean (**ko**)
- Marathi (**mr**)
- Malay (**ms**)
- Polish (**pl**)
- Portuguese (**pt**)
- Romanian (**ro**)
- Russian (**ru**)
- Tamil (**ta**)
- Turkish (**tr**)
- Ukranian (**uk**)
- Chinese (**zh**)

Install Instructions
--------------------

PyMultiDictionary can be installed via pip, for both MacOS, Windows & Linux. Simply run:

.. code-block:: bash

    $> python3 -m pip install --upgrade PyMultiDictionary

Usage
-----

PyMultiDictionary can be utilized in 2 ways, either by creating a dictionary instance
which can take words as arguments or by creating a dictionary instance with a fixed
amount of words.

**Create a dictionary object**:

For example,

.. code-block:: python

    from PyMultiDictionary import MultiDictionary
    dictionary = MultiDictionary()

This will create a local instance of the MultiDictionary class, and now it can
be used to get meanings, translations, etc.

For **Meanings**,

.. code-block:: python

    print(dictionary.meaning('en', 'good'))

This will return a tuple containing the meanings of the word, in the format
*(word_type, word_meaning, word_wikipedia)*. For example, the above code will return:

.. code-block:: python

    (['Noun', 'Adjective', 'Exclamation'],
     'The first definition of good in the dictionary is having admirable  ...',
     'Good may refer to: ▪ Good and evil, the distinction between positive...')

All methods support other dictionaries, for example, 'Merriam-Webster' can be used
for English words.

.. code-block:: python

    from PyMultiDictionary import MultiDictionary, DICT_MW
    dictionary = MultiDictionary()
    print(dictionary.meaning('en', 'good', dictionary=DICT_MW))

Will return:

.. code-block:: python

    {
        'adjective': ['of a favorable character or tendency', ...],
        'noun': ['something that is good', ...],
        'adverb': ['well']
    }

For **Synonyms**,

.. code-block:: python

    print(dictionary.synonym('es', 'Bueno'))

This will return a list containing the Synonyms of the word.

For **Antonyms**,

.. code-block:: python

    print(dictionary.antonym('en', 'Life'))

This will return a list containing the Antonyms of the word. Currently, only English is supported.

For **Translations**,

.. code-block:: python

    print(dictionary.translate('en', 'Range'))

This will return the word 'Range' translation in 20 different languages.
You can also extend the scope of the translations by providing a target language,
which will use Google Translate API, for example:

.. code-block:: python

    print(dictionary.translate('en', 'Range', to='ru'))

Alternatively, you can set a fixed number of words to the Dictionary Instance. This
is helpful if you want to get the meanings of some words quickly without any development need.

Example:

.. code-block:: python

    from PyMultiDictionary import MultiDictionary, DICT_EDUCALINGO

    dictionary=MultiDictionary('hotel', 'ambush', 'nonchalant', 'perceptive')
    dictionary.set_words_lang('en') # All words are English
    
    print(dictionary.get_meanings(dictionary=DICT_EDUCALINGO)) # This print the meanings of all the words
    print(dictionary.get_synonyms()) # Get synonyms list
    print(dictionary.get_antonyms()) # Get antonyms
    print(dictionary.get_translations()) # This will translate all words to over 20 languages
    print(dictionary.get_translations(to='ru')) # This will translate all words to Russian (if Google API is available)

Supported dictionaries
----------------------

- **DICT_EDUCALINGO**: Meaning, synonym, translation for all languages
- **DICT_MW**: Meanings (English) - Merriam-Webster
- **DICT_SYNONYMCOM**: Synonyms and Antonyms (English)
- **DICT_THESAURUS**: Synonyms (English)

There are many more dictionaries to come. Just contribute to this repo!

Author
------

`Pablo Pizarro R. <https://ppizarror.com>`_ | 2021 - 2025
