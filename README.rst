=================
PyMultiDictionary
=================

.. image:: https://img.shields.io/badge/author-Pablo%20Pizarro%20R.-lightgray.svg
    :target: https://ppizarror.com
    :alt: @ppizarror

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License MIT

.. image:: https://img.shields.io/badge/python-3.6+-red.svg
    :target: https://www.python.org/downloads
    :alt: Python 3.6+

.. image:: https://badge.fury.io/py/PyMultiDictionary.svg
    :target: https://pypi.org/project/PyMultiDictionary
    :alt: PyPi package

.. image:: https://travis-ci.com/ppizarror/PyMultiDictionary.svg?branch=master
    :target: https://app.travis-ci.com/github/ppizarror/PyMultiDictionary
    :alt: Travis

.. image:: https://img.shields.io/lgtm/alerts/g/ppizarror/PyMultiDictionary.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/ppizarror/PyMultiDictionary/alerts
    :alt: Total alerts

.. image:: https://img.shields.io/lgtm/grade/python/g/ppizarror/PyMultiDictionary.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/ppizarror/PyMultiDictionary/context:python
    :alt: Language grade: Python

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

PyMultiDictionary is a Dictionary Module for Python 3+ to get meanings, translations, synonyms and antonyms of words
in 20 different languages. It uses educalingo.com, synonym.com, and WordNet for getting meanings, translations, synonyms, and antonyms.

This module uses Python Requests and BeautifulSoup4.

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

PyMultiDictionary can be utilised in 2 ways, either by creating a dictionary instance which can take words as arguments or by creating a dictionary instance with a fixed amount of words.

**Create a dictionary object**:

For example,

.. code-block:: python

    from PyMultiDictionary import MultiDictionary
    dictionary = MultiDictionary()

This is will create a local instance of the MultiDictionary class and now it can be used to get meanings, translations etc.

For **Meanings**,

.. code-block:: python

    print (dictionary.meaning('en', 'good'))

This will return a dictionary containing the meanings of the word. For example the above code will return:

.. code-block:: python

    (['Noun', 'Adjective', 'Exclamation'], 'The first definition of good in the dictionary is having admirable, pleasing, superior, or positive qualities; not negative, bad or mediocre. Other definition of good is morally excellent or admirable; virtuous; righteous. Good is also suitable or efficient for a purpose.', 'Good may refer to: ▪ Good and evil, the distinction between positive and negative entities ▪ Good, objects produced for market ▪ Good ▪ Good ▪ Good, West Virginia, USA ▪ Form of the Good, Plato\'s macrocosmic view of goodness in living Expressive works: ▪ Good ▪ Good, a 2008 film starring Viggo Mortensen ▪ Good ▪ Good ▪ Good, by Cecil Philip Taylor Companies: ▪ Good Entertainment ▪ GOOD Music, a record label ▪ Good Technology Music: ▪ "Good", a song by Better Than Ezra from Deluxe...')

The dictionary keys are the different types of the word, the meaning, and the wikipedia first paragrah of the word. Words
in English can be also obtained from WordNet:

.. code-block:: python

    print (dictionary.meaning_wordnet('good'))

Will return:

.. code-block:: python

    {'Noun': ['benefit', 'moral excellence or admirableness', 'that which is pleasing or valuable or useful', 'articles of commerce'], 'Adjective': ['having desirable or positive qualities especially those suitable for a thing specified', 'having the normally expected amount', 'morally admirable', 'deserving of esteem and respect', 'promoting or enhancing well-being', 'agreeable or pleasing', 'of moral excellence', 'having or showing knowledge and skill and aptitude', 'thorough', 'with or in a close or intimate relationship', 'financially safe', 'most suitable or right for a particular purpose', 'resulting favorably', 'exerting force or influence', 'or in force', 'capable of pleasing', 'appealing to the mind', 'in excellent physical condition', 'tending to promote physical well-being; beneficial to health', 'not forged', 'not left to spoil', 'generally admired'], 'Adverb': ['(often used as a combining form', "`good' is a nonstandard dialectal variant for `well'", "completely and absolutely (`good' is sometimes used informally for `thoroughly'"]}

For **Synonyms**,

.. code-block:: python

    print (dictionary.synonym('es', 'Bueno'))

This will return a list containing the Synonyms of the word.

For **Antonyms**,

.. code-block:: python

    print (dictionary.antonym('en', 'Life'))

This will return a list containing the Antonyms of the word. Currently only English is supported.

For **Translations**,

.. code-block:: python

    print (dictionary.translate('en', 'Range'))

This will return the Translation of the word 'Range' in 20 different languages. You can also extend the scope of the translations by providing a target language, which will use google translate API, for example:

.. code-block:: python

    print (dictionary.translate('en', 'Range', to='ru'))

Alternatively, you can set a fixed number of words to the Dictionary Instance. This is useful if you just want to get the meanings of some words quickly without any development need.

Example:

.. code-block:: python

    from PyMultiDictionary import MultiDictionary

    dictionary=MultiDictionary('hotel', 'ambush', 'nonchalant', 'perceptive')
    dictionary.setLang('en') # All words are english
    
    print(dictionary.get_meanings()) # This print the meanings of all the words
    print(dictionary.get_synonyms()) # Get synonyms
    print(dictionary.get_antonyms()) # Get antonyms
    print(dictionary.get_translations()) # This will translate all words to over 20 languages
    print(dictionary.get_translations(to='ru')) # This will translate all words to Russian (if Google API available)

Author
------

<a href="https://ppizarror.com" title="ppizarror">Pablo Pizarro R.</a> | 2021