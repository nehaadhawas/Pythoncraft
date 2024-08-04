# Triangle Type Checker

# Get the lengths of the three sides from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input can form a triangle
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
    # Determine the type of triangle
    if side1 == side2 == side3:
        print("This is an Equilateral triangle.")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")
else:
    print("The lengths do not form a triangle.")
