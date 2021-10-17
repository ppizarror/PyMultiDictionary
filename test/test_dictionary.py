"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

TEST DICTIONARY
Test dictionary object.
"""

from PyMultiDictionary import MultiDictionary
# noinspection PyProtectedMember
from PyMultiDictionary._dictionary import InvalidLangCode
import os
import unittest


class DictionaryTest(unittest.TestCase):

    # noinspection HttpUrlsUsage
    @staticmethod
    def _get_dictionary() -> 'MultiDictionary':
        """
        Returns a dictionary prepared for tests.
        """
        d = MultiDictionary()

        # Set example pages
        __actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace('\\', '/') + '/'
        d._test_cached_file = {
            'https://educalingo.com/en/dic-en/good': __actualpath + 'data/educalingo_en_good.html',
            'https://www.synonym.com/synonyms/good': __actualpath + 'data/synonyms_en_good.html',
            'http://wordnetweb.princeton.edu/perl/webwn?s=good': __actualpath + 'data/wordnet_en_good.html'
        }

        return d

    def test_process(self) -> None:
        """
        Test word parse before process.
        """
        d = self._get_dictionary()

        # Test word parse
        self.assertEqual(d._process('word!!!  '), 'word')
        self.assertEqual(d._process('invalid1'), 'invalid')
        self.assertEqual(d._process('multiple words'), 'multiple')
        self.assertEqual(d._process('multiple!!!! words'), 'multiple')
        self.assertEqual(d._process('Abstract'), 'abstract')
        self.assertEqual(d._process('1234Abstract'), 'abstract')
        self.assertEqual(d._process('1234          Abstract'), 'abstract')
        self.assertEqual(d._process('1234 !!! .....        Abstract'), 'abstract')
        self.assertEqual(d._process('word.epic'), 'word')
        self.assertEqual(d._process('  '), '')
        self.assertEqual(d._process('\n\n!\nthis word'), 'this')
        self.assertEqual(d._process('<hack>'), 'hack')

    def test_meaning(self) -> None:
        """
        Test word meaning.
        """
        d = self._get_dictionary()

        ds = 'The first definition of good in the dictionary is having admirable, ' \
             'pleasing, superior, or positive qualities; not negative, bad or mediocre. ' \
             'Other definition of good is morally excellent or admirable; virtuous; ' \
             'righteous. Good is also suitable or efficient for a purpose.'
        wiki = 'Good may refer to: ▪ Good and evil, the distinction between positive and ' \
               'negative entities ▪ Good, objects produced for market ▪ Good ▪ Good ▪ Good, ' \
               "West Virginia, USA ▪ Form of the Good, Plato's macrocosmic view of goodness " \
               'in living Expressive works: ▪ Good ▪ Good, a 2008 film starring Viggo ' \
               'Mortensen ▪ Good ▪ Good ▪ Good, by Cecil Philip Taylor Companies: ▪ Good ' \
               'Entertainment ▪ GOOD Music, a record label ▪ Good Technology Music: ▪ ' \
               '"Good", a song by Better Than Ezra from Deluxe...'
        self.assertEqual(d.meaning('en', 'good'), (['Noun', 'Adjective', 'Exclamation'], ds, wiki))

        # Test invalid link
        self.assertIsNone(d._bsoup('abc'))
        self.assertIsNone(d._bsoup('abc1234aaaaaa.com'))

    def test_meaning_wordnet(self) -> None:
        """
        Test word meaning in wordnet.
        """
        d = self._get_dictionary()
        out = {'Noun': ['benefit', 'moral excellence or admirableness', 'that which is pleasing or valuable or useful',
                        'articles of commerce'],
               'Adjective': ['having desirable or positive qualities especially those suitable for a thing specified',
                             'having the normally expected amount', 'morally admirable',
                             'deserving of esteem and respect', 'promoting or enhancing well-being',
                             'agreeable or pleasing', 'of moral excellence',
                             'having or showing knowledge and skill and aptitude', 'thorough',
                             'with or in a close or intimate relationship', 'financially safe',
                             'most suitable or right for a particular purpose', 'resulting favorably',
                             'exerting force or influence', 'or in force', 'capable of pleasing',
                             'appealing to the mind', 'in excellent physical condition',
                             'tending to promote physical well-being; beneficial to health', 'not forged',
                             'not left to spoil', 'generally admired'],
               'Adverb': ['(often used as a combining form', "`good' is a nonstandard dialectal variant for `well'",
                          "completely and absolutely (`good' is sometimes used informally for `thoroughly'"]}
        self.assertEqual(d.meaning_wordnet('good'), out)

    def test_translate(self) -> None:
        """
        Test word parse before process.
        """
        d = self._get_dictionary()

        # Translate
        tr = [('af', 'goeie'),
              ('ar', 'جَيِّد'),
              ('bn', 'ভাল'),
              ('de', 'gut'),
              ('el', 'καλός'),
              ('en', 'good'),
              ('es', 'bueno'),
              ('fr', 'bon'),
              ('hi', 'अच्छा'),
              ('it', 'buono'),
              ('ja', '良い'),
              ('jv', 'Apik'),
              ('ko', '좋은'),
              ('mr', 'चांगले'),
              ('ms', 'baik'),
              ('no', 'bra'),
              ('pl', 'dobry'),
              ('pt', 'bom'),
              ('ro', 'bun'),
              ('ru', 'хороший'),
              ('sv', 'bra'),
              ('ta', 'நல்ல'),
              ('tr', 'iyi'),
              ('uk', 'гарний'),
              ('vi', 'tốt'),
              ('zh', '好的')]
        s = d.translate('en', 'good')
        self.assertEqual(s, tr)
        self.assertIsInstance(d.translate('en', 'epic'), list)

        # Translate another language
        d.translate('en', 'Good', to='ru')

    def test_synonym(self) -> None:
        """
        Test word synonym.
        """
        d = self._get_dictionary()

        # Synonyms
        syn = ['able', 'acceptable', 'accomplished', 'accurate', 'adept', 'adequate', 'admirable', 'adroit',
               'advantage', 'advantageous', 'agreeable', 'altruistic', 'ample', 'angelic', 'angelical', 'appropriate',
               'auspicious', 'authentic', 'avail', 'awesome', 'bad', 'balmy', 'bang-up', 'barrie', 'beatific', 'beaut',
               'behalf', 'belting', 'beneficence', 'beneficent', 'beneficial', 'benefit', 'benevolent', 'benignancy',
               'benignity', 'best', 'better', 'bitchin´', 'bona fide', 'booshit', 'bright', 'bully', 'calm', 'capable',
               'capital', 'charitable', 'cheerful', 'choice', 'clean', 'clear', 'clement', 'clever', 'cloudless',
               'commendable', 'common good', 'compelling', 'competent', 'complete', 'congenial', 'considerable',
               'constructive', 'convenient', 'convincing', 'convivial', 'corking', 'correct', 'cracking', 'crucial',
               'dandy', 'decorous', 'definite', 'dependable', 'desirability', 'desirable', 'dexterous', 'dinkum',
               'divine', 'dope', 'dutiful', 'eatable', 'edible', 'efficient', 'enjoyable', 'enjoyment', 'entire',
               'estimable', 'ethical', 'exact', 'excellence', 'excellent', 'exemplary', 'exo', 'expert', 'extensive',
               'fair', 'fancy', 'favorable', 'favourable', 'fine', 'finest', 'first-class', 'first-rate', 'fit',
               'fitting', 'friendly', 'full', 'gain', 'genuine', 'good enough', 'goodish', 'goodness', 'goody-goody',
               'gracious', 'graciousness', 'gratifying', 'great', 'groovy', 'halcyon', 'happy', 'healthy', 'helpful',
               'honest', 'honorable', 'honourable', 'humane', 'in order', 'interest', 'judicious', 'keen', 'kind',
               'kind-hearted', 'kindly', 'kindness', 'large', 'legitimate', 'long', 'lucrative', 'mannerly', 'merciful',
               'merit', 'mild', 'moral', 'moral excellence', 'morality', 'neat', 'nice', 'nifty', 'not bad', 'obedient',
               'obliging', 'of a high standard', 'of high quality', 'opportune', 'optimum', 'orderly', 'peachy',
               'pearler', 'persuasive', 'phat', 'pleasant', 'pleasing', 'pleasurable', 'polite', 'positive',
               'praiseworthy', 'precise', 'principled', 'probity', 'productive', 'proficient', 'profit', 'profitable',
               'proper', 'propitious', 'prudent', 'quality', 'rad', 'real', 'reasonable', 'rectitude', 'redeeming',
               'redemptive', 'reliable', 'respectable', 'right', 'righteous', 'righteousness', 'sainted', 'saintlike',
               'saintly', 'salubrious', 'salutary', 'satisfactory', 'satisfying', 'saving', 'schmick', 'seemly',
               'sensible', 'service', 'shrewd', 'sik', 'skilled', 'slap-up', 'smashing', 'solid', 'sound', 'soundness',
               'special', 'splendid', 'substantial', 'sufficient', 'suitable', 'summum bonum', 'sunny', 'sunshiny',
               'super', 'superb', 'superior', 'swell', 'talented', 'tasty', 'thorough', 'timely', 'tiptop', 'true',
               'trustworthy', 'uncorrupted', 'untainted', 'up to scratch', 'up to the mark', 'upright', 'uprightness',
               'upstanding', 'use', 'useful', 'usefulness', 'valid', 'valuable', 'vantage', 'virtue', 'virtuous',
               'virtuousness', 'welfare', 'well', 'well behaved', 'well-behaved', 'well-being', 'well-disposed',
               'well-mannered', 'well-reasoned', 'well-thought-out', 'well-timed', 'wellbeing', 'white', 'whole',
               'wholesome', 'wicked', 'wisdom', 'wise', 'wiseness', 'world-class', 'worth', 'worthiness', 'worthwhile',
               'worthy']
        self.assertEqual(d.synonym('en', 'good'), syn)
        self.assertIsInstance(d.synonym('en', 'epic'), list)

        # Invalid codes
        self.assertRaises(InvalidLangCode, lambda: d.synonym('unknown', 'word'))

    def test_antonym(self) -> None:
        """
        Test antonyms.
        """
        d = self._get_dictionary()
        self.assertRaises(InvalidLangCode, lambda: d.antonym('es', 'word'))

        ant = ['bad', 'badness', 'cold', 'cool', 'disobedience', 'domineering', 'evil', 'evilness', 'fidelity',
               'fruitfulness', 'immoral', 'immorality', 'lowercase', 'maleficence', 'malignancy', 'malignity',
               'naivete', 'nonpregnant', 'ordinary', 'passionless', 'unemotionality', 'unfavorable', 'unpropitious',
               'unrespectable', 'unrighteous', 'unsoundness', 'unworthiness', 'unworthy', 'wicked', 'worse', 'worst',
               'worthlessness', 'wrong']
        self.assertEqual(d.antonym('en', 'good'), ant)

    def test_language_name(self) -> None:
        """
        Test language name.
        """
        d = self._get_dictionary()
        self.assertEqual(d.get_language_name('en'), 'English')
        self.assertEqual(d.get_language_name('en', 'es'), 'Inglés')
        self.assertEqual(d.get_language_name('es'), 'Spanish')
        self.assertEqual(d.get_language_name('unknown'), 'Unknown')
        self.assertEqual(d.get_language_name('zh'), 'Chinese')
