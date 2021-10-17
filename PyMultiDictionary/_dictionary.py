"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

DICTIONARY
Dictionary object.
"""

__all__ = [
    'MultiDictionary'
]

import re
import goslate
import urllib.error
import PyMultiDictionary._utils as ut

from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Dict, Tuple, Optional, List
from warnings import warn

# Dicts
_EDUCALINGO = ('bn', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'jv', 'ko', 'mr',
               'ms', 'pl', 'pt', 'ro', 'ru', 'ta', 'tr', 'uk', 'zh')

# Cache
_CACHED_SOUPS: Dict[str, 'BeautifulSoup'] = {}  # Stores cached web


class MultiDictionary(object):
    """
    Dictionary. Support synonyms, antonyms and definitions from some languages.
    """

    _langs: Dict[str, Tuple[bool, bool]]  # synonyms, definition, translation, antonym
    _test_cached_file: Dict[str, str]  # If defined, loads that file instead

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
        self._test_cached_file = {}

    @staticmethod
    def _process(word: str) -> str:
        """
        Process a given word.

        :param word: Word
        :return: Word without invalid chars
        """
        assert isinstance(word, str), 'word must be an string'
        s = ''.join(i for i in word if not i.isdigit())  # remove numbers
        s = ut.tokenize(s).lower()  # tokenize
        s = s.replace(' ', '').replace('\n', '')  # remove spaces
        return s

    def _bsoup(self, link: str, encoding: str = 'utf-8') -> Optional['BeautifulSoup']:
        """
        Returns a parsed web.

        :param link: Link
        :param encoding: Web encoding
        :return: Parsed web. None if error
        """
        bs_keys = list(_CACHED_SOUPS.keys())
        if link in bs_keys:
            return _CACHED_SOUPS[link]
        if link in self._test_cached_file.keys():
            f = open(self._test_cached_file[link], 'r')
            data = ''.join(f.readlines())
        else:
            try:
                data = str(urlopen(link).read().decode(encoding))
            except (urllib.error.HTTPError, ValueError):
                return None
        bs = BeautifulSoup(data, 'html.parser')
        _CACHED_SOUPS[link] = bs
        if len(bs_keys) >= 50:
            del _CACHED_SOUPS[bs[0]]
        return bs

    def _synonym_com(self, word: str, _type: str) -> List[str]:
        """
        Retrieves synonyms from synonym.com.

        :param word: Word
        :param _type: Type (synonym, antonym)
        :return: Word list
        """
        assert _type in ('Synonyms', 'Antonyms')
        bs = self._bsoup(f'https://www.synonym.com/synonyms/{word}')
        results = bs.find_all('div', {'class': 'section'})
        en_words = []
        for section in results:  # Iterate each section
            title = section.find_all('h3', {'class': 'section-title'})
            if len(title) == 0:
                continue
            title = title[0].text
            if '.' not in title or 'Quotes containing' in title or 'Words that' in title or 'Example sententes' in title:
                continue
            for subsection in section.find_all('div', {'class': 'section-list-wrapper'}):
                section_type = subsection.find_all('h4', {'class': 'section-list-header'})
                if len(section_type) != 1:
                    continue
                section_type = section_type[0].text
                if section_type != _type:
                    continue
                sectionlist = subsection.find_all('ul', {'class': 'section-list'})
                if len(sectionlist) != 1:
                    continue
                for w in sectionlist[0].findAll('a'):
                    wr = w.text.strip()
                    if '(' not in wr and wr not in en_words:  # Avoid onld english
                        en_words.append(wr)
        return en_words

    @staticmethod
    def get_language_name(lang: str, lang_out: str = '') -> str:
        """
        Returns the name of a language.

        :param lang: Language tag (ISO 639)
        :param lang_out: Target language (ISO 639). If not supported, will return the English name
        :return: Language name from tag
        """
        return ut.get_language_name(lang, lang_out)

    def synonym(self, lang: str, word: str) -> List[str]:
        """
        Finds a synonyms for a given word.

        :param lang: Lang code
        :param word: Word to retrieve
        :return: Synonyms list
        """
        words = []
        word = self._process(word)
        if lang not in self._langs.keys() or not self._langs[lang][0]:
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

        # Customs
        if lang == 'en':
            en_words = self._synonym_com(word, 'Synonyms')
            for w in en_words:
                if w not in words:
                    words.append(w)
            words.sort()
        return words

    def antonym(self, lang: str, word: str) -> List[str]:
        """
        Finds a aynonyms for a given word.

        :param lang: Lang code
        :param word: Word to retrieve
        :return: Synonyms list
        """
        words = []
        word = self._process(word)
        if lang not in self._langs.keys() or not self._langs[lang][3]:
            raise InvalidLangCode(f'{lang} code is not supported for antonyms')

        if lang == 'en':
            en_words = self._synonym_com(word, 'Antonyms')
            for w in en_words:
                if w not in words:
                    words.append(w)
            words.sort()
        return words

    def meaning(self, lang: str, word: str) -> Tuple[List[str], str, str]:
        """
        Finds the meaning for a given word.

        :param lang: Lang code
        :param word: Word to retrieve
        :return: Meaning
        """
        types, words, wiki = [], '', ''
        word = self._process(word)
        if lang not in self._langs.keys() or not self._langs[lang][1]:
            raise InvalidLangCode(f'{lang} code is not supported for meanings')

        if lang in _EDUCALINGO:
            bs = self._bsoup(f'https://educalingo.com/en/dic-{lang}/{word}')
            if bs is not None:
                results = [i for i in bs.find_all('div', {'id': 'cuadro_categoria_gramatical'})]
                if len(results) == 1:
                    results = results[0]
                    for j in results.find_all('div', {'class': 'categoria_gramatical'}):
                        divj = j.find_all('div', {'class': 'circulo_categoria_gramatical'})
                        if len(divj) == 1:
                            divcls = divj[0].get('class')
                            if 'background_gris' not in divcls:
                                typej = j.find_all('div', {'class': 'texto_pie_categoria_gramatical'})
                                if len(typej) == 1:
                                    t = typej[0].text.strip().capitalize()
                                    if t != '':
                                        types.append(t)

                # Definition
                results = [i for i in bs.find_all('div', {'id': 'significado_de'})]
                if len(results) > 0:
                    words = results[0].text.strip().replace('\n', '')

                # Wikipedia
                results = [i for i in bs.find_all('span', {'id': 'wiki_introduccion'})]
                if len(results) > 0:
                    wiki = results[0].text.strip().replace('\n', '')

        return types, words, wiki

    # noinspection HttpUrlsUsage
    def meaning_wordnet(self, word: str) -> Dict[str, List[str]]:
        """
        Query the definition of an english word in WordNet.

        :param word: Word to query in English
        :return: Dict with Type, List of definitions
        """
        word = self._process(word)
        html = self._bsoup(f'http://wordnetweb.princeton.edu/perl/webwn?s={word}')
        types = html.findAll('h3')
        lists = html.findAll('ul')
        out = {}
        for a in types:
            reg = str(lists[types.index(a)])
            meanings = []
            for x in re.findall(r'\((.*?)\)', reg):
                if 'often followed by' in x:
                    pass
                elif len(x) > 5 or ' ' in str(x):
                    meanings.append(x.strip())
            name = a.text.strip()
            out[name] = meanings
        return out

    def translate(self, lang: str, word: str, to='') -> List[Tuple[str, str]]:
        """
        Translate a word.
