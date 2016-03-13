import requests

_BASE_WORD_URL = 'http://www.dictionary.com/browse/'
_DEFAULT_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'host': 'www.dictionary.com'
}


def get_word_page(word, timeout=None):
    return requests.get(
        _BASE_WORD_URL + word,
        headers=_DEFAULT_HEADERS,
        timeout=timeout)


def download_word_pronunciation(url):
    res = requests.get(url, headers=_DEFAULT_HEADERS)
    audio = res.content
    content_type = res.headers.get('content-type', 'audio/mpeg3')
    return audio, content_type
