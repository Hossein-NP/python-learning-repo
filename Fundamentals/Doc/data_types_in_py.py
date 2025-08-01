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


