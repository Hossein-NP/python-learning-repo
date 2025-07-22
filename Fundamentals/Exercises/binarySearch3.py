import math
def binary_search(user, start, end):
    import random
    # تولید عدد تصادفی
    num = random.randint(start, end)
    print(f"\nGuess the number!\nRange --> {start} - {end}")
    counter = 0
    while   True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")

        if guess < start or guess > end:
            print("What the hell 😡\nOut of range!")
            continue

        if guess == num:
            counter += 1
            print("You win")
            print(f"{user}, Mashallah!\nYour record --> {counter} tries")
            break
        elif guess < num:
            counter += 1
            print("Wrong guess, Brooo...\nGuess higher ⬆️")
        elif guess > num:
            counter += 1
            print("Wrong guess, Brooo...\nGuess lower ⬇️")
    return counter

user = input("Please enter username:🥴  ")

# محدوده ورودی
start = int(input("Enter range start: "))
while True:
    end = int(input("Enter range end: "))
    if start > end:
        print(f"End should be bigger than {start}")
    else:
        break

n = (end + 1) - start
bigO = math.ceil(math.log2(n))
print(f"BigO ---> {bigO}")


# user 1
first_user = str(input("Enter a username: "))
user_1 = binary_search(first_user, start, end)

# user 2
second_user = str(input("Enter a username: "))
user_2 = binary_search(second_user, start, end)

if user_1 < user_2:
    print(f"{first_user} won!\nCongratulations!")
elif user_1 > user_2:
    print(f"{second_user} won!\nCongratulations!")
else:
    print('Draw Draw Draw!')
