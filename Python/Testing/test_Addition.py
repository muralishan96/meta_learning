import Addition
import pytest

def test_add():
    assert Addition.add(4,5) == 9

def test_sub():
    assert Addition.sub(4,5) == -1
def test_sub1():
    assert Addition.sub(4,5) == -2