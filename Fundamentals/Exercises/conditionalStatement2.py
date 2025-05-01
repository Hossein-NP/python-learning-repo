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
    print("More than one character entered. Please enter a character.")
  else:
    print("The number of characters allowed.")
    break

