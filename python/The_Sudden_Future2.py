import os

print(
    """
-------------------------------------------------------------------------------------------------------------------------------
                                                THE SUDDEN FUTURE!
    """
)


def fall_asleep_again():
    print(
        "\nYou wake up in the storage room again. There are shelves and boxes full of hospital supplies, and you have eaten several spiders spleeping on the floor"
    )
    print("\nDo you:")
    print("1. Fall asleep on the floor?")
    print("2. Exit the storage room?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        fall_asleep()

    if choose == "2":
        os.system("cls")
        up_stairs()

    else:
        os.system("cls")
        fall_asleep_again()


def fall_asleep():
    print(
        "\nYou wake up in the storage room. There are shelves and boxes full of hospital supplies."
    )
    print("\n1. Fall asleep on the floor.")

    choose = input("")
    if choose == "1":
        os.system("cls")
        fall_asleep_again()

    else:
        os.system("cls")
        fall_asleep()


def door1():
    print(
        "\nDoor one turns out to be the storage room. There are shelves and boxes full of hospital suplies."
    )
    print("\nDo you:")
    print("1. Go back?")
    print("2. Fall asleep on the floor?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        up_stairs()

    if choose == "2":
        os.system("cls")
        fall_asleep()

    else:
        os.system("cls")
        door1()


def poke_man2():
    print("\nYou poke him again and nothing happens again.")
    print("\n1. Slap him in the face.")

    choose = input("")
    if choose == "1":
        os.system("cls")
        slap_man()

    else:
        os.system("cls")
        poke_man2()


def slap_man():
    print(
        "\nYou slap him hard in the face. Nothing happens. You get angry and flip the hospital bed and the tubes get pulled out of his face and stomach. The woman wakes up and screams. Short story short, the man dies, and you die of capital punishment after you get wrecked in court because the hospital had cameras in the room."
    )
    print("\n1. Play again?")
    print("2. Or no?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        start()

    if choose == "2":
        os.system("cls")
        game_over()

    else:
        os.system("cls")
        slap_man()


def poke_man():
    print("\nYou poke the man in the face and nothing happens.")
    print("\nDo you:")
    print("1. Poke him again?")
    print("2. Slap him in the face?")
    print("3. Check the womans phone?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        poke_man2()

    if choose == "2":
        os.system("cls")
        slap_man()

    if choose == "3":
        os.system("cls")
        check_phone()

    else:
        os.system("cls")
        poke_man()


def check_news():
    print(
        "\nYou find all the populat news channels and read them all. USA and Russia had started WW111 and The US had nuked the crap out of Russia. Flying cars were coming out in 3 weeks, and the first lesbian president was sworn into office 2 days ago."
    )
    print("\nDo you:")
    print("1. Kys?")
    print("2. Put the phone down?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        kys()

    if choose == "2":
        os.system("cls")
        door2()

    else:
        os.system("cls")
        check_news()


def check_phone():
    print(
        "\nYou walk over and pick up the phone. The phone screen turns on as you pick it up. You see the date on the phone is 1/23/2O67. The phone background looks like the man laying on the hospital bed before he got tubes in his eyes, mouth, and stomach."
    )
    print("\n1. Check the news?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        check_news()

    else:
        os.system("cls")
        check_phone()


def door2():
    print(
        "\nThere is a man on a hospital bed asleep with tubes going into his eyes mouth and several coming out of his stomach. The tubes are connected to several devices on the left side of the bed. On the right side of the bed a woman has fallen asleep in a chair and a phone is on the ground near the chair."
    )
    print("\nDo you:")
    print("1. Check if her phone is locked?")
    print("2. Check to see if the man is alive?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        check_phone()

    if choose == "2":
        os.system("cls")
        poke_man()

    else:
        os.system("cls")
        door2()


def door3():
    print("\nYou find the janitorial closet with mops and brooms and cleaner fluid.")
    print("\nDo you:")
    print("1. Drink the cleaner fluid?")
    print("2. Exit the janitorial closet?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        kys()

    if choose == "2":
        os.system("cls")
        up_stairs()

    else:
        os.system("cls")
        door3()


def superpowers():
    print(
        "\nYou feel strenghth surging through your body, but its too late and the doctors start beating and stabbing you. Your body heals and they still tryin ta kill ya but it dont work. You beat the shizzle out of the frenzying docters. Theres blood everywhere and you cant stand up without slipping so you just lay there. Eventualy someone finds you and calls the police. They go over the camera footage and you get off easy with a self defense argument. You get sent back to the hospital to continue whatever treatmet they were giving you."
    )
    print("\n1. Back to your room?")
    print("2. Kys?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        start()

    if choose == "2":
        os.system("cls")
        kys()

    else:
        os.system("cls")
        superpowers()


def piss_off_doctors():
    print(
        "\nYou open the door and everybody pauses what they are doing and slowly their heads raise to look at you. Then, with terrifying speed, in unison they rush you with fists up and sharp surgery tools raised and pointed at you."
    )
    print("\nDo you:")
    print("1. Unlock your superpowers?")
    print("2. Die?")
    print("3. Think this game sucks?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        superpowers()

    if choose == "2":
        os.system("cls")
        start()

    if choose == "3":
        os.system("cls")
        game_over()

    else:
        os.system("cls")
        piss_off_doctors()


def say_hi():
    print(
        '\nThe doctors not doing anything important look at you, the surgeon gets distracted and says to one of the doctors "did you forget to lock the door again mike?" and mike says "yes....ill get it." mike walks over and says "get the f$#& away!" He then slams the door in your face.'
    )
    print("\nDo you:")
    print("1. Keep bugging the doctors?")
    print("2. Check the other doors on the floor?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        piss_off_doctors()

    if choose == "2":
        os.system("cls")
        up_stairs()

    else:
        os.system("cls")
        say_hi()


def door4():
    print(
        "\nIn door 4 you find several docters around a patient performing surgery, and a couple of aids at computers and holding trays of tools."
    )
    print("\nDo you:")
    print("1. Say Hi?")
    print("2. Close the door?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        say_hi()

    if choose == "2":
        os.system("cls")
        up_stairs()

    else:
        os.system("cls")
        door4()


def up_stairs():
    print(
        "\nAs you walk up the stairs you pass several people that give you weird looks. You continue to walk up the stairs and at the top there is noticibly less people walking around. You and on the top floor and there are several doors on this hall."
    )
    print("\nDo you:")
    print("1. Go in door 1?")
    print("2. Go in door 2?")
    print("3. Go in door 3?")
    print("4. Go in door 4?")
    print("5. Go back down the stairs?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        door1()

    if choose == "2":
        os.system("cls")
        door2()

    if choose == "3":
        os.system("cls")
        door3()

    if choose == "4":
        os.system("cls")
        door4()

    if choose == "5":
        os.system("cls")
        down_hallway()

    else:
        os.system("cls")
        up_stairs()


def game_over():
    print("\nGame over bro, come back soon :)\n")
    gameover = True
    start()


def suicide_floor():
    print(
        "\nYou try your best to keep walking but you only make it a few steps before you are overcome with insanely strong suicidal thoughts that you curl up in a ball on the floor screaming and clawing at yourself until a docter runs over and sticks you with a sedative."
    )
    print("\nDo you:")
    print("1. Wake up?")
    print("2. Die?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        start()

    if choose == "2":
        os.system("cls")
        game_over()

    else:
        os.system("cls")
        suicide_floor()


def lower_floor():
    print(
        "\nYou walk down to the lower floor and feel a really annoying suicidal vibe from this floor."
    )
    print("\nDo you:")
    print("1. Continue walking?")
    print("2. Go back up the stairs?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        suicide_floor()

    if choose == "2":
        os.system("cls")
        exit_room()

    else:
        os.system("cls")
        lower_floor()


def sit_stare():
    print(
        "\nYou sat and stared at the wall until your doctor found you. He escorted you back to your hospital room."
    )
    print("\n1. Go back to your room.")

    choose = input("")
    if choose == "1":
        os.system("cls")
        start()

    else:
        os.system("cls")
        sit_stare()


def look_dumb():
    print(
        "\nYou try to go through to doors ar the same time that were 5 feet apart, how dumb are you? The people walking past give you weird looks and start walking faster."
    )
    print("\n1. Look down the hallway?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        down_hallway()

    else:
        os.system("cls")
        look_dumb()


def down_hallway():
    print(
        "\nYou walk down the hallway and walk past several doors and end up at some stairs."
    )
    print("\nDo you:")
    print("1. Go down the stairs?")
    print("2. Go up the stairs?")
    print("3. Sit on the stairs and think about life?")
    print("4. Try to go through two doors at once?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        lower_floor()

    if choose == "2":
        os.system("cls")
        up_stairs()

    if choose == "3":
        os.system("cls")
        sit_stare()

    if choose == "4":
        os.system("cls")
        look_dumb()

    else:
        os.system("cls")
        down_hallway()


def exit_room():
    print(
        "\nYou enter a well lit hospital hallway with nurses, doctors walking left and right. You see a stair way to the right and a long hallway to the left."
    )
    print("\nDo you:")
    print("1. Go down the hallway?")
    print("2. Walk up the stairs?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        down_hallway()

    if choose == "2":
        os.system("cls")
        up_stairs()

    else:
        os.system("cls")
        exit_room()


def examine_math():
    print("\nYou look at the mathy stuff and realize you suck at math.")
    print("\n1. Exit the room?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        exit()

    else:
        os.system("cls")
        examine_math()


def kys():
    print("\nthou hast killed thy self, dost thou be ashamed of thy self?")
    print("\n1. No.")
    print("2. Yes.")

    choose = input("")
    if choose == "1" or choose == "2":
        os.system("cls")
        start()

    else:
        os.system("cls")
        kys()


def sit_up():
    print(
        "\nYou see a door in the corner of the room and computer moniters with mathy stuff you dont understand."
    )
    print("\nDo you:")
    print("1. Exit the room?")
    print("2. Try to understand the moniters?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        exit_room()

    elif choose == "2":
        os.system("cls")
        examine_math()

    else:
        os.system("cls")
        sit_up()


def back_2_sleep():
    print(
        "\nYou dream about fairy tales and dragons and centaurs and satyrs and faries and magik and hot ladies and tall buildings and about rainbow toilets and about standing in the rain holding hands with a really tall obese lady wearing a heavy winter coat."
    )
    print("\nDo you:")
    print("1. Wake up?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        start()

    else:
        os.system("cls")
        back_2_sleep()


def search_4_weapons():
    print(
        "\nYou get up and look for sharp objects. You find scalpels bone chisels and drills, forceps, assorted knives, and some complicated looking devices."
    )
    print("\nDo you:")
    print("1. Stab yourself with all of them?")

    choose = input("")
    if choose == "1":
        os.system("cls")
        kys()

    else:
        os.system("cls")
        search_4_weapons()


def start():
    global gameover
    if gameover == True:
        print("")

    else:
        print(
            "\nYou wake up in a hospital with half a beard on the left side of your face, and half a thick mustache on the right side of your face. There is no one in the room with you, and you have no memory of your past life."
        )
        print("\nDo you:")
        print("1. Sit up and observe your suroundings?")
        print("2. Go back to sleep?")
        print("3. Find something to kill yourself with?")

        choose = input("")
        if choose == "1":
            os.system("cls")
            sit_up()

        elif choose == "2":
            os.system("cls")
            back_2_sleep()

        elif choose == "3":
            os.system("cls")
            search_4_weapons()

        else:
            os.system("cls")
            start()


gameover = False
start()
