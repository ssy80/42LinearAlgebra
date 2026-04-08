from vector import Vector


'''
dot product > 0 = same direction
dot product == 0 = perpendicular
dot product < 0 = opposite direction
'''
def main():
    """main"""

    try:
        u = Vector([0., 0.])
        v = Vector([1., 1.])
        print(u.dot(v))  # 0.0

        u = Vector([1., 1.])
        v = Vector([1., 1.])
        print(u.dot(v)) # 2.0

        u = Vector([-1., 6.])
        v = Vector([3., 2.])
        print(u.dot(v)) # 9.0

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
