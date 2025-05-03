# loops 
# NOTE: The range() function is one of the most commonly used tools in Python for creating a sequence of numbers.
# NOTE: print(list(range(1, 6)))
# >> [1, 2, 3, 4, 5]

# Exercise 1: Write a program that prints the numbers from 1 to 10 using a for loop.
print("*" *30, "Loops: Exercise 1: numbers: 1-10", "*" *30)

# METHOD 1:
print("method 1: ", end=" ")
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_numbers:
  print(i, end=" ")

print(end="\n")

# METHOD 2:
print("method 2: ", end=" ")
for i in range(1, 11):
  print(i, end=" ")

print(end="\n\n")

# Exercise 2: Calculate the sum of numbers from 1 to 100 with a while loop.
# NOTE: sum = n * (n + 1) / 2
# NOTE: sum = 100 * (100 + 1) / 2 = 5050
print("*" *30, "Loops: Exercise 2: sum(1-100)", "*" *30)

# METHOD 1:
print("method 1(whit while loop): ", end=" ")
i = 1
sum1 = 0
while i <= 100:
  sum1 += i
  i += 1
print(f"sum of numbers from 1 to 100: {sum1}")

# METHOD 2:
print("method 2(whit for loop): ", end=" ")
sum2 = 0 
for i in range(1, 101):
  sum2 += i
print(f"sum of numbers from 1 to 100: {sum2}")

print(end="\n\n")

# Exercise 3: Print all even numbers between 1 and 50.
print("(*,*)" *5, "Loops: Exercise 3: all even numbers between 1 and 50", "(*,*)" *5)
remain_list = []
odd_list = []
even_list = []
odd_count = 0
even_count = 0
for i in range(1, 51):
  remain = i % 2
  remain_list.append(remain)
  if i % 2 == 0:
    even_list.append(i)
  elif i % 2 == 1:
    odd_list.append(i)
print(f"Odd Numbers: {odd_list}\nEven Numbers: {even_list}")
for value in remain_list:
  if value == 1:
    odd_count += 1
  elif value == 0:
    even_count += 1
print(f"All remains: {remain_list}")
print(f"Odd Count: {odd_count}\nEven Count: {even_count}")


print(end="\n\n")

# Exercise 4: Take a number from the user and display the multiplication table of that number up to 10 with a for loop.
print("(*,*)" *5, "Loops: Exercise 4: multiplication table", "(*,*)" *5)

num = int(input("Please enter only one number.(e.g.,1, 3, 4, ...): "))
for i in range(1, 6):
  multipli = num * i
  print(f"{num} * {i}= ", num * i, end="\t")  #You can customize the column spacing with the end parameter.
  i += 5
  for j in range(1, 2):
    print(f"{num} * {i}= ", num * i)
