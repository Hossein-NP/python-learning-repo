#Exercise 2
"""
  Get the user's age and check whether or not entry is allowed.

"""
print("*" *30, "Exercise 2: Login", "*" *30)

age =  int(input("Please enter your age (e.g., 18): "))

if age >= 18:
  print("You are allowed to enter.")

else:
  print("You are not allowed to enter.")

# Exercise 3: 
"""
Write a program that takes "a character" (a single letter, number, or symbol) from the user and determines whether:
  - it is a letter (uppercase or lowercase)
  - it is a number
  - it is a symbol (not a letter or number)
  - it is not a valid character (e.g., more than one character entered)   
"""

while True:

  character = input("Please enter your character (a single letter, number, or symbol): ").strip()
  characters = []
  for i in character:
    characters.append(i)

  length = len(characters)
  print(f"Entered Character: {characters}")
  print("The number of characters: ", + length, end="\n\n")

  if length > 1:
    print("More than two character entered. Please enter a character.")
  else:
    print("The number of characters allowed.")
    break

if character.isupper():
  print("Uppercase Letter")

elif character.islower():
  print("Lowercase Letter")

elif character.isdigit():
  print("Digit")

elif character.isalpha():
  print("Alpha")

elif character.isalnum():
  print("Alpha + digit")

else:
  print("other characters")


# Exercise 3: second method

while True:
  characters = input("Please enter your character (a single letter, number, or symbol): ").strip()

  if len(characters) != 1:
    print("❌ Please enter exactly one character.\n")
  else:
    print("✅ Character accepted.\n")
    break

if character.isupper():
  print("Uppercase Letter")

elif character.islower():
  print("Lowercase Letter")

elif character.isdigit():
  print("Digit")

elif character.isalpha():
  print("Alpha")

elif character.isalnum():
  print("Alpha + digit")

else:
  print("other characters")


print("*" *30, "Exercise 4: Comparing two numbers", "*" *30)

# Exercise 4:
"""
 Take two numbers from the user and print the larger number.
"""

# METHOD 1:

number = float(input("Please enter first number(e.g.,10, 12.52, -20): "))
number_2 = float(input("Please enter second number(e.g.,10, 12.52, -20): "))

if number < number_2:
  print(f"{number} < {number_2}", end="\n\n")
elif number > number_2:
  print(f"{number} > {number_2}", end="\n\n")
elif number == number_2:
  print(f"{number} == {number_2}", end="\n\n")
else:
  print("The numbers entered are not correct.")


# METHOD 2 :
numbers = []
i = 1
while i <= 2:
    number = float(input(f"Enter number {i}: "))
    numbers.append(number)
    i += 1

if numbers[0] < numbers[1]:
  print(f"{numbers[0]} < {numbers[1]}", end="\n\n")
elif numbers[0] > numbers[1]:
  print(f"{numbers[0]} > {numbers[1]}", end="\n\n")
else:
  print(f"{numbers[0]} == {numbers[1]}", end="\n\n")
