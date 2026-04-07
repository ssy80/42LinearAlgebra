from vector import Vector
from typing import TypeVar


K = TypeVar("K", int, float)


def cross_product(u: Vector[K], v: Vector[K]) -> Vector[K]:
    """
    Cross product is an operation between two 3D vectors that produces another vector.
    A = (a1, a2, a3)
    B = (b1, b2, b3)
    A * B = (a2b3-a3b2, a3b1-a1b3, a1b2-a2b1)
    """
    if u.shape() != v.shape():
        raise ValueError("vectors shape does not match")
    if u.shape()[0] != 3:
        raise ValueError("cross product only for 3D vector")

    a = u.value
    b = v.value

    result  = Vector([
                (a[1][0] * b[2][0]) - (a[2][0] * b[1][0]),
                (a[2][0] * b[0][0]) - (a[0][0] * b[2][0]),
                (a[0][0] * b[1][0]) - (a[1][0] * b[0][0])
            ])
    return result


def main():
    """main"""

    try:

        u = Vector([0., 0., 1.])
        v = Vector([1., 0., 0.])
        print(cross_product(u, v))  # [0.][1.][0.]

        u = Vector([1., 2., 3.])
        v = Vector([4., 5., 6.])
        print(cross_product(u, v)) # [-3.][6.][-3.]

        u = Vector([4., 2., -3.])
        v = Vector([-2., -5., 16.])
        print(cross_product(u, v)) # [17.][-58.][-16.]
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
