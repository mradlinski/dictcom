from dictcom.download import get_word_page
from dictcom.parse import parse_word_page


def get_word(word, silence_errors=False, timeout=None):
    try:
        page = get_word_page(word, timeout=timeout)
        if page.status_code != 200:
            return None

        word_def = parse_word_page(word, page.text)
    except:
        if silence_errors:
            return None
        raise

    return word_def


def get_word_pronunciation(word, timeout=None):
    parsed_word = get_word(word)
    return parsed_word.get_pronunciation_audio()
