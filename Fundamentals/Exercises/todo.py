# (-->ToDO APP)

# (*.*)(*.*)(*.*)(*.*)(*.*)(*.*)

# START PROGRAM

works_list , works_time_list = [], []

while True:
    work = input("Enter what you want to do: ").lower()
    works_list.append(work)
    work_time = input("Enter the time of to do: ")
    works_time_list.append(work_time)

    resume = input("Do you want to continue?(yes/no) ").lower()
    if resume == "no":
        break
print(f"Works list: {works_list}\nWorks List Time: {works_time_list}", end="\n\n")