import random
import time

final_counter = 0

def pause():
    time.sleep(1)

def intro():
    print()
    print("You wake up in a hospital bed. Your head is foggy, and you're disoriented.")
    print("A nurse walks in, looking surprised that you're awake. She says, 'You’ve been in a coma for 30 years!'")
    print("You’re confused. Thirty years? You look at the calendar on the wall — it's the year 2054.")
    print("Everything feels wrong, but you’re alive. You have no memory of the past 30 years.")
    print("Your heart races. You can’t leave the hospital, the thought of it makes you dizzy.")
    pause()

def panic_attack():
    global final_counter
    final_counter += 1
    print("\nYou try to leave the hospital, but your body begins to tremble. You feel lightheaded...")
    print("You collapse, unable to breathe. The panic attack is overwhelming. You faint.")
    print("When you wake up, you're back in your hospital room, safe but shaken.")
    print("You can’t leave. You feel trapped inside your mind. There’s no way out.")
    pause()
    hospital_scenario()

def hospital_scenario():
    global final_counter
    final_counter += 1
    print("\nYou’re still in the hospital. Your mind races with confusion and fear.")
    print("Do you want to...")
    print("1. Explore the hospital room")
    print("2. Ask the nurse more questions")
    print("3. Try to leave the hospital")
    if final_counter > 5:
        print("4. Contemplate and think real hard.")
    
    choice = input("Choose an option (1, 2, or 3): ")
    if choice == "1":
        explore_room()
    elif choice == "2":
        ask_nurse()
    elif choice == "3":
        panic_attack()
    elif choice == "4" and final_counter > 5:
        final_choice()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        hospital_scenario()

def explore_room():
    global final_counter
    final_counter += 1
    print("\nYou start looking around your hospital room. There’s a calendar on the wall, a window with a view of the city, and a chair in the corner.")
    print("Suddenly, you notice a device on your wrist. It looks like some kind of high-tech health tracker.")
    print("You start to feel more confused as you wonder how this device works. Maybe it’s connected to your coma?")
    print("Do you want to...")
    print("1. Try to figure out how the device works")
    print("2. Look out the window at the city")
    print("3. Call the nurse for help")
    
    choice = input("Choose an option (1, 2, or 3): ")
    if choice == "1":
        figure_out_device()
    elif choice == "2":
        look_out_window()
    elif choice == "3":
        ask_nurse()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        explore_room()

def figure_out_device():
    global final_counter
    final_counter += 1
    print("\nYou examine the device closely. There’s a screen that displays your vitals: heart rate, blood pressure, and some unfamiliar data.")
    print("A message appears on the screen: 'Welcome back, Patient #2043. Medical analysis shows significant neural regeneration.'")
    print("You have no idea what this means, but it sounds important. You're more confused than ever.")
    print("Do you want to...")
    print("1. Try to turn off the device")
    print("2. Ask the nurse about the device")
    print("3. Ignore it and try to relax")

    choice = input("Choose an option (1, 2, or 3): ")
    if choice == "1":
        print("\nYou attempt to turn off the device, but it doesn’t respond. Something’s not right...")
        hospital_scenario()
    elif choice == "2":
        ask_nurse()
    elif choice == "3":
        print("\nYou decide to ignore the device for now and try to relax. But your mind races with questions.")
        hospital_scenario()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        figure_out_device()

def look_out_window():
    global final_counter
    final_counter += 1
    print("\nYou walk over to the window. The city looks different, with flying cars and buildings much taller than you remember.")
    print("It’s a world you don't recognize. How could it have changed so much in 30 years?")
    print("You feel a wave of dread wash over you. The world outside feels too overwhelming.")
    print("Do you want to...")
    print("1. Try to go outside and see the world")
    print("2. Go back to your bed and call the nurse")
    
    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        panic_attack()
    elif choice == "2":
        ask_nurse()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        look_out_window()

def ask_nurse():
    global final_counter
    final_counter += 1
    print("\nYou call the nurse into your room.")
    print("'What happened to me?' you ask. 'Where have I been?'")
    print("The nurse hesitates before speaking, 'You’ve been in a coma for 30 years. You were in a car accident, but you're stable now.'")
    print("You have so many questions, but you're still too weak to comprehend everything.")
    print("Do you want to...")
    print("1. Ask more questions about the accident")
    print("2. Try to leave the hospital again")
    print("3. Rest and process what you've heard")
    
    choice = input("Choose an option (1, 2, or 3): ")
    if choice == "1":
        print("\nYou ask the nurse about the accident, but she doesn't know many details. She says someone will visit you soon to explain more.")
        hospital_scenario()
    elif choice == "2":
        panic_attack()
    elif choice == "3":
        print("\nYou decide to rest and think about everything that’s happened so far.")
        hospital_scenario()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        ask_nurse()

def final_choice():
    print("\nAfter days of contemplation and conversation with the nurse, you start to feel a sense of peace.")
    print("You realize that while the future is scary, you're still alive. You have a second chance.")
    print("Do you want to...")
    print("1. Accept that you can never leave the hospital, but find a purpose within it.")
    print("2. Keep fighting, even though you can never leave, trying to find answers.")
    
    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        print("\nYou choose to find a purpose in your new life within the hospital. You help others, you study this new world, and find peace.")
        print("You realize that even though you can't leave, you still have a future.")
        print("ENDING: Peaceful Acceptance")
    elif choice == "2":
        print("\nYou keep fighting, searching for answers. But in the end, you're unable to escape your own fears.")
        print("You never leave the hospital, always trapped in your own mind.")
        print("ENDING: Forever Trapped")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        final_choice()

def start_game():
    intro()
    hospital_scenario()

start_game()
