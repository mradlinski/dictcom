from setuptools import setup

config = {
    'description': 'A pseudo-API for Dictionary.com that works by scraping its website.',
    'author': 'mromnia',
    'url': 'https://github.com/mromnia/dictcom',
    'author_email': 'mr.omnia.dev@gmail.com',
    'version': '0.0.3',
    'install_requires': [
        'requests',
        'beautifulsoup4'
    ],
    'name': 'dictcom',
    'license': 'MIT',
    'packages': ['dictcom'],
}

setup(**config)
