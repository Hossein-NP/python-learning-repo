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
print("Before swap: ","x_data: ", x_data, "y_data: ", y_data)

x_data, y_data = y_data, x_data
print("After swap:", "X_data:", x_data, "y_data:", y_data)

print("x_data + y_data ** 2: ", (x_data + y_data) ** 2)