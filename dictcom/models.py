from dictcom.download import download_word_pronunciation


class Word():
    def __init__(self, word, defs, pronunciation, pronunciation_url=None):
        self.word = word
        self.defs = defs
        self.pronunciation = pronunciation
        self.pronunciation_url = pronunciation_url
        self.pronunciation_audio = None

    def download_pronunciation_audio(self):
        audio, content_type = download_word_pronunciation(
            self.pronunciation_url)
        self.pronunciation_audio = WordPronunciation(audio, content_type)

    def get_pronunciation_audio(self):
        if self.pronunciation_audio is None:
            self.download_pronunciation_audio()
        return self.pronunciation_audio

    def __str__(self):
        parts = [
            '----{}---- {}\n'.format(self.word, self.pronunciation or '')]
        for pos in self.defs:
            def_list = self.defs[pos]
            parts.append('[{}]\n'.format(pos))
            for idx, d in enumerate(def_list):
                parts.append('{}. {}\n'.format(idx, d.text))
                if d.example is not None:
                    parts.append('({})\n'.format(d.example))
            parts.append('\n')
        return ''.join(parts)

    def __eq__(self, other):
        return self.word == other.word and \
            dict(self.defs) == dict(other.defs) and \
            self.pronunciation == other.pronunciation and \
            self.pronunciation_url == other.pronunciation_url

    def __ne__(self, other):
        return not self == other


class Definition():
    def __init__(self, text, example=None):
        self.text = text
        self.example = example

    def __eq__(self, other):
        return self.text == other.text and self.example == other.example

    def __ne__(self, other):
        return not self == other


class WordPronunciation():
    def __init__(self, audio, content_type):
        self.audio = audio
        self.content_type = content_type
