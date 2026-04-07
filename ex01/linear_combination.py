from __future__ import annotations
from vector import Vector
from typing import TypeVar


K = TypeVar("K", int, float)


def linear_combination(u: list[Vector[K]], coefs: list[K]) -> Vector[K]:
    """
    Sum the product of each (vector * coef) in the list
    """
    is_valid_list_of_vector(u)
    is_valid_list_of_coefs(coefs)
    is_length_match(u, coefs)

    size = len(u[0].value)
    result_vec = Vector([0.0] * size)  #init a blank vector of [[0], [0], [0]]
    
    for vec, coef in zip(u, coefs):
        uc_vec = Vector([row[0] for row in vec.value]).scl(coef)
        result_vec.add(uc_vec)
    
    return result_vec


def is_valid_list_of_coefs(coefs: list[K]) -> None:
    """
    Check if coef list is valid
    """
    if not isinstance(coefs, list):
            raise TypeError("must be a list of float or int")
    if len(coefs) == 0:
        raise TypeError("must not be empty list of coefs")
    for v in coefs:
        if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise TypeError("coefs must only contain int or float values")


def is_valid_list_of_vector(u: list[Vector[K]]) -> None:
    """
    Check list of vector is valid
    """
    if not isinstance(u, list):
        raise TypeError("must be a list of vector")
    if len(u) == 0:
        raise TypeError("must not be empty list of vector")
    for vec in u:
        if not isinstance(vec, Vector):
                raise TypeError("item in list must be a Vector")


def is_length_match(u: list[Vector[K]], coefs: list[K]) -> None:
    """
    Check length of u and coefs is same
    """
    if len(u) != len(coefs):
        raise ValueError("list of vector length and coefs does not match")
    
    
def main():
    """main"""

    try:

        e1 = Vector([1., 0., 0.])
        e2 = Vector([0., 1., 0.])
        e3 = Vector([0., 0., 1.])
        print(linear_combination([e1, e2, e3], [10., -2., 0.5])) #[10.][-2.][0.5]

        v1 = Vector([1., 2., 3.])
        v2 = Vector([0., 10., -100.])
        print(linear_combination([v1, v2], [10., -2.])) #[10.][0.][230.]

        #print(linear_combination([v1, v2], [10., -2., 1])) #error
        #print(linear_combination([v1, v2], []))            #error

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()







'''
def linear_combination(u: list[Vector[K]], coefs: list[K]) -> Vector[K]:
    """
    Sum the product of each (vector * coef) in the list
    """
    is_valid_list_of_vector(u)
    is_valid_list_of_coefs(coefs)
    is_length_match(u, coefs)

    dim = len(u[0].value)
    acc = [0.0] * dim
    
    for vec, coef in zip(u, coefs):
        for i, row in enumerate(vec.value):   # row is like [x_i]
            acc[i] = fma(float(coef), float(row[0]), acc[i])

    return Vector(acc)
'''    