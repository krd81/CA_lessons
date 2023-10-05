import math

# depending on the shape, we need to know the width, length, radius

# functions to calculate and print the area of each shape
def calc_square(length):
    area = length ** 2
    print(f"The area of the square is: {area}")

def calc_triangle(base, height):
    area = base * height * 0.5
    print(f"The area of the triangle is: {area}")

def calc_circle(radius):
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area}")




# what shape is it?
# Once we know what shape it is, ask for the appropriate lengths and then calculate the area
shape = input("What shape is it? Type S for square, T for triangle, C for circle: ")

match shape.upper():
    case "S" :
        length = float(input("What is the length/width of the square? "))
        calc_square(length)
    case "T" :
        base = float(input("What is the length of the base of the triangle? "))
        height = float(input("What is the height of the triangle? "))
        calc_triangle(base, height)
    case "C":
        radius = float(input("What is the radius of the circle? "))
        calc_circle(radius)



