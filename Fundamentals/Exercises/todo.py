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
    resume = input("Do you want to continue?(yes/no) ").lower()
    if resume == "no":
        print()
        break
# show output
print(f"Works List: {works_list}\nWork List Time: {works_time_list}", end="\n\n")
# Save number of tasks and times
tasks_number = len(works_list)
tasks_time_number = len(works_time_list)
# Table display of data
print(" " * 3, "زمان انجام کار ها", " " * 3, "لیست کار ها", " " * 3, "شماره ردیف")
for row in  range(1, tasks_number + 1):
    
