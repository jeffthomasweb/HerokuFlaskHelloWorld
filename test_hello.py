<<<<<<< HEAD
import pytest
from app import hello,helloroc

#Test for main site.
def test_hello():
    assert hello() == "Hello World!"

#Test for /hi enpoint.
=======
#Test for app using pytest

import pytest
from app import hello,helloroc #import hello() and helloroc() functions from file app.py

#Test for main site, route "/"
def test_hello():
    assert hello() == "Hello World!"

#Test for route "/hi"
>>>>>>> 2b95d937bc9beb38cb4c8fa35db97269c31c815f
def test_helloroc():
    assert helloroc() == "Hello RocPy 🪨🐍!"
