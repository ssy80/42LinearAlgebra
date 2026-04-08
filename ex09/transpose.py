from matrix import Matrix


def main():
    """main"""

    try:

        u = Matrix([[2., 0.],[0., 3.],[1, 5],])   # [2, 0, 1], [0, 3, 5]
        print(u.transpose())

        u = Matrix([[2., 0.],[0., 3.]])   # [2, 0], [0, 3]
        print(u.transpose())

        u = Matrix([[2., 0.]])   # [2], [0]
        print(u.transpose())

        u = Matrix([[2.], [0.]])   # [2, 0]
        print(u.transpose())

        #u = Matrix([[],[]])   # error
        #print(u.transpose())

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
