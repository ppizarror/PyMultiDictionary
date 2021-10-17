"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

DICTIONARY
Dictionary object.
"""

__all__ = [
    'detect_language',
    'get_language_name',
    'LANG_NAMES',
    'tokenize'
]

# langdetect supports:
# af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
# hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
# pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw
import langdetect

# noinspection PyPackageRequirements
from iso639 import Lang
# noinspection PyPackageRequirements
from iso639.exceptions import InvalidLanguageValue

from nltk.tokenize import RegexpTokenizer as _RegexpTokenizer

# Tokenizer
_TOKENIZER = _RegexpTokenizer(r'\w+')

# Enhanced lang names
LANG_NAMES = {
    'bn': [('af', 'আফ্রিকান'), ('ar', 'আরবী'), ('bn', 'বাংলা'), ('de', 'জার্মান'), ('el', 'গ্রীক্\u200c'),
           ('en', 'ইংরেজী'), ('es', 'স্পেনীয়'), ('fr', 'ফরাসি'), ('hi', 'হিন্দি'), ('it', 'ইতালীয়'), ('ja', 'জাপানি'),
           ('jv', 'জাভানি'), ('ko', 'কোরিয়ান'), ('mr', 'মারাঠি'), ('ms', 'মালে'), ('no', 'নরওয়েজীয়'),
           ('pl', 'পোলীশ'), ('pt', 'পর্তুগীজ'), ('ro', 'রোমানীয়'), ('ru', 'রুশ'), ('sv', 'সুইডিশ'), ('ta', 'তামিল'),
           ('tr', 'তুর্কী'), ('uk', 'ইউক্রেনীয়'), ('vi', 'ভিয়েতনামিয়'), ('zh', 'চীনা')],
    'de': [('af', 'Afrikaans'), ('ar', 'Arabisch'), ('bn', 'Bengalisch'), ('de', 'Deutsch'), ('el', 'Griechisch'),
           ('en', 'Englisch'), ('es', 'Spanisch'), ('fr', 'Französisch'), ('hi', 'Hindi'), ('it', 'Italienisch'),
           ('ja', 'Japanisch'), ('jv', 'Javanisch'), ('ko', 'Koreanisch'), ('mr', 'Marathi'), ('ms', 'Malaysisch'),
           ('no', 'Norwegisch'), ('pl', 'Polnisch'), ('pt', 'Portugiesisch'), ('ro', 'Rumänisch'), ('ru', 'Russisch'),
           ('sv', 'Schwedisch'), ('ta', 'Tamil'), ('tr', 'Türkisch'), ('uk', 'Ukrainisch'), ('vi', 'Vietnamesisch'),
           ('zh', 'Chinesisch')],
    'en': [('af', 'Afrikaans'), ('ar', 'Arabic'), ('bn', 'Bengali'), ('de', 'German'), ('el', 'Greek'),
           ('en', 'English'), ('es', 'Spanish'), ('fr', 'French'), ('hi', 'Hindi'), ('it', 'Italian'),
           ('ja', 'Japanese'), ('jv', 'Javanese'), ('ko', 'Korean'), ('mr', 'Marathi'), ('ms', 'Malay'),
           ('no', 'Norwegian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'),
           ('sv', 'Swedish'), ('ta', 'Tamil'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('vi', 'Vietnamese'),
           ('zh', 'Chinese')],
    'es': [('af', 'Afrikáans'), ('ar', 'Árabe'), ('bn', 'Bengalí'), ('de', 'Alemán'), ('el', 'Griego'),
           ('en', 'Inglés'), ('es', 'Español'), ('fr', 'Francés'), ('hi', 'Hindi'), ('it', 'Italiano'),
           ('ja', 'Japonés'), ('jv', 'Javanés'), ('ko', 'Coreano'), ('mr', 'Maratí'), ('ms', 'Malayo'),
           ('no', 'Noruego'), ('pl', 'Polaco'), ('pt', 'Portugués'), ('ro', 'Rumano'), ('ru', 'Ruso'), ('sv', 'Sueco'),
           ('ta', 'Tamil'), ('tr', 'Turco'), ('uk', 'Ucraniano'), ('vi', 'Vietnamita'), ('zh', 'Chino')],
    'fr': [('af', 'Afrikaans'), ('ar', 'Arabe'), ('bn', 'Bengali'), ('de', 'Allemand'), ('el', 'Grec'),
           ('en', 'Anglais'), ('es', 'Espagnol'), ('fr', 'Français'), ('hi', 'Hindi'), ('it', 'Italien'),
           ('ja', 'Japonais'), ('jv', 'Javanais'), ('ko', 'Coréen'), ('mr', 'Marathi'), ('ms', 'Malaisien'),
           ('no', 'Norvégien'), ('pl', 'Polonais'), ('pt', 'Portugais'), ('ro', 'Roumain'), ('ru', 'Russe'),
           ('sv', 'Suédois'), ('ta', 'Tamoul'), ('tr', 'Turc'), ('uk', 'Ukrainien'), ('vi', 'Vietnamien'),
           ('zh', 'Chinois')],
    'hi': [

    ]
}


def detect_language(s):
    """
    Detects languages.

    :param s: String
    :return: Detected language
    """
    s = str(s)
    if s == '':
        return '–'
    try:
        lang = langdetect.detect(s)
        if lang == 'zh-cn' or lang == 'zh-tw':
            lang = 'zh'
        return lang
    except langdetect.lang_detect_exception.LangDetectException:  # No features in text
        return '–'


def get_language_name(tag: str) -> str:
    """
    Returns a language name from its tag.

    :param tag: Language tag
    :return: Language name
    """
    try:
        return Lang(tag).name
    except InvalidLanguageValue:
        return 'Unknown'


def tokenize(s: str) -> str:
    """
    Tokenize a given word.

    :param s: Word
    :return: Tokenized word
    """
    s = str(s)
    try:
        return _TOKENIZER.tokenize(s)[0]
    except IndexError:
        pass
    return s
