# START
# Testing the  problem
print(f'Pay attention to the results below 👇', end="\n\n")
list_1 = [1, 3, 2, 5, 4]
list_2 = ["a", "C", "b", "A", "c", "B"]
list_3 = [1, "a", "A", 2, "c", "C"]
list_1.sort()
list_2.sort()
# list_3.sort()  ERROR
print(f"{list_1}\n{list_2}\n{list_3}", end="\n\n")


# Sorting the list
my_list, numbers_data_list, strings_data_list, final_list = [], [], [], []
numbers_data, strings_data, select_data_type = 0, 0, 0

while True:
    while True:
        try:
            select_data_type = int(input("Please select your data type.1(for numbres)/2(for strings): "))
        except ValueError:
            print("Invalid input ⛔.You are allowed to choose the number 1 or 2.Try again")
        else:
            if select_data_type == 1:
                while True:
                    try:
                        numbers_data = int(input("Please enter number data: "))
                    except ValueError:
                        print("You are allowed to enter only numeric data.Try again")
                    else:
                        numbers_data_list.append(numbers_data)
                        break
            elif select_data_type == 2:
                strings_data = str(input("Please enter strings data: "))
                strings_data_list.append(strings_data)
                break
            else:
                print("Invalid input ⛔.")
    while True:
        resume = input("Do you want to continue?(y/n) ").strip().lower()
        if resume == "y":
            print("New Data")
            break
        elif resume == "n":
            break
        else:
            print("Invalid input.The answer is only yes or no")
    if resume == "n":
        break

numbers_data_list.sort()
strings_data_list.sort()
print(f"👉Numbers Data List: {numbers_data_list} \n👉Strings Data List: {strings_data_list}")
final_list = numbers_data_list.extend(strings_data_list)
print(f"👉Final Data List: {final_list}")