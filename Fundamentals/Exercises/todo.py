# (-->ToDO APP)
# (*.*)(*.*)(*.*)(*.*)(*.*)(*.*)

# START PROGRAM

works_list , works_time_list = [], []
while True:

    # work input
    work = input("Enter what you want to do (ex => walking, reading,.....): ").lower()
    works_list.append(work)

    # work time input
    while True:
        work_time = input("Enter the time of to do (ex => 09 : 45): ").strip()
        if ":" not in work_time:
            print("Please enter the correct time format (e.g., 10:25)")
        else:
            break
    works_time_list.append(work_time)
    while True:
        resume = input("Do you want to continue?(yes/no) ").lower()
        if resume != "no" and resume != "yes":
            print("The answer is only yes or no")
        elif resume == "yes" or resume == "no":
            break
    if resume == "no":
        break

# show output
print(f"Works List: {works_list}\nWork List Time: {works_time_list}", end="\n\n")

# Save number of tasks and times
tasks_number = len(works_list)
tasks_time_number = len(works_time_list)

# Table display of data
print("زمان انجام کار ها", " " * 3, " کار ها", " " * 3, "شماره ردیف")
counter = 0
for i in  range(0, tasks_number):
    print("-" * 45)
    print(i + 1, " " * 12, end=" ")
    for j in range(1, 1 + 1):
        print(works_list[counter], " " * 6, end=" ")
        print(works_time_list[counter])
    counter += 1
    
# Clock code
time = []
for hour in range(0, 23 + 1):
    for minute in range(1, 59 + 1):
        # At this level of the program, I don't think we need seconds.
        # for second in range(1, 59 + 1):
        #print(f"{hour} : {minute}")
        time.append(f"{hour} : {minute}")
print(time)