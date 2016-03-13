import unittest
import dictcom

_TEST_WORDS = ('pinnate', 'gnathonic', 'something', 'what\'s up')
_TEST_FAKE_WORD = 'kdfsjdfgoir'


class DownloadTest(unittest.TestCase):
    def for_every_word(self, fn):
        for w in _TEST_WORDS:
            fn(w)

    def test_page_downloading(self):
        def test(w):
            html = dictcom.download.get_word_page(w).text
            self.assertTrue(w in html)
        self.for_every_word(test)

    def test_page_downloading_not_found(self):
        self.assertEqual(
            dictcom.download.get_word_page(_TEST_FAKE_WORD).status_code, 404)
