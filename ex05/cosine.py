from vector import Vector
from typing import TypeVar


K = TypeVar("K", int, float)


def angle_cos(u: Vector[K], v: Vector[K]) -> float:
    """
    Compute cos(u, v), the cosine of the angle between the two vectors u and v
    cos(θ) = A.B / (||A||||B||)
    ||A|| = length of A = 2-norm - also known as magnitude

    angle
    1 -> same direction
    0 -> perpendicular
    -1 -> opposite direction
    """
    norm_u = u.norm()
    norm_v = v.norm()

    if norm_u == 0 or norm_v == 0:
        raise ValueError("angle is undefined for zero vectors")

    return u.dot(v) / (norm_u * norm_v)

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



'''
# Rounding issue
eps = 1e-12
if abs(result - 1.0) < eps:
    result = 1.0
elif abs(result + 1.0) < eps:
    result = -1.0
elif abs(result) < eps:
    result = 0.0
'''