import pytest
from game import winner

def test_winner():
    assert winner('rock', 'scissors', 0, 0) == (1, 0)

def test_winner2():
   assert winner('paper', 'scissors', 0, 0) == (1, 0)

def test_winner3():
    assert winner('paper', 'rock', 2, 5) == (2, 5)