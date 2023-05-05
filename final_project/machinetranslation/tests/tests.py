import unittest

from machinetranslation import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_e2f_null_input(self):
        self.assertEqual(english_to_french(None),None)

    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_f2e_null_input(self):
        self.assertEqual(french_to_english(None),None)

    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()