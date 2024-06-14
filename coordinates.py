# Points Coordinates on XY Plane
x = float(input("Enter The Points of X Axis- "))
y = float(input("Enter The Points of Y Axis- "))
p = (x, y)
match p:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Point is on Y Axis Y={y}")
    case (x, 0):
        print(f"Point is on X Axis X={x}")
    case (x, y):
        print(f"Point is on Plain X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
