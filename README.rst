************
dictcom
************

dictcom is a simple Python package that extract dictionary info from Dictionary.com via web scraping. It can be thought of as an unofficial "API" for Dictionary.com.

************
Installation
************

dictcom is available on PyPI::

    $ pip install dictcom

Currently it only works under Python 3. Tested with Python 3.4 and 3.5.

************
Usage
************

The package itself exposes two main methods, ``get_word`` and ``get_word_pronunciation``. 

``get_word`` downloads all the data found for the word provided and packages it into a ``Word`` object::

  import dictcom
  word = dictcom.get_word('something')  # an instance of dictcom.models.Word

You can access the word's pronunciation (the textual representation of it) via the ``pronunciation`` property::

  word.pronunciation # '[suhm-thing]'

The definitions are found under the ``defs`` property, as a dictionary. Each key of the dictionary represents one definition subsection, which usually means a different part of speech (for example noun or pronoun)::

  word.defs.keys() # ['pronoun', 'noun', 'adverb']
  
The value under each key is a list of ``Definition`` instances. Each definition has two properties, ``text`` and ``example``.

One can also download the audio file for the word's pronunciation::

  pronun = word.get_pronunciation_audio() # an instance of dictcom.models.WordPronunciation
  pronun.audio # raw audio buffer
  pronun.content_type # the MIME type of the buffer data
  
You can also immediately get the pronunciation audio with ``get_word_pronunciation``, the other method exposed by the package.
