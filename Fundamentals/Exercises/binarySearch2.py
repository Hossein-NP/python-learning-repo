import random

user = input("Please enter username:🥴  ")

# محدوده ورودی
start = int(input("Enter range start: "))
while True:
    end = int(input("Enter range end: "))
    if start > end:
        print(f"End should be bigger than {start}")
    else:
        break

# تولید عدد تصادفی
num = random.randint(start, end)
print(f"\nGuess the number!\nRange --> {start} - {end}")

counter = 0
while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess < start or guess > end:
        print("What the hell 😡\nOut of range!")
        continue

    if guess == num:
        counter += 1
        print("🎉 You won!")
        print(f"{user}, Mashallah!\nYour record --> {counter} tries")
        break
    elif guess < num:
        counter += 1
        print("Wrong guess, Brooo...\nGuess higher ⬆️")
    else:
        counter += 1
        print("Wrong guess, brooo...\nGuess lower ⬇️")



