"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

TEST UTILS
Test utils.
"""

import PyMultiDictionary.version
# noinspection PyProtectedMember
from PyMultiDictionary._utils import tokenize, get_language_name

import unittest


class UtilsTest(unittest.TestCase):

    def test_language_name(self) -> None:
        """
        Test language name.
        """
        self.assertEqual(get_language_name('en'), 'English')
        self.assertEqual(get_language_name('en', 'es'), 'Inglés')
        self.assertEqual(get_language_name('es'), 'Spanish')
        self.assertEqual(get_language_name('unknown'), 'Unknown')
        self.assertEqual(get_language_name('zh'), 'Chinese')

    def test_tokenize(self) -> None:
        """
        Test tokenize.
        """
        s: str = """
        # ----------------------------------------------------------------------
        # Settings button
        # ----------------------------------------------------------------------


        """
        t: list = []
        for w in s.split(' '):
            tw = tokenize(w)
            if tw == '' or '\n' in tw:
                continue
            t.append(tw)
        self.assertEqual(t, ['Settings', 'button'])
        self.assertEqual(tokenize('hello!!___..'), 'hello')
        self.assertEqual(tokenize('hypen-word!!1111'), 'hypen-word')
        self.assertEqual(tokenize('8934205@@hypen-word!!1111'), 'hypen-word')
        self.assertEqual(tokenize('@@hypen-word!!1111'), 'hypen-word')
        self.assertEqual(tokenize('893420  5@@  hypen-word!!1111'), 'hypen-word')
        self.assertEqual(tokenize('893420  5@@  hypen–word!!1111'), 'hypen-word')
        self.assertEqual(tokenize('hyphen_word'), 'hyphen word')
        self.assertEqual(tokenize('__________________hyphen___word'), 'hyphen word')
        self.assertEqual(tokenize('__________________hyphen-word'), 'hyphen-word')
        self.assertEqual(tokenize('12345aaa31123'), 'aaa')
        self.assertEqual(tokenize('!!!'), '')
        self.assertEqual(tokenize('for these reasons'), 'for these reasons')
        self.assertEqual(tokenize('for                       these reasons'), 'for these reasons')

    def test_version(self) -> None:
        """
        Test version.
        """
        self.assertTrue(isinstance(PyMultiDictionary.version.ver, str))
        self.assertTrue(isinstance(repr(PyMultiDictionary.version.vernum), str))
        self.assertTrue(isinstance(str(PyMultiDictionary.version.vernum), str))
