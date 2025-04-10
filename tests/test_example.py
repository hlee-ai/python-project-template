"""
Python test file for example.py

This file contains a simple test case for the hello function and the bye function.
"""
from example import bye, hello


def test_hello():
    """
    Test the hello function.
    """
    assert hello("World") == "Hello, World!"


def test_bye():
    """
    Test the bye function.
    """
    assert bye("World") == "Goodbye, World!"
