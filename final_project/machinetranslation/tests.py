import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_e2f_null_input(self):
        self.assertEqual(englishToFrench(None),None)

    def test_e2f(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_f2e_null_input(self):
        self.assertEqual(frenchToEnglish(None),None)

    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()