# Data Types 
# Python has several built-in data types that are used to store values.
# Here are some of the most commonly used data types:

# 1. Numeric Types
# Integers
int_var = 10
# Floating Point Numbers
float_var = 10.5
# Complex Numbers
complex_var = 3 + 4j
print("Integer:", int_var," Float:", float_var, "Complex:", complex_var)
# NOTE:
# Numeric types can be used in arithmetic operations
sum_var = int_var + float_var  # 20.5

# 2. Sequence Types
# Strings
str_var = "Hello, World!"
str_var2 = 'Python is great!'
str_var3 = "123445@#$  &^%()&&*)()  "
print("String 1:", str_var, "String 2:", str_var2, "String 3:", str_var3)
# Lists
list_var = [1, 2, 3, 4, 5]
list_var2 = ["apple", "banana", "cherry"] 
list_var3 = [1, "apple", 3.14, True]
list_var4 = [1, 2, 3, [4, 5], "hello"]
print("list_var:", list_var, "list_var2:", list_var2, "list_var3:", list_var3, "list_var4:", list_var4)
# Tuples
tuple_var = (1, 2, 3, 4, 5)
tuple_var2 = ("apple", "banana", "cherry")
tuple_var3 = (1, "apple", 3.14, True) 
tuple_var4 = (1, 2, 3, (4, 5), "hello")
print("tuple_var: " + str(tuple_var), "tuple_var2: " + str(tuple_var2), "tuple_var3: " + str(tuple_var3), "tuple_var4: " + str(tuple_var4), sep="\t")

# 3. Dictionary Type
# Dictionaries
dict_var = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
dict_var2 = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
print("dict_var:", dict_var, "dict_var2:", dict_var2)

# 4. Set Types
# Sets  
set_var = {1, 2, 3, 4, 5}
set_var2 = {"apple", "banana", "cherry"}
set_var3 = {1, "apple", 3.14, True}
set_var4 = {1, 2, 3, (4, 5), "hello"}
print("set_var: " + str(set_var), "set_var2: " + str(set_var2), "set_var3: " + str(set_var3), "set_var4: " + str(set_var4), sep="\t")

# 5. Boolean Type
# Booleans
bool_var = True
bool_var2 = False
print("bool_var:", bool_var, "bool_var2:", bool_var2)
# NOTE:
# Booleans can be used in conditional statements
if bool_var:
    print("bool_var is True")
else:
    print("bool_var is False")
# NOTE:
# Booleans can also be used in logical operations
logical_and = bool_var and bool_var2  # False
logical_or = bool_var or bool_var2    # True
logical_not = not bool_var             # False
print("logical_and:", logical_and, "logical_or:", logical_or, "logical_not:", logical_not)

# 6. None Type
# None
none_var = None
print("none_var:", none_var)
# NOTE:
# None is often used to represent the absence of a value or a null value
# It can be used as a default value for function arguments
def example_function(param=None):
    if param is None:
        print("No value provided")
    else:
        print("Value provided:", param)
example_function()  # No value provided
example_function(42)  # Value provided: 42

