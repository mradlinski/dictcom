import unittest
import dictcom
from examples import data


class ParseTest(unittest.TestCase):
    def test_examples(self):
        for ex in data:
            w = dictcom.parse_word_page('test', ex['html'])
            self.assertEqual(w, ex['result'])
