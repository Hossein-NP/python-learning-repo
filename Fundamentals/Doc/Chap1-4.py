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

# Variables:
"""
  Variables are used to store data in Python.
  You can assign a value to a variable using the '=' operator.
  Variable names must start with a letter or underscore and can contain letters, numbers, and underscores.
  Variable names are case-sensitive.

"""
# 1-Variable Assignment:
x = 5  # Assigning an integer value to variable x
y = 3.14  # Assigning a float value to variable y
name = "John"  # Assigning a string value to variable name
bool_var = True  # Assigning a boolean value to variable bool_var
print("x:", x, "y:", y, "name:", name, "bool-var:", bool_var)  # Output: x: 5 y: 3.14 name: John bool-var: True
x = x + 1  # Incrementing the value of x by 1
print("Updated x:", x)  # Output: Updated x: 6

# 2-Variable Naming Rules:
"""
  - Must start with a letter (a-z, A-Z) or an underscore (_)
  - Can contain letters, numbers (0-9), and underscores
  - Cannot start with a number
  - Case-sensitive (e.g., myVar and myvar are different variables)
  - Cannot use reserved keywords (e.g., if, else, while, etc.)
  - snake_case is a common naming convention for variables in Python.
  - Use descriptive names to make your code more readable.
"""
# Valid variable names:
my_var = 10
myVar = 20
_myVar = 30
myvar1 = 40
myVar1 = 50
print( my_var, myVar, _myVar, myvar1, myVar1, sep="==")  # Output: 20 10 30 40 50


# Invalid variable names:
# 1myVar = 10  # Invalid: Cannot start with a number
# my-var = 20  # Invalid: Hyphen is not allowed in variable names
# my var = 30  # Invalid: Space is not allowed in variable names
# my@var = 40  # Invalid: Special characters are not allowed in variable names
# my var! = 50  # Invalid: Special characters are not allowed in variable names
# myvar$ = 60  # Invalid: Special characters are not allowed in variable names
# myvar% = 70  # Invalid: Special characters are not allowed in variable names
# myvar^ = 80  # Invalid: Special characters are not allowed in variable names
# myvar& = 90  # Invalid: Special characters are not allowed in variable names
# myvar* = 100  # Invalid: Special characters are not allowed in variable names
# myvar( = 110  # Invalid: Special characters are not allowed in variable names
# myvar) = 120  # Invalid: Special characters are not allowed in variable names
# myvar{ = 130  # Invalid: Special characters are not allowed in variable names
# myvar} = 140  # Invalid: Special characters are not allowed in variable names
# myvar[ = 150  # Invalid: Special characters are not allowed in variable names
# myvar] = 160  # Invalid: Special characters are not allowed in variable names
# myvar| = 170  # Invalid: Special characters are not allowed in variable names
# myvar\ = 180  # Invalid: Special characters are not allowed in variable names
# myvar: = 190  # Invalid: Special characters are not allowed in variable names
# myvar; = 200  # Invalid: Special characters are not allowed in variable names
# myvar' = 210  # Invalid: Special characters are not allowed in variable names
# myvar" = 220  # Invalid: Special characters are not allowed in variable names
# myvar< = 230  # Invalid: Special characters are not allowed in variable names
# myvar> = 240  # Invalid: Special characters are not allowed in variable names
# myvar, = 250  # Invalid: Special characters are not allowed in variable names
# myvar. = 260  # Invalid: Special characters are not allowed in variable names
# myvar/ = 270  # Invalid: Special characters are not allowed in variable names
# myvar? = 280  # Invalid: Special characters are not allowed in variable names
# myvar~ = 290  # Invalid: Special characters are not allowed in variable names
# myvar` = 300  # Invalid: Special characters are not allowed in variable names
# myvar! = 310  # Invalid: Special characters are not allowed in variable names
# myvar# = 320  # Invalid: Special characters are not allowed in variable names

