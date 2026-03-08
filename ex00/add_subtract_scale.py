from vector import Vector
from matrix import Matrix


def main():
    """main"""

    try:

        # vector
        u = Vector([2., 3.])
        v = Vector([5., 7.])
        print(u.add(v))         #[7][10]

        u = Vector([2., 3.])
        v = Vector([5., 7.])
        print(u.sub(v))         #[-3][-4]

        u = Vector([2., 3.])
        print(u.scl(2.))        #[4.0][6.0]

        # matrix
        u = Matrix([[1., 2.], [3., 4.]])
        v = Matrix([[7., 4.], [-2., 2.]])
        print(u.add(v))        #[8.0, 6.0][1.0, 6.0]

        u = Matrix([[1., 2.], [3., 4.]])
        v = Matrix([[7., 4.], [-2., 2.]])
        print(u.sub(v))        # [-6.0, -2.0] [5.0, 2.0]

        u = Matrix([[1., 2.], [3., 4.]])
        print(u.scl(2.))       # [2.0, 4.0] [6.0, 8.0]

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
