from vector import Vector
from typing import TypeVar


K = TypeVar("K", int, float)


#fn angle_cos::<K>(u: &Vector::<K>, v: &Vector::<K>) -> f32;
def angle_cos(u: Vector[K], v: Vector[K]) -> float:
    """
    Compute cos(u, v), the cosine of the angle between the two vectors u and v
    """

def main():
    """main"""

    try:

        u = Vector([1., 0.])
        v = Vector([1., 0.])
        print(angle_cos(u, v)) # 1.0

        u = Vector([1., 0.])
        v = Vector([0., 1.])
        print(angle_cos(u, v)) # 0.0

        u = Vector([-1., 1.])
        v = Vector([ 1., -1.])
        print(angle_cos(u, v)) # -1.0

        u = Vector([2., 1.])
        v = Vector([4., 2.])
        print(angle_cos(u, v)) # 1.0

        u = Vector([1., 2., 3.])
        v = Vector([4., 5., 6.])
        print(angle_cos(u, v)) # 0.974631846

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
