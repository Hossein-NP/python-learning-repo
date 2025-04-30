# Conditional Statement
print("*" *30, "Conditional Statement Exercise:", "*" *30, end="\n\n")

# Exercise 1
"""
  positive, negative or zero
"""
number = int(input("Enter a number: "))
if number < 0:
  print(f"The entered number is negative.")

elif number > 0:
  print(f"The entered number is positive.")

else:
  print(f"The entered number is zero.")

print(f"The entered number is {number}.")

