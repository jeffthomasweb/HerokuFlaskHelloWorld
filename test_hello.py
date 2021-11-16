import pytest
from app import hello,helloroc

#Test for main site.
def test_hello():
    assert hello() == "Hello World!"

#Test for /hi enpoint.
def test_helloroc():
    assert helloroc() == "Hello RocPy 🪨🐍!"
