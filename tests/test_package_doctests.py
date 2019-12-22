import doctest
import unittest

# Paths to one's Python modules
from app import models, views


def test_doctest_suit():
    test_suit = unittest.TestSuite()
    test_suit.addTest(doctest.DocTestSuite(models))
    test_suit.addTest(doctest.DocTestSuite(views))
    # There are 3 different levels of a verbosity parameter:
    # 0 (quiet): you just get the total numbers of tests executed and the global result
    # 1 (default): you get the same plus a dot for every successful test or a F for every failure
    # 2 (verbose): you get the help string of every test and the result
    runner = unittest.TextTestRunner(verbosity=2).run(test_suit)

    assert not runner.failures
