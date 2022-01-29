from abc import ABC, abstractmethod
from functools import reduce
from dataclasses import dataclass

from libgolf.string import Character, String


class Matcher(ABC):
    @abstractmethod
    def match(self, subject: String, index: int) -> set[int]:
        ...


@dataclass
class Literal(Matcher):
    value: Character

    def match(self, subject, index):
        if index < len(subject) and subject[index] == self.value:
            return {index + 1}
        else:
            return set()


@dataclass
class Optional(Matcher):
    matcher: Matcher

    def match(self, subject, index):
        return {index} | self.matcher.match(subject, index)


@dataclass
class Sequence(Matcher):
    a: Matcher
    b: Matcher

    @classmethod
    def multiple(cls, components: list[Matcher]):
        return reduce(cls, components)

    def match(self, subject, i):
        result = set()
        for j in self.a.match(subject, i):
            result |= self.b.match(subject, j)
        return result
