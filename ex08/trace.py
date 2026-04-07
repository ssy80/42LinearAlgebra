from matrix import Matrix


def main():
    """main"""

    try:

        u = Matrix([[1., 0.],[0., 1.],])
        print(u.trace()) # 2.0

        u = Matrix([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.],])
        print(u.trace()) # 9.0

        u = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.],])
        print(u.trace()) # -21.0
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
