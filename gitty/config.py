import os
from . import files

"""
A list of configuration values for gitty that are read from environment
variables and can also be set programmatically.
"""

CACHE_DISABLE = os.environ.get('GITTY_CACHE_DISABLE', False)
PATH = os.environ.get('GITTY_PATH', '')
CACHE_DIRECTORY = os.environ.get('GITTY_CACHE_DIRECTORY', '~/.gitty')
WHITELIST = os.environ.get('GITTY_WHITELIST', '~/.gitty_whitelist')


def cache():
    return files.canonical(CACHE_DIRECTORY)


def whitelist():
    return files.canonical(WHITELIST)
