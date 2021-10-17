"""
PyDetex
https://github.com/ppizarror/PyDetex

TEST UTILS
Test utils.
"""

import os
import unittest


class UtilsTest(unittest.TestCase):

    def test_dictionary(self) -> None:
        """
        Test dictionary.
        """
        d = ut.Dictionary()

        # Get lang names
        s = d.translate('en', 'good')
        print([(tag, lang) for (lang, tag, _) in sorted(s, key=lambda x: x[1])])
        return

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

        # Definition
        __actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace('\\', '/') + '/'
        d._test_cached_file = __actualpath + 'data/educalingo_en_good.html'
        tr = """The first definition of good in the dictionary is having admirable, pleasing, superior, or positive qualities; not negative, bad or mediocre. Other definition of good is morally excellent or admirable; virtuous; righteous. Good is also suitable or efficient for a purpose. 

Good may refer to: ▪ Good and evil, the distinction between positive and negative entities ▪ Good, objects produced for market ▪ Good ▪ Good ▪ Good, West Virginia, USA ▪ Form of the Good, Plato's macrocosmic view of goodness in living Expressive works: ▪ Good ▪ Good, a 2008 film starring Viggo Mortensen ▪ Good ▪ Good ▪ Good, by Cecil Philip Taylor Companies: ▪ Good Entertainment ▪ GOOD Music, a record label ▪ Good Technology Music: ▪ "Good", a song by Better Than Ezra from Deluxe..."""
        self.assertEqual(d.definition('en', 'good'), tr)

        # Translate
        tr = [('Chinese', 'zh-cn', '好的'),
              ('Spanish', 'es', 'bueno'),
              ('English', 'en', 'good'),
              ('Hindi', 'hi', 'अच्छा'),
              ('Arabic', 'ar', 'جَيِّد'),
              ('Russian', 'ru', 'хороший'),
              ('Portuguese', 'pt', 'bom'),
              ('Bengali', 'bn', 'ভাল'),
              ('French', 'fr', 'bon'),
              ('Malay', 'ms', 'baik'),
              ('German', 'de', 'gut'),
              ('Japanese', 'ja', '良い'),
              ('Korean', 'ko', '좋은'),
              ('Javanese', 'jv', 'Apik'),
              ('Vietnamese', 'vi', 'tốt'),
              ('Tamil', 'ta', 'நல்ல'),
              ('Marathi', 'mr', 'चांगले'),
              ('Turkish', 'tr', 'iyi'),
              ('Italian', 'it', 'buono'),
              ('Polish', 'pl', 'dobry'),
              ('Ukrainian', 'uk', 'гарний'),
              ('Romanian', 'ro', 'bun'),
              ('Greek', 'el', 'καλός'),
              ('Afrikaans', 'af', 'goeie'),
              ('Swedish', 'sv', 'bra'),
              ('Norwegian', 'no', 'bra')]
        s = d.translate('en', 'good')
        self.assertEqual(s, tr)

        # Synonyms
        syn = ['able', 'acceptable', 'accomplished', 'accurate', 'adept', 'adequate', 'admirable', 'adroit',
               'advantage', 'advantageous', 'agreeable', 'altruistic', 'ample', 'appropriate', 'auspicious',
               'authentic', 'avail', 'awesome', 'bad', 'balmy', 'barrie', 'beaut', 'behalf', 'belting', 'beneficent',
               'beneficial', 'benefit', 'benevolent', 'best', 'bitchin´', 'bona fide', 'booshit', 'bright', 'calm',
               'capable', 'capital', 'charitable', 'cheerful', 'choice', 'clear', 'clement', 'clever', 'cloudless',
               'commendable', 'compelling', 'competent', 'complete', 'congenial', 'considerable', 'constructive',
               'convenient', 'convincing', 'convivial', 'correct', 'crucial', 'decorous', 'definite', 'dependable',
               'desirable', 'dexterous', 'dinkum', 'divine', 'dope', 'dutiful', 'eatable', 'edible', 'efficient',
               'enjoyable', 'entire', 'estimable', 'ethical', 'exact', 'excellence', 'excellent', 'exemplary', 'exo',
               'expert', 'extensive', 'fair', 'fancy', 'favourable', 'fine', 'finest', 'first-class', 'first-rate',
               'fit', 'fitting', 'friendly', 'full', 'gain', 'genuine', 'goodness', 'gracious', 'gratifying', 'great',
               'halcyon', 'happy', 'healthy', 'helpful', 'honest', 'honourable', 'humane', 'interest', 'judicious',
               'kind', 'kind-hearted', 'kindly', 'large', 'legitimate', 'long', 'lucrative', 'mannerly', 'merciful',
               'merit', 'mild', 'moral', 'morality', 'obedient', 'obliging', 'opportune', 'orderly', 'pearler',
               'persuasive', 'phat', 'pleasant', 'pleasing', 'pleasurable', 'polite', 'positive', 'praiseworthy',
               'precise', 'probity', 'productive', 'proficient', 'profit', 'profitable', 'proper', 'propitious',
               'prudent', 'rad', 'real', 'reasonable', 'rectitude', 'reliable', 'right', 'righteous', 'righteousness',
               'salubrious', 'salutary', 'satisfactory', 'satisfying', 'schmick', 'seemly', 'sensible', 'service',
               'shrewd', 'sik', 'skilled', 'solid', 'sound', 'special', 'splendid', 'substantial', 'sufficient',
               'suitable', 'sunny', 'sunshiny', 'super', 'superb', 'superior', 'talented', 'tasty', 'thorough',
               'timely', 'tiptop', 'true', 'trustworthy', 'uncorrupted', 'untainted', 'upright', 'uprightness', 'use',
               'useful', 'usefulness', 'valid', 'valuable', 'virtue', 'virtuous', 'welfare', 'well-behaved',
               'well-disposed', 'well-mannered', 'well-reasoned', 'well-thought-out', 'well-timed', 'wellbeing',
               'whole', 'wholesome', 'wicked', 'wise', 'world-class', 'worth', 'worthwhile', 'worthy']
        self.assertEqual(d.synonym('en', 'good'), syn)

        # Synonyms
        self.assertEqual(d.synonym('unknown', 'word'), [])
