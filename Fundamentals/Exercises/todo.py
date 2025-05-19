# (-->ToDO APP)
# (*.*)(*.*)(*.*)(*.*)(*.*)(*.*)

# START PROGRAM

tasks_list , tasks_time_list, count = [], [], 1
while True:
    # task input
    task = input("Enter what you want to do (ex => walking, reading,.....): ").lower()
    if task == "":
        task = f"untitled {count}"
        count += 1
    tasks_list.append(task)
    # task hour input
    while True:
        try:
            task_hour = int(input("Enter the hour of the task: "))
        except ValueError:
            print("Invalid Input\nTry Again")
        else:
            if task_hour in range(0, 23 + 1):
                break
            else:
                print("Invalid Input\nTry Again")
    while True:
        try:
            task_minute = int(input("Enter the minute of the task: "))
        except ValueError:
            print("Invalid Input\nTry Again")
        else:
            if task_minute in range(0, 59 + 1):
                break
            else:
                print("Invalid Input\nTry Again")

    tasks_time = f"{task_hour} : {task_minute}"
    tasks_time_list.append(tasks_time)

    while True:
        resume = input("Do you want to continue?(yes/no) ").strip().lower()
        if resume == "yes":
            print("New Task")
            break
        elif resume == "no":
            break
        else:
            print("Invalid input.The answer is only yes or no")
    if resume == "no":
        break
# show output
print(f"Works List: {tasks_list}\nWork List Time: {tasks_time_list}", end="\n\n")
# Save number of tasks and times
tasks_number = len(tasks_list)
tasks_time_number = len(tasks_time_list)
# Table display of data
print("زمان انجام کار ها", " " * 3, " کار ها", " " * 3, "شماره ردیف")
counter = 0
for i in  range(0, tasks_number):
    print("-" * 45)
    print(i + 1, " " * 12, end=" ")
    for j in range(1, 1 + 1):
        print(tasks_list[counter], " " * 6, end=" ")
        print(tasks_time_list[counter])
    counter += 1
print()
# Clock code
# times_list = []
for hour in range(0, 23 + 1):
    for minute in range(0, 59 + 1):
        # At this level of the program, I don't think we need seconds.
        # for second in range(1, 59 + 1):
        time = f"{hour} : {minute}"
        # times_list.append(f"{hour} : {minute}")
        # print(time)
        if time in tasks_time_list:
            print(time)
            print("⏰", tasks_list[tasks_time_list.index(time)])
            while True:
                if time == "23 : 59":
                    check = str(input("Do you want to do your todo?(yes/no) ")).strip().lower()
                else:
                    check = str(input("Do you want to do your todo?(yes/no/snooze) ")).strip().lower()
                if check == "no":
                    print("Task skipped!")
                    break
                elif check == "yes":
                    print("Task Done")
                    break
                elif check == "snooze":
                    break
                else:
                    print("Invalid input\n Try again")
            if check == "snooze" and time != "23 : 59":
                tasks_list.append(tasks_list[tasks_time_list.index(time)])
                while True:
                    try:
                        snooze_details = int(input("Enter '1' to snooze 10 minutes\n""Enter '2' to select new time? "))
                    except ValueError:
                        print("Invalid input\n Try again")
                    else:
                        break
                if snooze_details == 1:
                    pass
                elif snooze_details == 2:
                    while True:
                        try:
                            new_task_hour = int(input("Enter the new hour of the task: "))
                        except ValueError:
                            print("Invalid Input\nTry Again")
                        else:
                            if hour <= new_task_hour <= 24:
                                if new_task_hour == hour:
                                    if minute == 59:
                                        print("You can't snooze at this moment...")
                                    else:
                                        break
                                else:
                                    break
                            else:
                                print("Invalid Input\nTry Again")
                    while True:
                        try:
                            new_task_minute = int(input("Enter new todo minute: "))
                        except ValueError:
                            print("Invalid Input\nTry Again")
                        else:
                            if hour == new_task_hour:
                                if minute < new_task_minute < 60:
                                    break
                                else:
                                    print("Invalid Input\nTry Again")
                            elif hour != new_task_hour:
                                if new_task_minute in range(0, 59 + 1):
                                    break
                                else:
                                    print("Invalid Input\nTry Again")
                            else:
                                print("Invalid Input\nTry Again")
                new_time = f"{new_task_hour} : {new_task_minute}"
                tasks_time_list.append(new_time)
            else:
                print("You can't snooze in day's last minute")