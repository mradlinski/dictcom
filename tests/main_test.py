import unittest
import dictcom


class MainTest(unittest.TestCase):
    def word_check_helper(
        self,
        word,
        should_have_pronunciation,
        should_have_pronunciation_audio
    ):
        parsed = dictcom.get_word(word)
        self.assertIsInstance(parsed, dictcom.models.Word)
        self.assertEqual(parsed.word, word)
        self.assertIsNotNone(parsed.defs)
        self.assertGreater(len(parsed.defs), 0)

        first_defs = list(parsed.defs.values())[0]
        self.assertGreater(len(first_defs), 0)
        self.assertIsInstance(first_defs[0], dictcom.models.Definition)
        self.assertIsNotNone(first_defs[0].text)

        if should_have_pronunciation:
            self.assertIsNotNone(parsed.pronunciation)
        if should_have_pronunciation_audio:
            self.assertIsNotNone(parsed.pronunciation_url)
            self.assertIsNotNone(parsed.get_pronunciation_audio())

    def test_get_word(self):
        self.word_check_helper('pinnate', True, True)
        self.word_check_helper('gnathonic', True, True)
        self.word_check_helper('something', True, True)
        self.word_check_helper('goddammit', True, True)
        self.word_check_helper('who', True, True)
        self.word_check_helper('what', True, True)
        self.word_check_helper('yolo', True, True)
        self.word_check_helper('what\'s up', False, False)
        self.word_check_helper('speak up', False, False)

    def test_get_word_not_found(self):
        word = dictcom.get_word('dsakjadsfkf')
        self.assertIsNone(word)

    # def test_wotds(self):
    #     import datetime, requests
    #     from bs4 import BeautifulSoup
    #     date = datetime.date.today()
    #     for i in range(200):
    #         date_string = date.strftime('%Y/%m/%d')
    #         wotd_id = date.strftime('#wotd-%Y-%m-%d')
    #
    #         wotd_page = requests.get('http://www.dictionary.com/wordoftheday/' + date_string).text
    #         soup = BeautifulSoup(wotd_page, 'html.parser')
    #         word = soup.select(wotd_id)[0].get('data-word')
    #
    #         try:
    #             word_defs = dictcom.get_word(word)
    #         except Exception as e:
    #             print(word)
    #             raise e
    #
    #         date = date - datetime.timedelta(1)
    #         # time.sleep(5)
    #         print('-')
