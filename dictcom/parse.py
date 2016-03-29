from collections import OrderedDict
from bs4 import BeautifulSoup
from bs4.element import Tag
from dictcom.models import Word, Definition

_MAIN_CONTAINER_CLASS = 'source-box'

_DEF_LIST_CLASS = 'def-list'
_DEF_SECTIONS_CLASS = 'def-pbk'
_DEF_POS_HEADER_CLASS_1 = 'dbox-pg'
_DEF_POS_HEADER_CLASS_2 = 'dbox-bold'
_DEF_SET_CLASS = 'def-set'
_DEF_CONTENT_CLASS = 'def-content'
_EXAMPLE_CLASS = 'def-inline-example'

_DEF_UNUSUAL_TYPE_CLASS = 'def-class'
_DEF_UNUSUAL_TEXT_CLASS = 'def-text'

_MAIN_HEADER_CLASS = 'main-header'
_PRONUNCIATION_CLASS = 'spellpron'
_PRONUNCIATION_SPEAKER_CLASS = 'speaker'


def parse_word_page(word, text):
    soup = BeautifulSoup(text, 'html.parser')
    main = soup.find(class_=_MAIN_CONTAINER_CLASS)
    defs = None

    try:
        defs = parse_regular_word(main)
    except Exception as e1:
        try:
            defs = parse_unusual_word(main)
        except:
            raise DictParsingException(
                'Could not parse the Dictionary.com page for {0}'.format(word),
                word) from e1

    header = main.find(class_=_MAIN_HEADER_CLASS)
    pronunciation = get_pronunciation(header)
    pronunciation_url = get_pronunciation_url(header)

    return Word(word, defs, pronunciation, pronunciation_url)


def parse_regular_word(main_container):
    def_list = main_container.find(class_=_DEF_LIST_CLASS)
    defs = OrderedDict()

    for section in def_list.find_all(class_=_DEF_SECTIONS_CLASS):
        pos, df = parse_pos_section(section)
        defs[pos] = df

    return defs


def parse_unusual_word(main_container):
    type = main_container.find(class_=_DEF_UNUSUAL_TYPE_CLASS) \
                         .get_text().strip()
    text = main_container.find(class_=_DEF_UNUSUAL_TEXT_CLASS) \
                         .get_text().strip()

    return {
        type: [Definition(text)]
    }


def parse_pos_section(section):
    pos = get_pos(section)

    def_list = section.find_all(class_=_DEF_CONTENT_CLASS)
    defs = [parse_def(d) for d in def_list]

    return pos, defs


def get_pos(section):
    header = section.find('header')

    if header is not None:
        return header.get_text().strip()

    text = collect_until_class(section, (_DEF_SET_CLASS,))
    return text


def parse_def(defin):
    text = collect_until_class(defin.children, (_EXAMPLE_CLASS,))
    example_el = defin.find(class_=_EXAMPLE_CLASS)
    example = example_el.get_text().strip() if example_el else None
    return Definition(text, example)


def get_pronunciation(def_head):
    try:
        pronunciation = def_head.find(class_=_PRONUNCIATION_CLASS) \
                                .get_text().strip()
    except:
        return None
    return pronunciation


def get_pronunciation_url(def_head):
    try:
        p_url = def_head.find(class_=_PRONUNCIATION_SPEAKER_CLASS).get('href')
    except:
        return None
    return p_url


def collect_until_class(elems, classes):
    classes = set(classes)
    text = []
    for e in elems:
        if isinstance(e, Tag):
            el_classes = e.get('class')
            if (el_classes is not None and
                    not classes.isdisjoint(el_classes)):
                break
            else:
                text.append(e.get_text())
        else:
            text.append(str(e))
    return ''.join(text).strip()


class DictParsingException(Exception):
    def __init__(self, message, word):
        super(Exception, self).__init__(self, message)
        self.word = word
