from __future__ import annotations
from typing import Generic, TypeVar
from vector import Vector

K = TypeVar("K", int, float)


class Matrix(Generic[K]):
    EPS = 1e-12

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

    def mul_mat(self, mat: "Matrix[K]")-> "Matrix[K]":
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

    def trace(self)-> K:
        """
        The trace of a square matrix is the sum of the elements on the main diagonal
        Only defined for square matrices
        """
        self.is_square_matrix()
        rows, _ = self.shape()
        mat = self.value
        return sum(mat[i][i] for i in range(rows))

    def transpose(self) -> "Matrix[K]":
        """
        Rows become columns, columns become row
        """
        mat_t = [list(t) for t in zip(*self.value)]

        return Matrix(mat_t)

    def row_echelon(self)-> "Matrix[K]":
        """
        Reduced Row echelon form
        RREF (Gauss-Jordan)
        """
        mat = [[float(x) for x in row] for row in self.value]
        mat, _ = self._gauss_jordan_elimination(mat)
        return Matrix(mat)

    def _gauss_jordan_elimination(
        self,
        left: list[list[float]],
        right: list[list[float]] | None = None,
        require_full_pivot: bool = False,
    ) -> tuple[list[list[float]], list[list[float]] | None]:
        """
        Gauss-Jordan elimination on left matrix (and optional right matrix).
        left is use for RREF
        right is use for Inverse (Identity matrix)
        require_full_pivot - inverse check, no row can be without a pivot
        """
        rows = len(left)
        cols = len(left[0])
        pivot_row = 0

        for col in range(cols):
            if pivot_row >= rows:
                break
            
            # Partial pivoting: pick the row with the col having largest absolute value.
            best_row = max(range(pivot_row, rows), key=lambda r: abs(left[r][col])) # pass r from range(), max() find largest col value using key, get row with largest col value 
            
            if abs(left[best_row][col]) < self.EPS:     # best row (pivot) col is 0, 
                if require_full_pivot:                  # cannot get inverse
                    raise ValueError("matrix is singular and has no inverse")
                continue

            if best_row != pivot_row:                     # swap pivot row with best row, best_row becomes pivot_row
                left[pivot_row], left[best_row] = left[best_row], left[pivot_row]
                if right is not None:
                    right[pivot_row], right[best_row] = right[best_row], right[pivot_row]

            pivot = left[pivot_row][col]

            left[pivot_row] = [x / pivot for x in left[pivot_row]]     # Normalize pivot row so each pivot is 1.0. By dividing every number with pivot
            if right is not None:
                right[pivot_row] = [x / pivot for x in right[pivot_row]]

            # Gauss-Jordan elimination: clear above and below pivot.
            for r in range(rows):
                if r == pivot_row:
                    continue
                factor = left[r][col]
                if abs(factor) < self.EPS:
                    continue
                left[r] = [a - factor * b for a, b in zip(left[r], left[pivot_row])]
                if right is not None:
                    right[r] = [a - factor * b for a, b in zip(right[r], right[pivot_row])]

            pivot_row += 1

        if require_full_pivot and pivot_row < rows:  # final pivot check, every row must have a pivot.
            raise ValueError("matrix is singular and has no inverse")

        return left, right

    def determinant(self)-> K:
        """
        Determinant is only defined for square matrices
        Reduces the matrix to an upper triangular matrix, and then computes the determinant from the product of the diagonal pivots.
        Row Reduction using Gaussian elimination.

        Computes the determinant by reducing the matrix to upper triangular form and multiplying the pivots, while accounting for row swaps.
        """
        self.is_square_matrix()
        rows, cols = self.shape()
        if rows == 0:
            return 1
        if rows == 1:
            return self.value[0][0]

        side_length = cols # rows or cols does not matter as it is a square matrix

        mat = [[float(x) for x in row] for row in self.value]
        det = 1

        for i in range(side_length): 
            pivot = max(range(i, side_length), key=lambda r: abs(mat[r][i]))  # Find the row with the largest absolute value in the pivot column
            
            if abs(mat[pivot][i]) < self.EPS:      # if any pivot is 0, the diagonal number will have 0, a * 0 = 0.
                return 0
            if pivot != i:                    # pivot row id is not same as currnt row, swap row, best row now on top mat[i].
                mat[i], mat[pivot], det = mat[pivot], mat[i], -det     # every row swap, det sign is changed by multiply by -1
            
            det *= mat[i][i]                 # no need normalise to 1
            
            for r in range(i+1, side_length):               # process each col value to 0 below pivot value
                factor = mat[r][i] / mat[i][i]              # elimination factor
                for c in range(i, side_length): 
                    mat[r][c] -= factor * mat[i][c]        

        return det

    def inverse(self) -> "Matrix[K]":
        """
        Inverse of a square matrix using Gauss-Jordan elimination.
        Gauss-Jordan elimination, which is general for all square sizes.
        [A|I]->[I|A-1]
        """
        self.is_square_matrix()
        rows, _ = self.shape()
        det = float(self.determinant())
        if abs(det) < self.EPS:
            raise ValueError("matrix is singular and has no inverse")

        a = [[float(x) for x in row] for row in self.value]
        inv = [[1.0 if r == c else 0.0 for c in range(rows)] for r in range(rows)]
        _, inv = self._gauss_jordan_elimination(a, inv, require_full_pivot=True)
        return Matrix(inv)

    def rank(self) -> int:
        """
        Rank of matrix = number of non-zero rows in RREF.
        """
        mat = [[float(x) for x in row] for row in self.value]
        mat, _ = self._gauss_jordan_elimination(mat)
        return sum(1 for row in mat if any(abs(x) >= self.EPS for x in row))

    def is_square_matrix(self)-> None:
        """
        Check shape for square matrix
        """
        rows, cols = self.shape()
        if rows != cols:
            raise ValueError("not a square matrix")

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
