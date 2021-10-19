""""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

PyMultiDictionary is a Dictionary Module for Python 2 to get meanings, translations, synonyms and antonyms of words in 20 different languages.
"""

try:
    from PyMultiDictionary._dictionary import *
except ModuleNotFoundError:
    pass
import PyMultiDictionary.version

__author__ = 'Pablo Pizarro R.'
__copyright__ = 'Copyright 2021 Pablo Pizarro R. @ppizarror'
__description__ = 'PyMultiDictionary is a Dictionary Module for Python 2 to get meanings, translations, synonyms and antonyms of words in 20 different languages'
__email__ = 'pablo@ppizarror.com'
__keywords__ = 'dictionary multi-language synonym antonym definition'
__license__ = 'MIT'
__module_name__ = 'PyMultiDictionary'
__url__ = 'https://github.com/ppizarror/PyMultiDictionary'
__url_bug_tracker__ = 'https://github.com/ppizarror/PyMultiDictionary'
__url_documentation__ = 'https://github.com/ppizarror/PyMultiDictionary'
__url_source_code__ = 'https://github.com/ppizarror/PyMultiDictionary'
__version__ = PyMultiDictionary.version.ver
