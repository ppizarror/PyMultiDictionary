"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

DICTIONARY
Dictionary object.
"""

__all__ = [
    'MultiDictionary'
]

import urllib.error

from PyMultiDictionary._utils import *

from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Dict, Tuple, Optional, List

# Dicts
_EDUCALINGO = ('bn', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'jv', 'ko', 'mr',
               'ms', 'pl', 'pt', 'ro', 'ru', 'ta', 'tr', 'uk', 'zh')


class MultiDictionary(object):
    """
    Dictionary. Support synonyms, antonyms and definitions from some languages.
    """

    _cached_soups: Dict[str, 'BeautifulSoup']  # Stores cached web
    _langs: Dict[str, Tuple[bool, bool]]  # synonyms, definition, translation, antonym
    _test_cached_file: str = ''  # If defined, loads that file instead

    def __init__(self) -> None:
        """
        Constructor.
        """
        self._langs = {  # iso 639 codes
            'bn': (True, True, True, False),
            'de': (True, True, True, False),
            'en': (True, True, True, True),
            'es': (True, True, True, False),
            'fr': (True, True, True, False),
            'hi': (True, True, True, False),
            'it': (True, True, True, False),
            'ja': (True, True, True, False),
            'jv': (True, True, True, False),
            'ko': (True, True, True, False),
            'mr': (True, True, True, False),
            'ms': (True, True, True, False),
            'pl': (True, True, True, False),
            'pt': (True, True, True, False),
            'ro': (True, True, True, False),
            'ru': (True, True, True, False),
            'ta': (True, True, True, False),
            'tr': (True, True, True, False),
            'uk': (True, True, True, False),
            'zh': (True, True, True, False)
        }
        self._cached_soups = {}
        self._test_cached_file = ''

    @staticmethod
    def _process(word: str) -> str:
        """
        Process a given word.

        :param word: Word
        :return: Word without invalid chars
        """
        assert isinstance(word, str), 'word must be an string'
        s = ''.join(i for i in word if not i.isdigit())  # remove numbers
        s = tokenize(s).lower()  # tokenize
        s = s.replace(' ', '').replace('\n', '')  # remove spaces
        return s

    def _bsoup(self, link: str, encoding: str = 'utf-8') -> Optional['BeautifulSoup']:
        """
        Returns a parsed web.

        :param link: Link
        :param encoding: Web encoding
        :return: Parsed web. None if error
        """
        if self._test_cached_file != '':  # Load test file
            f = open(self._test_cached_file)
            data = ''.join(f.readlines())
            f.close()
            return BeautifulSoup(data, 'html.parser')
        bs_keys = list(self._cached_soups.keys())
        if link in bs_keys:
            return self._cached_soups[link]
        try:
            data = str(urlopen(link).read().decode(encoding))
        except urllib.error.HTTPError:
            return None
        bs = BeautifulSoup(data, 'html.parser')
        self._cached_soups[link] = bs
        if len(bs_keys) >= 50:
            del self._cached_soups[bs[0]]
        return bs

    def synonym(self, lang: str, word: str) -> List[str]:
        """
        Finds a synonym for a given word.

        :param lang: Lang code
        :param word: Word to retrieve
        :return: Synonyms list
        """
        words = []
        word = self._process(word)
        if lang not in self._langs.keys():
            raise InvalidLangCode(f'{lang} code is not supported for synonyms')
        if lang in _EDUCALINGO:
            bs = self._bsoup(f'https://educalingo.com/en/dic-{lang}/{word}')
            if bs is None:
                return words
            results = [i for i in bs.find_all('div', {'class': 'contenido_sinonimos_antonimos0'})]
            if len(results) > 0:
                results = results[0]
            else:
                return words
            for j in results.findAll('a'):
                words.append(j.get('title').strip())
        return words

    def meaning(self, lang: str, word: str) -> str:
        """
        Finds the meaning for a given word.

        :param lang: Lang code
        :param word: Word to retrieve
        :return: Meaning
        """
        words = ''
        word = self._process(word)
        if lang not in self._langs.keys():
            raise InvalidLangCode(f'{lang} code is not supported for meanings')
        if lang in _EDUCALINGO:
            bs = self._bsoup(f'https://educalingo.com/en/dic-{lang}/{word}')
            if bs is None:
                return words

            # Definition
            results = [i for i in bs.find_all('div', {
                'id': 'significado_de'})]
            if len(results) > 0:
                results = results[0]
            else:
                return words
            words = results.text

            # Wikipedia
            results = [i for i in bs.find_all('span', {
                'id': 'wiki_introduccion'})]
            if len(results) > 0:
                results = results[0]
            else:
                return words
            words += '\n\n' + results.text

        return words.strip()

    def translate(self, lang: str, word: str, to='') -> List[Tuple[str, str, str]]:
        """
        Translate a word.
l
        :param lang: Lang tag
        :param word: Word to translate
        :param to: Target language
        :return: List of (Lang name, Lang tag, translated word)
        """
        assert isinstance(lang, str), 'lang code must be an string'
        assert isinstance(to, str), 'to lang code must be an string'
        words = []
        word = self._process(word)
        if lang not in self._langs.keys():
            raise InvalidLangCode(f'{lang} code is not supported for translation')
        if lang in _EDUCALINGO:
            bs = self._bsoup(f'https://educalingo.com/fr/dic-{lang}/{word}')
            if bs is None:
                return words
            results = [i for i in bs.find_all('div', {'class': 'traduccion0'})]
            if len(results) == 0:
                return words
            for j in results:
                lang_tag = j.get('id')
                lang_name = j.find_all('h4', {'class', 'traductor'})
                if len(lang_name) != 1:
                    continue
                lang_name = lang_name[0].find_all('strong', {})
                if len(lang_name) != 1:
                    continue
                lang_name = lang_name[0].text.strip().capitalize()

                # Find non-links
                lang_nonlink = j.find_all('span', {'class': 'negro'})
                if len(lang_nonlink) == 1:
                    words.append((lang_name, lang_tag, lang_nonlink[0].text.strip()))
                    continue

                # Find links
                lang_link = j.find_all('strong', {})
                if len(lang_link) != 2:
                    continue
                lang_link = lang_link[1].find_all('a', {})
                if len(lang_link) == 1:
                    words.append((lang_name, lang_tag, lang_link[0].text.strip()))

        return words


class InvalidLangCode(Exception):
    """
    Invalid lang.
    """
