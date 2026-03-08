from __future__ import annotations
from typing import Generic, TypeVar

K = TypeVar("K", int, float)


class Vector(Generic[K]):

    def __init__(self, value: list[K]) -> None:
        """
        Constructor of Vector object
        """
        self.is_valid_vector_value(value)
        self.value = self.to_column_vector(value)

    def add(self, v: "Vector[K]") -> "Vector[K]":
        """
        vector addition, add the v.value to self.value
        """
        self.is_vector(v)
        self.is_match_vector_len(v)
        self.value = [[a[0] + b[0]] for a, b in zip(self.value, v.value)]
        return self

    def sub(self, v: "Vector[K]") -> "Vector[K]":
        """
        vector subtract, subtract v.value from self.value
        """
        self.is_vector(v)
        self.is_match_vector_len(v)
        self.value = [[a[0] - b[0]] for a, b in zip(self.value, v.value)]
        return self

    def scl(self, a: K) -> "Vector[K]":
        """
        vector scaling, scale self.value by a
        """
        if isinstance(a, bool) or not isinstance(a, (float, int)):
            raise TypeError("scale factor must be a float or an int")
        
        self.value = [[row[0] * a] for row in self.value]
        return self

    def dot(self, v: "Vector[K]") -> K:
        """
        A⋅B = a1b1 + a2b2 + a3b3
        """
        self.is_vector(v)
        self.is_match_vector_len(v)
        return sum(a[0] * b[0] for a, b in zip(self.value, v.value))

    def is_vector(self, v: "Vector[K]") -> None:
        """
        Check is valid instance of Vector class
        """
        if not isinstance(v, Vector):
            raise TypeError("v must be a Vector")

    def to_column_vector(self, v: list[K]) -> list[list[K]]:
        """
        Normalize vector values into column format: [[x], [y], ...]
        """
        vec = [[a] for a in v]
        return vec

    def is_valid_vector_value(self, v: list[K]) -> None:
        """
        Check vector is valid:
            [K, ...]
        """
        if not isinstance(v, list):
            raise TypeError("vector must be a list")

        for c in v:
            if isinstance(c, bool) or not isinstance(c, (int, float)):
                raise TypeError("vector must only contain int or float values")

    def is_match_vector_len(self, v: "Vector[K]") -> None:
        """
        Check the len of self.value and v.value is of same len
        """
        self.is_vector(v)
        if len(self.value) != len(v.value):
            raise ValueError("vector len does not match")

    def __repr__(self) -> str:
        return "\n".join(str(row) for row in self.value)
