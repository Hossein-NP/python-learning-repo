# Conditional Statement
print("*" *30, "Conditional Statement Exercise:", "*" *30, end="\n\n")

# Exercise 1
"""
  positive, negative or zero
"""
print("*" *30, "Exercise 1:", "*" *30, end="\n\n")

number = float(input("Enter a number: "))
if number < 0:
  print(f"The entered number is negative.")

elif number > 0:
  print(f"The entered number is positive.")

else:
  print(f"The entered number is zero.")

print(f"The entered number is {number}.", end="\n\n")

# Exercise 1: try/except
print("*" *30, "Exercise 1: try/except", "*" *30, end="\n\n")

try:
  number = float(input("Enter a number: "))
  if number < 0:
    print(f"The entered number is negative.")

  elif number > 0:
    print(f"The entered number is positive.")

  else:
    print(f"The entered number is zero.")

  print(f"The entered number is {number}.", end="\n\n")

except ValueError:
  print("Invalid input! Please enter a numeric value.", end="\n\n")

# Exercise 1: with while loop
print("*" *30, "Exercise 1: with while loop", "*" *30, end="\n\n")

while True:
  number = float(input("Enter a number: "))
  