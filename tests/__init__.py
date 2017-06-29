import logging

from src import foobar

__author__ = 'DungDM'
_logger = logging.getLogger(__name__)


def test_foobar():
    assert foobar(1, 1) == 2
