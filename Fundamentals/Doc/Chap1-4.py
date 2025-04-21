# Mft Python course

# ===> Master Pasha Nasir

# ===> chapter 1 - 4

# ===> Python Basics

print("============================================")
print(".........===Print Function===.........")
# Print Function
"""
  The print() function in Python is used to display output to the console.
  It takes one or more arguments and prints them as a string.
  By default, it adds a newline character at the end of the output,
  so each print() call appears on a new line.

"""
# 1-Basic usage:
print("Hello world")

# 2-Multiple Arguments: "," is used to separate multiple arguments in the print() function.
print("Hello", "world", "from", "Python" , 313)

# 3-Custom Separator: The 'sep' parameter allows you to specify a custom separator between the arguments.
print("Hello", "world", "from", "Python", sep="-")  # Output: Hello-world-from-Python
print("Hello", "world", "from", "Python", sep=" ")  # Output: Hello world from Python
print("Hello", "world", "from", "Python", sep="*")  # Output: Hello*world*from*Python
print("Hello", "world", "from", "Python", sep="")  # Output: HelloworldfromPython

# 4-Custom End Character: The 'end' parameter allows you to specify a custom end character instead of the default newline.
print("Hello", end=" ")  # Output: Hello (no newline)
print("world")  # Output: world (on the same line)
print("Hello", end="*")  # Output: Hello* (no newline)
print("world")  # Output: world (on the same line)

print("============================================")
print(".........===Data Types===.........")
# Data Types:
"""
  Python has several built-in data types, including:
  - int: Integer numbers (e.g., 5, -10)
  - float: Floating-point numbers (e.g., 3.14, -2.5)
  - str: Strings (e.g., "Hello", "Python")
  - bool: Boolean values (True or False)
"""
# 1-Integer: Whole numbers, positive or negative.
print(".........Integer.........")
print(5)  # Output: 5
print(-10)  # Output: -10

print(".........Float.........")
# 2-Floating-point: Numbers with decimal points.
print(3.14)  # Output: 3.14
print(-3.14)  # Output: -3.14

print(".........String.........")
# 3-String: Text enclosed in quotes (single or double).
print("Hello")  # Output: Hello
print('Python')  # Output: Python
print("Hello, world!")  # Output: Hello, world!
print('Python is fun!')  # Output: Python is fun!
print("123")  # Output: 123 (string, not an integer)
print("jnkjnfbkdj734y8374y#*@*#)@#)()@(#(@)#((&^$&#&^&#^&@#^@#)#(747567)))")

print(".........Boolean.........")
# 4-Boolean: Represents True or False values.
print(True)  # Output: True
print(False)  # Output: False
# print(true) # Output: NameError: name 'true' is not defined (case-sensitive)
print(True + True)  # Output: 2 (True is treated as 1)
print(True + False)  # Output: 1 (True is treated as 1 and False as 0)
print(False + False)  # Output: 0 (both are treated as 0)
print(True * True)  # Output: 1 (True is treated as 1)
print(True * False)  # Output: 0 (True is treated as 1 and False as 0)
print(False * False)  # Output: 0 (both are treated as 0)
print(5 > 2) # Output: True (5 is greater than 2)
print(5 < 2) # Output: False (5 is not less than 2)
print(5 == 5) # Output: True (5 is equal to 5)
print(5 != 5) # Output: False (5 is not equal to 5)
print(5 >= 2) # Output: True (5 is greater than or equal to 2)
print(5 <= 2) # Output: False (5 is not less than or equal to 2)
print(5 > 2 and 3 < 5) # Output: True (both conditions are true)
print(5 > 2 or 3 > 5) # Output: True (at least one condition is true)
print(not True) # Output: False (not operator negates the value)
print(not False) # Output: True (not operator negates the value)

print("============================================")
print(".........===Variables===.........")



