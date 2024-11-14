import datetime

started_entry = False

# get todays date
date = datetime.datetime.now().strftime("%Y-%m-%d")

# check if there is a journal entry for today in the text file
with open("behavior_tracker.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        if date in line:
            started_entry = True

# enter the date in the text file
if started_entry == False:
    with open("behavior_tracker.txt", "a") as file:
        file.write(f"\nDate: {date}\n")
    started_entry = True

# print the tracker for "today"
with open("behavior_tracker.txt", "r") as file:
    
    lines = file.readlines()
    counter = 0
    for line in lines:
        if date in line:
            break
        counter += 1

    print()
    skipper = 1
    for line in lines:
        if skipper > counter:
            print(line.strip())
            # if "Morning prayer" in line: morning prayer = True
        skipper += 1

# ask questions and record if yes
if started_entry == True:
    with open("behavior_tracker.txt", "a") as file:
        ask = input(f"\nDid you say your morning prayer? ")
        if ask == 'y':
            file.write(f"\nMorning prayer: {ask}")

        ask = input(f"Did you read the scriptures? ")
        if ask == 'y':
            file.write(f"\nRead scriptures: {ask}")

        ask = input(f"Did you brush your teeth? ")
        if ask == 'y':
            file.write(f"\nBrush teeth: {ask}")

        ask = input(f"Did you go to the gym? ")
        if ask == 'y':
            file.write(f"\nGo Gym: {ask}")

        ask = input(f"Did you Stay Pure? ")
        if ask == 'y':
            file.write(f"\nStay Pure: {ask}")

        ask = input(f"Did you say your nightly prayer? ")
        if ask == 'y':
            file.write(f"\nNightly prayer: {ask}")
        print()
        
