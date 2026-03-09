from __future__ import annotations
from typing import Generic, TypeVar
from vector import Vector

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

    #fn mul_vec::<K>(&mut self, vec: Vector::<K>) -> Vector::<K>;
    def mul_vec(self, vec: Vector[K]) -> Vector[K]:
        """
        """
        rows = len(self.value)
        cols = len(self.value[0])
        
        v_rows = len(vec.value)

        if cols != v_rows:
            raise ValueError("Matrix columns must equal vector rows")
        
        result = []

        for row in self.value:
            total = sum(row[i] * vec.value[i][0] for i in range(cols))
            result.append(total)

        return Vector(result)

    #fn mul_mat::<K>(&mut self, mat: Matrix::<K>) -> Matrix::<K>;
    def mul_mat(self, mat: Matrix[K])-> Matrix[K]:
        """
        Matrix * Matrix multiplication
            Am*n X Bn*p , A(m=rows,n=cols), B(n=rows, p=cols) must be An == Bn
        Compute (row of A ⋅ column of B) if columns of A == rows of B
        """
        am, an = self.shape()
        bn, bp = mat.shape()
        if an != bn:
            raise ValueError("length of cols of matrix(self) must be same as length of rows(mat)")
        mat_cols = list(zip(*mat.value)) # transpose cols to rows
        
        result = [[sum(a*b for a,b in zip(row,col)) for col in mat_cols] for row in self.value]
        return Matrix(result)

    def shape(self) -> tuple[int, int]:
        """
        Return the shape of the matrix as (rows, cols)
        """
        rows = len(self.value)
        cols = len(self.value[0])
        return (rows, cols)

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
