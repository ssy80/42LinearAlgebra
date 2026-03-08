from __future__ import annotations
from vector import Vector
from matrix import Matrix
from typing import TypeVar


K = TypeVar("K", int, float)
V = TypeVar("V", int, float, Vector[K], Matrix[K])


def lerp(u: V, v: V, t: float) -> V:
    """
    Linear interpolation: u + (t * (v - u))
    """
    is_valid_t(t)
    is_same_type(u, v)

    if isinstance(u, (int, float)):
        return (u + (t * (v - u)))

    if isinstance(u, Vector):
        is_match_vector_len(u, v)
        v_minus_u = Vector([row[0] for row in v.value]).sub(Vector([row[0] for row in u.value]))
        v_minus_u_t = v_minus_u.scl(t)
        result = Vector([row[0] for row in u.value]).add(v_minus_u_t)
        return result

    if isinstance(u, Matrix):
        is_match_matrix_shape(u, v)
        v_minus_u = Matrix([row[:] for row in v.value]).sub(Matrix([row[:] for row in u.value]))
        v_minus_u_t = v_minus_u.scl(t)
        result = Matrix([row[:] for row in u.value]).add(v_minus_u_t)
        return result

    raise TypeError("u and v must be int, float, Vector, or Matrix")


def is_valid_t(t: float) -> None:
    """
    Validate interpolation parameter.
    """
    if isinstance(t, bool) or not isinstance(t, (int, float)):
        raise TypeError("t must be a float or int")
    if t < 0 or t > 1:
        raise ValueError("t must satisfy 0 <= t <= 1")


def is_same_type(u: V, v: V) -> None:
    """
    u and v must be same type.
    """
    if type(u) is not type(v):
        raise TypeError("u and v must be of the same type")


def is_match_vector_len(u: Vector[K], v: Vector[K]) -> None:
    """
    Check vectors have same dimension.
    """
    if len(u.value) != len(v.value):
        raise ValueError("vector length does not match")


def is_match_matrix_shape(u: Matrix[K], v: Matrix[K]) -> None:
    """
    Check matrices have same shape.
    """
    if len(u.value) != len(v.value):
        raise ValueError("matrix row count does not match")
    if len(u.value[0]) != len(v.value[0]):
        raise ValueError("matrix column count does not match")


def main():
    """main"""

    try:
        print(lerp(0.0, 1.0, 0.0))  #0.0
        print(lerp(0.0, 1.0, 1.0))  #1.0
        print(lerp(0.0, 1.0, 0.5))  #0.5
        print(lerp(21.0, 42.0, 0.3)) #27.3
        print(lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3)) #[2.6][1.3]
        print(lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5)) #[[11., 5.5][16.5, 22.]]

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
