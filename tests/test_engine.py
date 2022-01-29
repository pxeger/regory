from libgolf.string import Character

from regory.engine import Literal, Optional, Sequence


A = Literal(Character("a"))
B = Literal(Character("b"))


def test_literal():
    assert A.match("a", 0) == {1}
    assert A.match("ba", 1) == {2}
    assert A.match("b", 0) == set()
    assert A.match("ab", 0) == {1}
    assert A.match("ab", 1) == set()
    assert A.match("ab", 4) == set()
    assert A.match("ba", 0) == set()
    assert A.match("", 0) == set()


def test_optional():
    assert Optional(A).match("a", 0) == {0, 1}
    assert Optional(A).match("b", 0) == {0}


def test_sequence():
    assert Sequence(A, B).match("ab", 0) == {2}
    assert Sequence(A, B).match("abc", 0) == {2}
    assert Sequence(A, B).match("cab", 0) == set()
    assert Sequence(A, B).match("ba", 0) == set()
    assert Sequence(A, B).match("ac", 0) == set()
    assert Sequence(A, B).match("a", 0) == set()
    assert Sequence(A, B).match("b", 0) == set()
    assert Sequence(A, B).match("", 0) == set()
    assert Sequence(A, B).match("ab", 1) == set()
    assert Sequence(A, B).match("ab", 4) == set()
