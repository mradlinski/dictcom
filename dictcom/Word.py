from dictcom.download import download_word_pronunciation


class Word():
    def __init__(self, word, defs, pronunciation, pronunciation_url=None):
        self.word = word
        self.defs = defs
        self.pronunciation = pronunciation
        self.pronunciation_url = pronunciation_url
        self.pronunciation_audio = None

    def download_pronunciation_audio(self):
        audio, content_type = download_word_pronunciation(self.word)
        self.pronunciation_audio = WordPronunciation(audio, content_type)

    def get_pronunciation_audio(self):
        if self.pronunciation_audio is None:
            self.download_pronunciation()
        return self.pronunciation_audio

    def pretty_print(self):
        print('----{0}---- {1}'.format(self.word, self.pronunciation or ''))
        for pos in self.defs:
            def_list = self.defs[pos]
            print('[{0}]'.format(pos))
            for idx, d in enumerate(def_list):
                print('{0}. {1}'.format(idx, d.text))
                if d.example is not None:
                    print('({0})'.format(d.example))
            print('\n')


class Definition():
    def __init__(self, text, example=None):
        self.text = text
        self.example = example


class WordPronunciation():
    def __init__(self, audio, content_type):
        self.audio = audio
        self.content_type = content_type