l
        :param lang: Lang tag (ISO 639)
        :param word: Word to translate
        :param to: Target language (Google API)
        :return: List of (Lang tag, translated word)
        """
        assert isinstance(lang, str), 'lang code must be an string'
        assert isinstance(to, str), 'to lang code must be an string'
        words = []
        word = self._process(word)

        if to != '':
            gs = goslate.Goslate()
            try:
                return [(to, gs.translate(word, to, lang))]
            except (urllib.error.HTTPError, IndexError):
                warn(f'{word} cannot be translated to {to} as Google API is not available')

        if lang not in self._langs.keys() or not self._langs[lang][2]:
            raise InvalidLangCode(f'{lang} code is not supported for translation')

        if lang in _EDUCALINGO:
            bs = self._bsoup(f'https://educalingo.com/en/dic-{lang}/{word}')
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
                # lang_name = lang_name[0].text.strip().capitalize()

                # Find non-links
                lang_nonlink = j.find_all('span', {'class': 'negro'})
                if len(lang_nonlink) == 1:
                    words.append((lang_tag, lang_nonlink[0].text.strip()))
                    continue

                # Find links
                lang_link = j.find_all('strong', {})
                if len(lang_link) != 2:
                    continue
                lang_link = lang_link[1].find_all('a', {})
                if len(lang_link) == 1:
                    words.append((lang_tag, lang_link[0].text.strip()))

            # Sort translations
            words = sorted(words, key=lambda x: x[0])

        return words


class InvalidLangCode(Exception):
    """
    Invalid lang.
    """
