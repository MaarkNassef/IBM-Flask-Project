import unittest
from machinetranslation.translator import english_to_french, french_to_english

class AppTest(unittest.TestCase):
    def test_en_fr_none(self):
        self.assertEqual(english_to_french(''), '')

    def test_fr_en_none(self):
        self.assertEqual(french_to_english(''), '')

    def test_en_fr_1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_fr_en_1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()