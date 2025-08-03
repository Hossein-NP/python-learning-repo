# Unit conversion
# Example kg --> g
kg = int(input("Please enter kg: "))
g = kg * 1000
print(str(g) + "g")
# or
print(g, "g", sep="", end="\n\n")

# Area of a triangle
# S = 1 / 2 * HEIGHT * RULE
height = int(input("Please enter height: "))
rule = int(input("Please enter rule: "))
s = (1 / 2) * height * rule
print("s = ", s, end="\n\n")

# Calculator
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", x / y)

# Digit separator
number  = int(input("please enter number: "))
temp = number % 10  # In mathematics, the remainder of any number divided by 10 is the last digit of that number.
print(temp)
number = number // 10
temp = number % 10
print(temp)
number = number // 10
temp = number % 10
print(temp)