print("============================================")
print(".........===Operators===.........")
# Operators:
"""
  Python supports various operators for performing operations on variables and values.
  Some common operators include:
  - Arithmetic Operators: +, -, *, /, //, %, ** (addition, subtraction, multiplication, division, floor division, modulus, exponentiation)
  - Comparison Operators: ==, !=, >, <, >=, <= (equal to, not equal to, greater than, less than, greater than or equal to, less than or equal to)
  - Logical Operators: and, or, not (logical AND, logical OR, logical NOT)
  - Assignment Operators: =, +=, -=, *=, /= (assignment and compound assignment operators)
"""
# 1-Arithmetic Operators:
print(".........1-Arithmetic Operators.........")
print("Addition:", 5 + 3)  # Output: 8
print("Substraction:", 5 - 3) # Output: 2
print("Multiplication:", 5 * 3)  # Output: 15
print("Division:", 5 / 3)  # Output: 1.6666666666666667
print("Floor Division:", 5 // 3)  # Output: 1 (integer division)
print("Modulus:", 5 % 3)  # Output: 2 (remainder of division) 
print("Exponentiation:", 5 ** 3)  # Output: 125 (5 raised to the power of 3)

# 2-Comparison Operators:
print(".........2-Comparison Operators.........")
print("Equal to:", 5 == 3)  # Output: False (5 is not equal to 3)
print("Not equal to:", 5 != 3)  # Output: True (5 is not equal to 3)
print("Greater than:", 5 > 3)  # Output: True (5 is greater than 3)
print("Less than:", 5 < 3)  # Output: False (5 is not less than 3)  
print("Greater than or equal to:", 5 >= 3)  # Output: True (5 is greater than or equal to 3)
print("Less than or equal to:", 5 <= 3)  # Output: False (5 is not less than or equal to 3)

# 3-Logical Operators:
print(".........3-Logical Operators.........")
print("Logical AND:", True and False)  # Output: False (both conditions are not true)
print("Logical AND:", True and False)  # Output: False (both conditions are not true)
print("Logical AND:", True and True)  # Output: True (both conditions are true)
print("Logical AND:", False and False)  # Output: False (both conditions are not true)
print("Logical OR:", True or False)  # Output: True (at least one condition is true)
print("Logical OR:", True or True)  # Output: True (at least one condition is true)
print("Logical OR:", False or False)  # Output: False (both conditions are not true)
print("Logical OR:", False or True)  # Output: True (at least one condition is true)
print("Logical NOT:", not True)  # Output: False (not operator negates the value)
print("Logical NOT:", not False)  # Output: True (not operator negates the value)

# 4-Assignment Operators:
print(".........4-Assignment Operators.........")
my_var = 10  # Assigning value to variable
myVar2 = 20

my_var = my_var + myVar2
print("my_var:", my_var)  # Output: 30 (10 + 20)  
 # or
my_var += myVar2
print("my_var:", my_var)  # Output: 50 (30 + 20)

my_var = my_var - myVar2
print("my_var:", my_var)  # Output: 30 (50 - 20) 
 # or
my_var -= myVar2
print("my_var:", my_var)  # Output: 10 (30 - 20)

print("============================================")
print(".........===Concatenate===.........")
# Concatenate:
"""
  Concatenation is the process of joining two or more strings together.
  In Python, you can use the '+' operator to concatenate strings.
  You can also use the 'join()' method to concatenate strings in a list.

"""
# 1-Using '+' operator:
name = "Hossein"
last_name = "Noruzpur"
age = 29
province = "\"Azarbaijan\""
city = "\"Tabriz\""
bio = "Hi, my name is " + name + " " + last_name + ". I am " + str(age) + " years old. I live in " + province + " " + "province" ", " + city + "."
print(bio)  # Output: Hi, my name is Hossein Noruzpur. I am 29 years old. I live in "Azarbaijan" province, "Tabriz".

# 2-f string 
bio2 = f"Hi, my name is {name} {last_name}. I am {29} years old. I live in {province} province, {city}."
print(bio2)  # Output: Hi, my name is Hossein Noruzpur. I am 29 years old. I live in "Azarbaijan" province, "Tabriz".

print("============================================")
print(".........===Collection Data Types===.........")
# Collection Data Types:
"""
  Python has several built-in collection data types, including:
  - list: Ordered, mutable collection of items (e.g., [1, 2, 3])
  - tuple: Ordered, immutable collection of items (e.g., (1, 2, 3))
  - set: Unordered collection of unique items (e.g., {1, 2, 3})
  - dict: Unordered collection of key-value pairs (e.g., {"key": "value"})
"""
# 1-List:
"""
  A list is an ordered, mutable(changable) and  collection of items.
  Lists can contain different data types and can be modified after creation.
  Lists are defined using square brackets [] and items are separated by commas.
"""
my_list = [1, 2, 3, 4, 5]  # Creating a list of integers 
print("my_list:", my_list)  # Output: [1, 2, 3, 4, 5]
# indexing => 0, 1, 2, 3, 4,...........
# If a list contains that N member, the index is a 0 from N-1.
# For example, if a list contains 5 members, the index is 0 to 4.
print("my_list:", my_list[0])  # Output: 1 (first item)
print("my_list:", my_list[1])  # Output: 2 (second item)
print("my_list:", my_list[2])  # Output: 3 (third item)
print("my_list:", my_list[3])  # Output: 4 (fourth item)
print("my_list:", my_list[4])  # Output: 5 (fifth item)
print("my_list:", my_list[5])  # Output: IndexError: list index out of range (no sixth item)
print("my_list:", my_list[-1])  # Output: 5 (last item)
print("my_list:", my_list[-2])  # Output: 4 (second last item)
print("my_list:", my_list[-3])  # Output: 3 (third last item)
print("my_list:", my_list[-4])  # Output: 2 (fourth last item)
print("my_list:", my_list[-5])  # Output: 1 (fifth last item)

