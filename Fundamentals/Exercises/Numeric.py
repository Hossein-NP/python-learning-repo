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
print("s = ", s)
