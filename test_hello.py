#Test for app using pytest

import pytest
from app import hello,helloroc #import hello() and helloroc() functions from file app.py

#Test for main site, route "/"
def test_hello():
    assert hello() == "Hello World!"

#Test for route "/hi"
def test_helloroc():
    assert helloroc() == "Hello RocPy 🪨🐍!"
