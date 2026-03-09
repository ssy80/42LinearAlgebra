from matrix import Matrix
from typing import TypeVar


K = TypeVar("K", int, float)


def main():
    """main"""

    try:

        u = Matrix([[2., 0.],[0., 3.],[1, 5],])
        print(u.transpose())

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
