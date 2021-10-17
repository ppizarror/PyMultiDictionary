"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

TEST UTILS
Test utils.
"""

# noinspection PyProtectedMember
import PyMultiDictionary.version
from PyMultiDictionary._utils import detect_language, tokenize, get_language_name

import unittest


class UtilsTest(unittest.TestCase):

    def test_detect_language(self) -> None:
        """
        Test language recognition.
        """
        s = """From anchor-based frameworks, Wu et al. [1] used Mask-RCNN [2] to vectorize the walls
            by finding a rectangle proposal representing each segment's width, thickness, angle,
            and location. """
        self.assertEqual(detect_language(s), 'en')
        s = """El modelo propuesto contiene diferentes métricas para coordenar las tareas de segmentación"""
        self.assertEqual(detect_language(s), 'es')
        self.assertEqual(detect_language(''), '–')
        self.assertEqual(detect_language('https://epic.com'), '–')
        self.assertEqual(detect_language('好的'), 'zh')

    def test_language_name(self) -> None:
        """
        Test language name.
        """
        self.assertEqual(get_language_name('en'), 'English')
        self.assertEqual(get_language_name('es'), 'Spanish')
        self.assertEqual(get_language_name('unknown'), 'Unknown')
        self.assertEqual(get_language_name('zh'), 'Chinese')

    def test_tokenize(self) -> None:
        """
        Test tokenize.
        """
        s = """
        # ----------------------------------------------------------------------
        # Settings button
        # ----------------------------------------------------------------------


        """
        t = []
        for w in s.split(' '):
            tw = tokenize(w)
            if tw == '' or '\n' in tw:
                continue
            t.append(tw)
        self.assertEqual(t, ['#', '#', 'Settings', 'button', '#'])
        self.assertEqual(tokenize('hello!!___..'), 'hello')

    def test_version(self) -> None:
        """
        Test version.
        """
        self.assertTrue(isinstance(PyMultiDictionary.version.ver, str))
        self.assertTrue(isinstance(repr(PyMultiDictionary.version.vernum), str))
        self.assertTrue(isinstance(str(PyMultiDictionary.version.vernum), str))
