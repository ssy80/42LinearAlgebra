from vector import Vector
from typing import TypeVar


K = TypeVar("K", int, float)

#fn cross_product::<K>(u: &Vector::<K>, v: &Vector::<K>) -> Vector::<K>;
def cross_product(u: Vector[K], v: Vector[K]) -> Vector[K]:
    """
    """


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
