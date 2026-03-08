from __future__ import annotations
from typing import Generic, TypeVar

K = TypeVar("K", int, float)


class Matrix(Generic[K]):

    def __init__(self, v: list[list[K]]) -> None:
        """
        Constructor of Matrix object
        """
        self.is_valid_matrix_value(v)
        self.value = v

    def add(self, v: "Matrix[K]") -> "Matrix[K]":
        """
        Matrix addition, add v.value to self.value
        """
        self.is_matrix(v)
        self.is_match_matrix_shape(v)
        self.value = [
            [a + b for a, b in zip(self_row, v_row)]
            for self_row, v_row in zip(self.value, v.value)
        ]
        return self

    def sub(self, v: "Matrix[K]") -> "Matrix[K]":
        """
        Matrix subtraction, subtract v.value from self.value
        """
        self.is_matrix(v)
        self.is_match_matrix_shape(v)
        self.value = [
            [a - b for a, b in zip(self_row, v_row)]
            for self_row, v_row in zip(self.value, v.value)
        ]
        return self

    def scl(self, a: K) -> "Matrix[K]":
        """
        Matrix scaling, scale self.value by a
        """
        if isinstance(a, bool) or not isinstance(a, (float, int)):
            raise TypeError("scale factor must be a float or an int")

        self.value = [[x * a for x in row] for row in self.value]
        return self

    def is_matrix(self, v: "Matrix[K]") -> None:
        """
        Check valid instance of Matrix class
        """
        if not isinstance(v, Matrix):
            raise TypeError("v must be a Matrix")

    def is_valid_matrix_value(self, v: list[list[K]]) -> None:
        """
        Check matrix is valid:
            [[K, ...], ...]
        """
        if not isinstance(v, list):
            raise TypeError("matrix must be a list")
        if len(v) == 0:
            raise ValueError("matrix cannot be empty")

        first_row_len = None
        for row in v:
            if not isinstance(row, list):
                raise TypeError("matrix rows must be lists")
            if len(row) == 0:
                raise ValueError("matrix rows cannot be empty")
            if first_row_len is None:
                first_row_len = len(row)
            elif len(row) != first_row_len:
                raise ValueError("matrix rows must have same length")

            for cell in row:
                if isinstance(cell, bool) or not isinstance(cell, (int, float)):
                    raise TypeError("matrix must only contain int or float values")

    def is_match_matrix_shape(self, v: "Matrix[K]") -> None:
        """
        Check self.value and v.value have same shape
        """
        self.is_matrix(v)
        if len(self.value) != len(v.value):
            raise ValueError("matrix row count does not match")
        if len(self.value[0]) != len(v.value[0]):
            raise ValueError("matrix column count does not match")

    def __repr__(self) -> str:
        return "\n".join(str(row) for row in self.value)
