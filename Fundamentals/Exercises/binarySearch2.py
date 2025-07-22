import random

user = input("Please enter username: ")
start = int(input("Enter range start: "))
end = None
is_range_valid = True
while is_range_valid :
    end = int(input("Enter range end: "))
    if start > end:
        print(f"End Should be bigger than {start}")
    else:
        is_range_valid = False

num  = random.randint(start, end)
print(f"Guess the number\nRange -> {start} - {end}")

guess_number = True
counter = 0
while guess_number:
    guess = int(input("Enter Your Guess: "))
    if guess not in range(start, end + 1):
        print('What the hell\nOut of range')
    elif guess == num:
        counter += 1
        print("You won")
        print(f"{user} Mashallah!\nYou Record --> {counter}")
        break
    elif guess < num:
        counter += 1
        print("Wrong guess Brooo\nGuess higher...")
    elif guess > num:
        counter += 1
        print('Wrong guess brooo\nGuess lower...')


