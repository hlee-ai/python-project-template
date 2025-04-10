"""
Python test file for example.py

This file contains a simple test case for the hello function.
"""
from example import hello


def test_hello():
    """
    Test the hello function.
    """
    assert hello("World") == "Hello, World!"
