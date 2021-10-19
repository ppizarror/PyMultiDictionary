"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

DICTIONARY
Dictionary object.
"""

__all__ = [
    'get_language_name',
    'LANG_NAMES',
    'tokenize'
]

# noinspection PyPackageRequirements
from iso639 import Lang
# noinspection PyPackageRequirements
from iso639.exceptions import InvalidLanguageValue

from PyMultiDictionary._tokenizer import *

# Tokenizer
_TOKENIZER = RegexpTokenizer(r'\w+(?:-\w+)*')

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
    'hi': [('af', 'अफ़्रीकांस'), ('ar', 'अरबी'), ('bn', 'बांग्ला'), ('de', 'जर्मन'), ('el', 'ग्रीक'),
           ('en', 'अंग्रेज़ी'), ('es', 'स्पैनिश'), ('fr', 'फ़्रेंच'), ('hi', 'हिन्दी'), ('it', 'इटैलियन'),
           ('ja', 'जापानी'), ('jv', 'जैवेनीज़'), ('ko', 'कोरियन'), ('mr', 'मराठी'), ('ms', 'मलय'), ('no', 'नॉर्वेजियन'),
           ('pl', 'पोलिश'), ('pt', 'पुर्तगाली'), ('ro', 'रोमेनियन'), ('ru', 'रूसी'), ('sv', 'स्वीडिश'), ('ta', 'तमिल'),
           ('tr', 'तुर्क'), ('uk', 'यूक्रेनियन'), ('vi', 'वियतनामी'), ('zh', 'चीनी')],
    'it': [('af', 'Afrikaans'), ('ar', 'Arabo'), ('bn', 'Bengalese'), ('de', 'Tedesco'), ('el', 'Greco'),
           ('en', 'Inglese'), ('es', 'Spagnolo'), ('fr', 'Francese'), ('hi', 'Hindi'), ('it', 'Italiano'),
           ('ja', 'Giapponese'), ('jv', 'Giavanese'), ('ko', 'Coreano'), ('mr', 'Marathi'), ('ms', 'Malese'),
           ('no', 'Norvegese'), ('pl', 'Polacco'), ('pt', 'Portoghese'), ('ro', 'Rumeno'), ('ru', 'Russo'),
           ('sv', 'Svedese'), ('ta', 'Tamil'), ('tr', 'Turco'), ('uk', 'Ucraino'), ('vi', 'Vietnamita'),
           ('zh', 'Cinese')],
    'ja': [('af', 'アフリカーンス語'), ('ar', 'アラビア語'), ('bn', 'ベンガル語'), ('de', 'ドイツ語'), ('el', 'ギリシャ語'), ('en', '英語'),
           ('es', 'スペイン語'), ('fr', 'フランス語'), ('hi', 'ヒンディー語'), ('it', 'イタリア語'), ('ja', '日本語'), ('jv', 'ジャワ語'),
           ('ko', '韓国語'), ('mr', 'マラーティー語'), ('ms', 'マレー語'), ('no', 'ノルウェー語'), ('pl', 'ポーランド語'), ('pt', 'ポルトガル語'),
           ('ro', 'ルーマニア語'), ('ru', 'ロシア語'), ('sv', 'スウェーデン語'), ('ta', 'タミル語'), ('tr', 'トルコ語'), ('uk', 'ウクライナ語'),
           ('vi', 'ベトナム語'), ('zh', '中国語')],
    'jv': [('af', 'Basa afrikaans'), ('ar', 'Basa arab'), ('bn', 'Basa bengali'), ('de', 'Basa jerman'),
           ('el', 'Basa yunani'), ('en', 'Basa inggris'), ('es', 'Basa spanyol'), ('fr', 'Basa prancis'),
           ('hi', 'Basa india'), ('it', 'Basa italia'), ('ja', 'Basa jepang'), ('jv', 'Basa jawa'),
           ('ko', 'Basa korea'), ('mr', 'Basa marathi'), ('ms', 'Basa malaysia'), ('no', 'Basa norwegia'),
           ('pl', 'Basa polandia'), ('pt', 'Basa portugis'), ('ro', 'Basa romawi'), ('ru', 'Basa rusia'),
           ('sv', 'Basa swedia'), ('ta', 'Basa tamil'), ('tr', 'Basa turki'), ('uk', 'Basa ukrania'),
           ('vi', 'Basa vietnam'), ('zh', 'Basa cina')],
    'ko': [('af', '아프리칸스어'), ('ar', '아랍어'), ('bn', '벵골어'), ('de', '독일어'), ('el', '그리스어'), ('en', '영어'), ('es', '스페인어'),
           ('fr', '프랑스어'), ('hi', '힌디어'), ('it', '이탈리아어'), ('ja', '일본어'), ('jv', '자바어'), ('ko', '한국어'), ('mr', '마라티어'),
           ('ms', '말레이어'), ('no', '노르웨이어'), ('pl', '폴란드어'), ('pt', '포르투갈어'), ('ro', '루마니아어'), ('ru', '러시아어'),
           ('sv', '스웨덴어'), ('ta', '타밀어'), ('tr', '터키어'), ('uk', '우크라이나어'), ('vi', '베트남어'), ('zh', '중국어')],
    'mr': [('af', 'अफ्रिकान्स'), ('ar', 'अरबी'), ('bn', 'बंगाली'), ('de', 'जर्मन'), ('el', 'ग्रीक'), ('en', 'इंग्रजी'),
           ('es', 'स्पॅनिश'), ('fr', 'फ्रेंच'), ('hi', 'हिन्दी'), ('it', 'इटालियन'), ('ja', 'जपानी'), ('jv', 'जावानीज'),
           ('ko', 'कोरियन'), ('mr', 'मराठी'), ('ms', 'मलय'), ('no', 'नॉर्वेजियन'), ('pl', 'पोलिश'), ('pt', 'पोर्तुगीज'),
           ('ro', 'रोमानियन'), ('ru', 'रशियन'), ('sv', 'स्वीडिश'), ('ta', 'तमिळ'), ('tr', 'तुर्की'),
           ('uk', 'युक्रेनियन'), ('vi', 'व्हिएतनामी'), ('zh', 'चीनी')],
    'ms': [('af', 'Afrikaans'), ('ar', 'Amhara'), ('bn', 'Basque'), ('de', 'Chichewa'), ('el', 'Cina'),
           ('en', 'Corsica'), ('es', 'Czech'), ('fr', 'Frisia'), ('hi', 'Hindi'), ('it', 'Itali'), ('ja', 'Jepun'),
           ('jv', 'Jerman'), ('ko', 'Kreol haiti'), ('mr', 'Marathi'), ('ms', 'Melayu'), ('no', 'Parsi'),
           ('pl', 'Poland'), ('pt', 'Punjabi'), ('ro', 'Romania'), ('ru', 'Rusia'), ('sv', 'Swahili'),
           ('ta', 'Tagalog'), ('tr', 'Turki'), ('uk', 'Ukraine'), ('vi', 'Vietnam'), ('zh', 'Cina')],
    'pl': [('af', 'Afrikaans'), ('ar', 'Arabski'), ('bn', 'Bengalski'), ('de', 'Niemiecki'), ('el', 'Grecki'),
           ('en', 'Angielski'), ('es', 'Hiszpański'), ('fr', 'Francuski'), ('hi', 'Hindi'), ('it', 'Włoski'),
           ('ja', 'Japoński'), ('jv', 'Jawajski'), ('ko', 'Koreański'), ('mr', 'Marathi'), ('ms', 'Malajski'),
           ('no', 'Norweski'), ('pl', 'Polski'), ('pt', 'Portugalski'), ('ro', 'Rumuński'), ('ru', 'Rosyjski'),
           ('sv', 'Szwedzki'), ('ta', 'Tamilski'), ('tr', 'Turecki'), ('uk', 'Ukraiński'), ('vi', 'Wietnamski'),
           ('zh', 'Chiński')],
    'pt': [('af', 'Africâner'), ('ar', 'Arabe'), ('bn', 'Bengali'), ('de', 'Alemão'), ('el', 'Grego'), ('en', 'Inglês'),
           ('es', 'Espanhol'), ('fr', 'Francês'), ('hi', 'Hindi'), ('it', 'Italiano'), ('ja', 'Japonês'),
           ('jv', 'Javanês'), ('ko', 'Coreano'), ('mr', 'Marata'), ('ms', 'Malaio'), ('no', 'Norueguês'),
           ('pl', 'Polonês'), ('pt', 'Português'), ('ro', 'Romeno'), ('ru', 'Russo'), ('sv', 'Sueco'), ('ta', 'Tâmil'),
           ('tr', 'Turco'), ('uk', 'Ucraniano'), ('vi', 'Vietnamita'), ('zh', 'Chinês')],
    'ro': [('af', 'Afrikaans'), ('ar', 'Arabă'), ('bn', 'Bengali'), ('de', 'Germană'), ('el', 'Greacă'),
           ('en', 'Engleză'), ('es', 'Spaniolă'), ('fr', 'Franceză'), ('hi', 'Hindi'), ('it', 'Italiană'),
           ('ja', 'Japoneză'), ('jv', 'Javaneză'), ('ko', 'Coreeană'), ('mr', 'Marathi'), ('ms', 'Malaeză'),
           ('no', 'Norvegiană'), ('pl', 'Poloneză'), ('pt', 'Portugheză'), ('ro', 'Română'), ('ru', 'Rusă'),
           ('sv', 'Suedeză'), ('ta', 'Tamilă'), ('tr', 'Turcă'), ('uk', 'Ucraineană'), ('vi', 'Vietnameză'),
           ('zh', 'Chineză')],
    'ru': [('af', 'Африкаанс'), ('ar', 'Арабский'), ('bn', 'Бенгальский'), ('de', 'Немецкий'), ('el', 'Греческий'),
           ('en', 'Английский'), ('es', 'Испанский'), ('fr', 'Французский'), ('hi', 'Хинди'), ('it', 'Итальянский'),
           ('ja', 'Японский'), ('jv', 'Яванский'), ('ko', 'Корейский'), ('mr', 'Маратхи'), ('ms', 'Малайский'),
           ('no', 'Норвежский'), ('pl', 'Польский'), ('pt', 'Португальский'), ('ro', 'Румынский'), ('ru', 'Русский'),
           ('sv', 'Шведский'), ('ta', 'Тамильский'), ('tr', 'Турецкий'), ('uk', 'Украинский'), ('vi', 'Вьетнамский'),
           ('zh', 'Китайский')],
    'ta': [('af', 'ஆஃப்ரிக்கான்ஸ்'), ('ar', 'அரபிக்'), ('bn', 'வங்காளம்'), ('de', 'ஜெர்மன்'), ('el', 'கிரேக்கம்'),
           ('en', 'ஆங்கிலம்'), ('es', 'ஸ்பானிஷ்'), ('fr', 'ஃபிரெஞ்சு'), ('hi', 'இந்தி'), ('it', 'இத்தாலியன்'),
           ('ja', 'ஜாப்பனிஸ்'), ('jv', 'ஜாவனீஸ்'), ('ko', 'கொரியன்'), ('mr', 'மராத்தி'), ('ms', 'மலாய்'),
           ('no', 'நார்வீஜியன்'), ('pl', 'போலிஷ்'), ('pt', 'போர்ச்சுகீஸ்'), ('ro', 'ருமேனியன்'), ('ru', 'ரஷ்யன்'),
           ('sv', 'ஸ்வீடிஷ்'), ('ta', 'தமிழ்'), ('tr', 'துருக்கியம்'), ('uk', 'உக்ரைனியன்'), ('vi', 'வியட்னாமீஸ்'),
           ('zh', 'சீனம்')],
    'tr': [('af', 'Afrika dili'), ('ar', 'Arapça'), ('bn', 'Bengalce'), ('de', 'Almanca'), ('el', 'Yunanca'),
           ('en', 'İngilizce'), ('es', 'İspanyolca'), ('fr', 'Fransızca'), ('hi', 'Hintçe'), ('it', 'İtalyanca'),
           ('ja', 'Japonca'), ('jv', 'Cava dili'), ('ko', 'Korece'), ('mr', 'Marathi'), ('ms', 'Malezya dili'),
           ('no', 'Norveççe'), ('pl', 'Lehçe'), ('pt', 'Portekizce'), ('ro', 'Romence'), ('ru', 'Rusça'),
           ('sv', 'İsveççe'), ('ta', 'Tamil'), ('tr', 'Türkçe'), ('uk', 'Ukraynaca'), ('vi', 'Vietnamca'),
           ('zh', 'Çince')],
    'uk': [('af', 'Африкаанс'), ('ar', 'Арабська'), ('bn', 'Бенгальська'), ('de', 'Німецька'), ('el', 'Грецька'),
           ('en', 'Англійська'), ('es', 'Іспанська'), ('fr', 'Французька'), ('hi', 'Гінді'), ('it', 'Італійська'),
           ('ja', 'Японська'), ('jv', 'Яванська'), ('ko', 'Корейська'), ('mr', 'Маратхі'), ('ms', 'Малайська'),
           ('no', 'Норвезька'), ('pl', 'Польська'), ('pt', 'Португальська'), ('ro', 'Румунська'), ('ru', 'Російська'),
           ('sv', 'Шведська'), ('ta', 'Тамільська'), ('tr', 'Турецька'), ('uk', 'Українська'), ('vi', 'В’єтнамська'),
           ('zh', 'Китайська')],
    'zh': [('af', '布尔语(南非荷兰语)'), ('ar', '阿拉伯语'), ('bn', '孟加拉语'), ('de', '德语'), ('el', '希腊语'), ('en', '英语'),
           ('es', '西班牙语'), ('fr', '法语'), ('hi', '印地语'), ('it', '意大利语'), ('ja', '日语'), ('jv', '印尼爪哇语'), ('ko', '韩语'),
           ('mr', '马拉地语'), ('ms', '马来语'), ('no', '挪威语'), ('pl', '波兰语'), ('pt', '葡萄牙语'), ('ro', '罗马尼亚语'), ('ru', '俄语'),
           ('sv', '瑞典语'), ('ta', '泰米尔语'), ('tr', '土耳其语'), ('uk', '乌克兰语'), ('vi', '越南语'), ('zh', '中文')]

}


def get_language_name(tag: str, lang: str = '') -> str:
    """
    Returns a language name from its tag.

    :param tag: Language tag (ISO 639)
    :param lang: Target language (ISO 639). If not supported, will return the English name
    :return: Language name
    """
    assert isinstance(tag, str)
    assert isinstance(lang, str)
    if lang != '':
        if lang in LANG_NAMES.keys():
            for j in LANG_NAMES[lang]:
                if j[0] == tag:
                    return j[1]
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
    # Pre-process
    s = str(s)
    s = s.replace('_', ' ')  # Remove underscore
    s = s.replace('–', '-')  # uniform chars
    s = ''.join([i for i in s if not i.isdigit()])  # remove digits

    # Tokenize
    tok = _TOKENIZER.tokenize(s)
    if len(tok) >= 1:
        return ' '.join(_TOKENIZER.tokenize(s))
    else:
        return ''
