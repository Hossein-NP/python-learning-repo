import fractions
# Exercise 1
"""
  Suppose you are programming a simple game. You need to store the position of an object in the game.
  This position consists of two variables x and y, which specify the horizontal and vertical dimensions of the object, respectively.
  How can you define and assign values ​​to these two variables?

"""
cordinate_x = 10
cordinate_y = 20
print("Current position:", cordinate_x, cordinate_y)
# OR
x, y = 20, 10
print("Current Position:(", x, ",", y,")")


# Exercise 2
"""
  Suppose two variables x and y are defined with values ​​5 and 10.

  a) Using an expression, swap the values ​​of these two variables.

  b) Without using auxiliary variables, raise the sum of x and y to the power of 2.

"""
x_data, y_data = 5, 10            # multiple assignment
print("Before swap: x_data:", x_data, " y_data: ", y_data)

x_data, y_data = y_data, x_data
print("After swap: X_data:", x_data, "  y_data:", y_data)

print("x_data + y_data ** 2: ", (x_data + y_data) ** 2, end="\n\n")

print("==============👇==============", end="\n\n")

# values change

x = 5
y = 6
print(f"x: {x} y: {y}")
x, y = y, x  # x = y , y = x
print(f"x: {x} y: {y}")

print("==============👇==============", end="\n\n")

# Area of the rectangle

length  = 12 # cm
width = 20 # cm
area = length * width
print(f"Area of the rectangle: {area} cm**2")

print("==============👇==============", end="\n\n")

# Celsius to Fahrenheit: (Celsius * 9/5) + 32

celsius = 55.25
fahrenheit = (celsius * 9 / 5) + 32  # (celsius * 9) / 5 + 32
print(f"fahrenheit: {fahrenheit}")

print("==============👇==============", end="\n\n")

# circle area and circumference
# circle area = pi * r**2
# pi: 3.14 r: radius
#
# circumference = 2 * pi * radius

pi = 3.14
circle_radius = 25 # cm
circle_area = pi * (circle_radius**2)
print(f"circle area: {circle_area} cm**2")
print(f"circumference: ", 2 * pi * circle_radius,"cm")

