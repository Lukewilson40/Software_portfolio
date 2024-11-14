# Luke Wilson
# 1/7/24

import os
import random
import time


def damage_calc(attack, defense, level, move_power):
    damage = int((level / 50) * (attack / defense) * move_power)
    if damage < 1:
        damage = 1
    return damage


def health_stat(base_hp, level):
    max_health = int(((2 * base_hp * level) / 50) + level + 10)
    return max_health


def phys_stat(base_phys, level):
    phys = int(((2 * base_phys * level) / 100) + 5)
    return phys


def spec_stat(base_spec, level):
    spec = int(((2 * base_spec * level) / 100) + 5)
    return spec


def speed_stat(base_speed, level):
    speed = int(((2 * base_speed * level) / 100) + 5)
    return speed


def display_creature(
    player_level,
    player_type,
    player_name,
    player_current_hp,
    player_health,
    cpu_level,
    cpu_type,
    cpu_name,
    cpu_current_hp,
    cpu_health,
):
    player_current_hp = int(player_current_hp)
    cpu_current_hp = int(cpu_current_hp)

    player_type = " ".join(player_type)
    cpu_type = " ".join(cpu_type)

    print(
        f"""
---------------------------------------------------------------------------------------------------
{player_name} |Type: {player_type}| |Lvl: {player_level}| |HP: {player_current_hp}/{player_health} |
---------------------------------------------
{cpu_name} |Type: {cpu_type}| |Lvl: {cpu_level}| |HP: {cpu_current_hp}/{cpu_health} |
---------------------------------------------
"""
    )


def get_move_info(
    move_selected,
    current_health,
    max_health,
    user_phys,
    user_spec,
    user_speed,
    opponent_phys,
    opponent_spec,
    opponent_speed,
):

    # lizard/dragon moves
    if move_selected == "Burn":
        move_power = 20
        move_type = "spec"
    elif move_selected == "Flames":
        move_power = 30
        move_type = "spec"
    elif move_selected == "Incinerate":
        move_power = 60
        move_type = "spec"

    # plant/ent moves
    elif move_selected == "Acid":
        move_power = 40
        move_type = "spec"
    elif move_selected == "Intoxicate":
        move_power = 45
        move_type = "spec"

    # fish/shark moves
    elif move_selected == "Splash":
        move_power = 30
        move_type = "spec"
    elif move_selected == "Submerge":
        move_power = 40
        move_type = "spec"
    elif move_selected == "Chomp":
        move_power = 50
        move_type = "phys"

    # rocklet/golem moves
    elif move_selected == "Sandblast":
        move_power = 20
        move_type = "spec"
    elif move_selected == "Quake":
        move_power = 40
        move_type = "spec"

    # bird/eagle moves
    elif move_selected == "Gust":
        move_power = 20
        move_type = "spec"
    elif move_selected == "Whirlwind":
        move_power = 30
        move_type = "spec"
    elif move_selected == "Tornado":
        move_power = 50
        move_type = "spec"

    # cub/bears moves
    elif move_selected == "Growl":
        move_power = 30
        move_type = "spec"
    elif move_selected == "Roar":
        move_power = 40
        move_type = "spec"

    # grub/hornet moves
    elif move_selected == "Wing Buzz":
        move_power = 20
        move_type = "spec"

    elif move_selected == "Sting":
        move_power = 35
        move_type = "phys"

    elif move_selected == "Intimidate":
        move_power = 0
        move_type = "stat"

        check_stat = opponent_phys
        opponent_phys *= 0.8
        opponent_phys = int(opponent_phys)
        if opponent_phys == check_stat:
            opponent_phys -= 1

        check_stat = user_phys
        user_phys *= 1.2
        user_phys = int(user_phys)
        if user_phys == check_stat:
            user_phys += 1

    elif move_selected == "Venom Spray":
        move_power = 40
        move_type = "spec"

        check_stat = user_spec
        user_spec *= 1.2
        user_spec = int(user_spec)
        if user_spec == check_stat:
            user_spec += 1

    elif move_selected == "Adaptation":
        move_power = 0
        move_type = "stat"

        check_stat = user_speed
        user_speed *= 1.2
        user_speed = int(user_speed)
        if user_speed == check_stat:
            user_speed += 1

        if current_health < max_health:
            current_health += max_health * 0.25
            current_health = int(current_health)

        if current_health > max_health:
            current_health = max_health

    elif move_selected == "Mega Sting":
        move_power = 50
        move_type = "phys"

        check_stat = user_phys
        user_phys *= 1.15
        user_phys = int(user_phys)
        if user_phys == check_stat:
            user_phys += 1

    # physical moves
    elif move_selected == "Smack":
        move_power = 20
        move_type = "phys"
    elif move_selected == "Scratch":
        move_power = 25
        move_type = "phys"
    elif move_selected == "Headbutt":
        move_power = 30
        move_type = "phys"
    elif move_selected == "Bite":
        move_power = 35
        move_type = "phys"
    elif move_selected == "Slash":
        move_power = 40
        move_type = "phys"
    elif move_selected == "Kick":
        move_power = 50
        move_type = "phys"
    elif move_selected == "Mega Kick":
        move_power = 55
        move_type = "phys"

    # Status moves
    elif move_selected == "Concentrate":
        move_power = 0
        move_type = "Stat"

        check_stat = user_spec
        user_spec *= 1.2
        user_spec = int(user_spec)
        if user_spec == check_stat:
            user_spec += 1

    elif move_selected == "Scare":
        move_power = 0
        move_type = "Stat"

        check_stat = opponent_spec
        opponent_spec *= 0.8
        opponent_spec = int(opponent_spec)
        if opponent_spec == check_stat:
            opponent_spec -= 1

    elif move_selected == "Bruise":
        move_power = 0
        move_type = "Stat"

        check_stat = opponent_phys
        opponent_phys *= 0.8
        opponent_phys = int(opponent_phys)
        if opponent_phys == check_stat:
            opponent_phys -= 1

    elif move_selected == "Strengthen":
        move_power = 0
        move_type = "Stat"

        check_stat = user_phys
        user_phys *= 1.2
        user_phys = int(user_phys)
        if user_phys == check_stat:
            user_phys += 1

    elif move_selected == "Invigorate":
        move_power = 0
        move_type = "Stat"

        check_stat = user_speed
        user_speed *= 1.2
        user_speed = int(user_speed)
        if user_speed == check_stat:
            user_speed += 1

    elif move_selected == "Trap":
        move_power = 0
        move_type = "Stat"

        check_stat = opponent_speed
        opponent_speed *= 0.8
        opponent_speed = int(opponent_speed)
        if opponent_speed == check_stat:
            opponent_speed -= 1

    elif move_selected == "Heal":
        move_power = 0
        move_type = "Stat"

        if current_health < max_health:
            current_health += max_health * 0.3
            current_health = int(current_health)

        elif current_health > max_health:
            current_health = max_health

    # Hydras moves
    elif move_selected == "Fireball":
        move_power = 40
        move_type = "spec"
    elif move_selected == "Inferno":
        move_power = 70
        move_type = "spec"

    # Leviathons moves
    elif move_selected == "Tsunami":
        move_power = 55
        move_type = "spec"
    elif move_selected == "Hyper Impact":
        move_power = 70
        move_type = "phys"

    # monsters moves
    elif move_selected == "Power Down":
        move_power = 0
        move_type = "Stat"

        check_stat = opponent_spec
        opponent_spec *= 0.8
        opponent_spec = int(opponent_spec)
        if opponent_spec == check_stat:
            opponent_spec -= 1

        check_stat = opponent_phys
        opponent_phys *= 0.8
        opponent_phys = int(opponent_phys)
        if opponent_phys == check_stat:
            opponent_phys -= 1

    elif move_selected == "Power Up":
        move_power = 0
        move_type = "Stat"

        check_stat = user_spec
        user_spec *= 1.2
        user_spec = int(user_spec)
        if user_spec == check_stat:
            user_spec += 1

        check_stat = user_phys
        user_phys *= 1.2
        user_phys = int(user_phys)
        if user_phys == check_stat:
            user_phys += 1

    elif move_selected == "Devastate":
        move_power = 65
        move_type = "spec"
    elif move_selected == "Annihilate":
        move_power = 65
        move_type = "phys"

    return (
        move_power,
        move_type,
        current_health,
        user_phys,
        user_spec,
        user_speed,
        opponent_phys,
        opponent_spec,
        opponent_speed,
    )


def display_move_changes(move_selected, user_name, opponent_name):
    print("")
    if move_selected == "Power Down":
        print(f"{opponent_name}s Physical and Special stats were lowered.")
    if move_selected == "Power Up":
        print(f"Monsters Physical and Special stats were raised.")

    if move_selected == "Concentrate" or move_selected == "Venom Spray":
        print(f"{user_name}s Special stat was raised.")
    if move_selected == "Scare":
        print(f"{user_name}s Special stat was lowered.")

    if move_selected == "Bruise" or move_selected == "Intimidate":
        print(f"{opponent_name}s Physical stat was lowered.")
    if (
        move_selected == "Strengthen"
        or move_selected == "Mega Sting"
        or move_selected == "Intimidate"
    ):
        print(f"{user_name}s Physical stat was raised.")

    if move_selected == "Invigorate":
        print(f"{user_name}s Speed stat was raised.")
    if move_selected == "Trap":
        print(f"{opponent_name}s Speed stat was lowered.")
    if move_selected == "Heal" or move_selected == "Adaptation":
        print(f"{user_name} healed itself.")
    time.sleep(2)


type_effectiveness = {
    "fire": {
        "fire": 0.5,
        "plant": 2.0,
        "sea": 0.5,
        "stone": 0.5,
        "air": 1.0,
        "wild": 1.0,
        "bug": 2.0,
    },
    "plant": {
        "fire": 0.5,
        "plant": 0.5,
        "sea": 2.0,
        "stone": 2.0,
        "air": 0.5,
        "wild": 1.0,
        "bug": 0.5,
    },
    "sea": {
        "fire": 2.0,
        "plant": 0.5,
        "sea": 0.5,
        "stone": 2.0,
        "air": 1.0,
        "wild": 1.0,
        "bug": 1.0,
    },
    "stone": {
        "fire": 2.0,
        "plant": 1.0,
        "sea": 0.5,
        "stone": 1.0,
        "air": 2.0,
        "wild": 1.0,
        "bug": 2.0,
    },
    "air": {
        "fire": 1.0,
        "plant": 2.0,
        "sea": 1.0,
        "stone": 0.5,
        "air": 1.0,
        "wild": 1.0,
        "bug": 2.0,
    },
    "wild": {
        "fire": 1.0,
        "plant": 1.0,
        "sea": 1.0,
        "stone": 0.5,
        "air": 1.0,
        "wild": 1.0,
        "bug": 1.0,
    },
    "bug": {
        "fire": 1.0,
        "plant": 2.0,
        "sea": 1.0,
        "stone": 0.5,
        "air": 1.0,
        "wild": 2.0,
        "bug": 1.0,
    },
}


def get_type_effectiveness(user_typing, opponent_typing):
    effectiveness = 1
    for user_type in user_typing:
        for opponent_type in opponent_typing:
            effectiveness *= type_effectiveness[user_type][opponent_type]
    return effectiveness


dryad = {
    "type": ["plant"],
    "base_hp": 20,
    "base_phys": 20,
    "base_spec": 20,
    "base_speed": 10,
    "name": "Dryad",
}
ent = {
    "type": ["plant"],
    "base_hp": 40,
    "base_phys": 40,
    "base_spec": 40,
    "base_speed": 20,
    "name": "Ent",
}

fish = {
    "type": ["sea"],
    "base_hp": 10,
    "base_phys": 20,
    "base_spec": 15,
    "base_speed": 25,
    "name": "Fish",
}
shark = {
    "type": ["sea"],
    "base_hp": 20,
    "base_phys": 40,
    "base_spec": 30,
    "base_speed": 50,
    "name": "Shark",
}

lizard = {
    "type": ["fire"],
    "base_hp": 15,
    "base_phys": 15,
    "base_spec": 20,
    "base_speed": 20,
    "name": "Lizard",
}
dragon = {
    "type": ["fire"],
    "base_hp": 30,
    "base_phys": 30,
    "base_spec": 40,
    "base_speed": 40,
    "name": "Dragon",
}

bird = {
    "type": ["air"],
    "base_hp": 10,
    "base_phys": 15,
    "base_spec": 20,
    "base_speed": 25,
    "name": "Bird",
}
eagle = {
    "type": ["air"],
    "base_hp": 20,
    "base_phys": 30,
    "base_spec": 40,
    "base_speed": 50,
    "name": "Eagle",
}

rocklet = {
    "type": ["stone"],
    "base_hp": 25,
    "base_phys": 25,
    "base_spec": 10,
    "base_speed": 10,
    "name": "Rocklet",
}
golem = {
    "type": ["stone"],
    "base_hp": 50,
    "base_phys": 50,
    "base_spec": 20,
    "base_speed": 20,
    "name": "Golem",
}

cub = {
    "type": ["wild"],
    "base_hp": 15,
    "base_phys": 25,
    "base_spec": 15,
    "base_speed": 15,
    "name": "Cub",
}
bear = {
    "type": ["wild"],
    "base_hp": 30,
    "base_phys": 50,
    "base_spec": 30,
    "base_speed": 30,
    "name": "Bear",
}

grub = {
    "type": ["bug"],
    "base_hp": 25,
    "base_phys": 20,
    "base_spec": 20,
    "base_speed": 5,
    "name": "Grub",
}
hornet = {
    "type": ["bug"],
    "base_hp": 30,
    "base_phys": 45,
    "base_spec": 25,
    "base_speed": 45,
    "name": "Hornet",
}

hydra = {
    "type": ["fire", "air"],  # implement cpu typ of air
    "base_hp": 50,
    "base_phys": 45,
    "base_spec": 55,
    "base_speed": 50,
    "name": "Hydra",
}
leviathon = {
    "type": ["sea", "stone"],  # implement cpu type of stone
    "base_hp": 50,
    "base_phys": 55,
    "base_spec": 45,
    "base_speed": 50,
    "name": "Leviathon",
}
monster = {
    "type": ["wild", "Random"],  # cpu type will be random except for plant
    "base_hp": 120,
    "base_phys": 60,
    "base_spec": 60,
    "base_speed": 50,
    "name": "Monster",
}
# plant, sea, fire, air, stone, wild, bug
type_two = random.randint(1, 6)
if type_two == 1:
    monster["type"][1] = "plant"
elif type_two == 2:
    monster["type"][1] = "sea"
elif type_two == 3:
    monster["type"][1] = "fire"
elif type_two == 4:
    monster["type"][1] = "air"
elif type_two == 5:
    monster["type"][1] = "stone"
elif type_two == 6:
    monster["type"][1] = "bug"


lizard_dragon_moves = [
    "Burn",
    "",
    "Trap",
    "",
    "Smack",
    "",
    "",
    "Concentrate",
    "",
    "Flames",
    "",
    "",
    "Invigorate",
    "",
    "Slash",
    "",
    "",
    "Bruise",
    "",
    "Incinerate",
]
dryad_ent_moves = [
    "Smack",
    "",
    "Heal",
    "",
    "Bite",
    "",
    "",
    "Trap",
    "",
    "Acid",
    "",
    "",
    "Concentrate",
    "",
    "Intoxicate",
    "",
    "",
    "Invigorate",
    "",
    "Kick",
]
fish_shark_moves = [
    "Headbutt",
    "",
    "Bruise",
    "",
    "Splash",
    "",
    "",
    "Heal",
    "",
    "Bite",
    "",
    "",
    "Trap",
    "",
    "Submerge",
    "",
    "",
    "Concentrate",
    "",
    "Chomp",
]
rocklet_golem_moves = [
    "Smack",
    "",
    "Invigorate",
    "",
    "Sandblast",
    "",
    "",
    "Bruise",
    "",
    "Slash",
    "",
    "",
    "Heal",
    "",
    "Quake",
    "",
    "",
    "Trap",
    "",
    "Mega Kick",
]
bird_eagle_moves = [
    "Gust",
    "",
    "Concentrate",
    "",
    "Headbutt",
    "",
    "",
    "Invigorate",
    "",
    "Whirlwind",
    "",
    "",
    "Bruise",
    "",
    "Slash",
    "",
    "",
    "Heal",
    "",
    "Tornado",
]
cub_bear_moves = [
    "Scratch",
    "",
    "Scare",
    "",
    "Growl",
    "",
    "",
    "Strengthen",
    "",
    "Bite",
    "",
    "",
    "Trap",
    "",
    "Roar",
    "",
    "",
    "Invigorate",
    "",
    "Mega Kick",
]
grub_hornet_moves = [
    "Bite",  # 35 phys
    "",
    "Invigorate",  # speed up
    "",
    "Wing buzz",  # 20 spec
    "",
    "",
    "Bruise",  # phys down
    "",
    "Sting",  # 40 phys
    "",
    "",
    "Intimidate",  # phys up and phys down
    "",
    "Venom Spray",  # spec 40 and spec up
    "",
    "",
    "Adaptation",  # heal and speed up
    "",
    "Mega Sting",  # 60 phys and phys up
]
hydra_moves = [
    "",
    "",
    "Trap",
    "",
    "Fireball",
    "",
    "",
    "Strengthen",
    "",
    "Mega Kick",
    "",
    "",
    "Bruise",
    "",
    "Invigorate",
    "",
    "",
    "Concentrate",
    "",
    "Inferno",
]
leviathon_moves = [
    "",
    "",
    "Strengthen",
    "",
    "Slash",
    "",
    "",
    "Scare",
    "",
    "Tsunami",
    "",
    "",
    "Concentrate",
    "",
    "Heal",
    "",
    "",
    "Bruise",
    "",
    "Hyper Impact",
]
monster_moves  =  [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Power Down",
    "Devastate",
    "Power Up",
    "Annihilate",
    "",
    "",
    "",
]


def build_team():

    # creature [number, level, alive?, moves, current health]
    player_team = [
        [0, 0, True, 0, 0],
        [0, 0, True, 0, 0],
        [0, 0, True, 0, 0],
        [0, 0, True, 0, 0],
    ]
    counter = 0
    while counter < 4:
        os.system("cls")

        # get creature number
        try:
            player_selected = int(
                input(
                    """
-----------------------------
Select a creature by number:
    
1.Dyrad,    8.Ent
2.Fish,     9.Shark
3.Lizard,   10.Dragon
4.Bird,     11.Eagle
5.Rocklet,  12.Golem
6.Cub,      13.Bear
7.Grub      14.Hornet

15.Hydra,   16.Leviathon

17.Monster

"""
                )
            )
        except:
            print("\nIncorrect Response, try again.")

        # get creature level
        player_level = 0
        while player_level < 1 or player_level > 20:
            try:
                player_level = int(input("\nWhat level is the Creature?: "))
            except:
                print("\nIncorrect Response, try again.")
            if player_level < 1 or player_level > 20:
                print("Level must be 1 through 20")

        # input creature data into player team list
        if player_selected == 1:
            player_team[counter][0] = dryad
            player_team[counter][1] = player_level
            player_team[counter][3] = dryad_ent_moves

        else:
            player_team[counter][0] = player_selected
            player_team[counter][1] = player_level
        counter += 1

    return player_team


def generate_team(player_team):

    # creature [number, level, alive?, moves, current health]
    cpu_team = [
        [0, 0, True, 0, 0],
        [0, 0, True, 0, 0],
        [0, 0, True, 0, 0],
        [0, 0, True, 0, 0],
    ]
    cpu_level = 0
    counter = 0
    # cpu creature team
    for creature in player_team:

        if creature[0] == dryad or creature[0] < 8:
            cpu_selected = random.randint(1, 7)

        elif creature[0] > 7 and creature[0] < 18:
            cpu_selected = random.randint(8, 17)
        else:
            cpu_selected = 1

        cpu_team[counter][0] = cpu_selected
        cpu_team[counter][1] = cpu_level
        counter += 1

    return cpu_team


def battle(player_team, cpu_team):

    for creature in player_team:
        if creature[2] == True:
            player_selected = creature[0]
            player_level = creature[1]
            if creature[3] != 0:
                player_moves = creature[3]
            break

    for creature in cpu_team:
        if creature[2] == True:
            cpu_selected = creature[0]
            cpu_level = creature[1]
            break

    # if player_selected == 1:
    #     player_selected = dryad
    #     player_moves = dryad_ent_moves

    if player_selected == 8:
        player_selected = ent
        player_moves = dryad_ent_moves

    elif player_selected == 2:
        player_selected = fish
        player_moves = fish_shark_moves

    elif player_selected == 9:
        player_selected = shark
        player_moves = fish_shark_moves

    elif player_selected == 3:
        player_selected = lizard
        player_moves = lizard_dragon_moves

    elif player_selected == 10:
        player_selected = dragon
        player_moves = lizard_dragon_moves

    elif player_selected == 4:
        player_selected = bird
        player_moves = bird_eagle_moves

    elif player_selected == 11:
        player_selected = eagle
        player_moves = bird_eagle_moves

    elif player_selected == 5:
        player_selected = rocklet
        player_moves = rocklet_golem_moves

    elif player_selected == 12:
        player_selected = golem
        player_moves = rocklet_golem_moves

    elif player_selected == 6:
        player_selected = cub
        player_moves = cub_bear_moves

    elif player_selected == 13:
        player_selected = bear
        player_moves = cub_bear_moves

    elif player_selected == 7:
        player_selected = grub
        player_moves = grub_hornet_moves

    elif player_selected == 14:
        player_selected = hornet
        player_moves = grub_hornet_moves

    elif player_selected == 15:
        player_selected = hydra
        player_moves = hydra_moves

    elif player_selected == 16:
        player_selected = leviathon
        player_moves = leviathon_moves

    elif player_selected == 17:
        player_selected = monster
        player_moves = monster_moves

    time.sleep(1)

    # make a list that will hold the names of the moves of the player selected creature
    player_attacks = []

    # make sure that the amount of moves that a creature gets assigned depends on the level and maxes out at 4
    if player_level > 7:
        num_attacks = 4
    elif player_level < 7 and player_level > 4:
        num_attacks = 3
    elif player_level < 4 and player_level > 2:
        num_attacks = 2
    elif player_level < 3 and player_level > 0:
        num_attacks = 1

    counter = player_level
    while len(player_attacks) < num_attacks:
        if player_moves[counter - 1] != "":
            player_attacks.append(player_moves[counter - 1])
        counter -= 1

    # display attacks
    # if num_attacks == 4:
    #     print(
    #         f"\n{player_selected['name']}s moves are: {player_attacks[0]}, {player_attacks[1]}, {player_attacks[2]}, {player_attacks[3]} "
    #     )
    # elif num_attacks == 3:
    #     print(
    #         f"\n{player_selected['name']}s moves are: {player_attacks[0]}, {player_attacks[1]}, {player_attacks[2]} "
    #     )
    # elif num_attacks == 2:
    #     print(
    #         f"\n{player_selected['name']}s moves are: {player_attacks[0]}, {player_attacks[1]} "
    #     )
    # elif num_attacks == 1:
    #     print(f"\n{player_selected['name']}s moves are: {player_attacks[0]} ")
    # time.sleep(2)

    # cpu team is generated
    if cpu_selected == 1:
        cpu_selected = dryad
        cpu_moves = dryad_ent_moves
        cpu_level = random.randint(8, 11)

    elif cpu_selected == 8:
        cpu_selected = ent
        cpu_moves = dryad_ent_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 2:
        cpu_selected = fish
        cpu_moves = fish_shark_moves
        cpu_level = random.randint(7, 9)

    elif cpu_selected == 9:
        cpu_selected = shark
        cpu_moves = fish_shark_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 3:
        cpu_selected = lizard
        cpu_moves = lizard_dragon_moves
        cpu_level = random.randint(9, 14)

    elif cpu_selected == 10:
        cpu_selected = dragon
        cpu_moves = lizard_dragon_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 4:
        cpu_selected = bird
        cpu_moves = bird_eagle_moves
        cpu_level = random.randint(7, 9)

    elif cpu_selected == 11:
        cpu_selected = eagle
        cpu_moves = bird_eagle_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 5:
        cpu_selected = rocklet
        cpu_moves = rocklet_golem_moves
        cpu_level = random.randint(8, 11)

    elif cpu_selected == 12:
        cpu_selected = golem
        cpu_moves = rocklet_golem_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 6:
        cpu_selected = cub
        cpu_moves = cub_bear_moves
        cpu_level = random.randint(8, 11)

    elif cpu_selected == 13:
        cpu_selected = bear
        cpu_moves = cub_bear_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 7:
        cpu_selected = grub
        cpu_moves = grub_hornet_moves
        cpu_level = random.randint(7, 8)

    elif cpu_selected == 14:
        cpu_selected = hornet
        cpu_moves = grub_hornet_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 15:
        cpu_selected = hydra
        cpu_moves = hydra_moves
        cpu_level = random.randint(15, 20)

    elif cpu_selected == 16:
        cpu_selected = leviathon
        cpu_moves = leviathon_moves
        cpu_level = random.randint(15, 20)

    else:
        cpu_selected = monster
        cpu_moves = monster_moves
        cpu_level = 17

    # get stats from the selected creatures
    player_name = player_selected["name"]
    player_type = player_selected["type"]
    player_health = health_stat(player_selected["base_hp"], player_level)
    player_phys = phys_stat(player_selected["base_phys"], player_level)
    player_spec = spec_stat(player_selected["base_spec"], player_level)
    player_speed = speed_stat(player_selected["base_speed"], player_level)

    cpu_name = cpu_selected["name"]
    cpu_type = cpu_selected["type"]
    cpu_health = health_stat(cpu_selected["base_hp"], cpu_level)
    cpu_phys = phys_stat(cpu_selected["base_phys"], cpu_level)
    cpu_spec = spec_stat(cpu_selected["base_spec"], cpu_level)
    cpu_speed = speed_stat(cpu_selected["base_speed"], cpu_level)

    player_current_hp = int(player_health)
    cpu_current_hp = int(cpu_health)

    print(f"\nCPU chose a level {cpu_level} {cpu_name}")
    time.sleep(2)

    # make a list that will hold the names of the moves of the cpu selected creature
    cpu_attacks = []

    # make sure that the amount of moves that a creature gets assigned depends on the level and maxes out at 4
    if cpu_level > 7:
        num_attacks = 4
    elif cpu_level < 7 and cpu_level > 4:
        num_attacks = 3
    elif cpu_level < 4 and cpu_level > 2:
        num_attacks = 2
    elif cpu_level < 3 and cpu_level > 0:
        num_attacks = 1

    # fill in move set
    counter = cpu_level
    while len(cpu_attacks) < num_attacks:
        if cpu_moves[counter - 1] != "":
            cpu_attacks.append(cpu_moves[counter - 1])
        counter -= 1

    time.sleep(1)
    os.system("cls")
    move_damage = 0
    player_faster = False
    cpu_faster = False

    while (player_current_hp > 0) and (cpu_current_hp > 0):
        # Display both creatures info
        display_creature(
            player_level,
            player_type,
            player_name,
            player_current_hp,
            player_health,
            cpu_level,
            cpu_type,
            cpu_name,
            cpu_current_hp,
            cpu_health,
        )

        # player_phys = int(player_phys)
        # player_spec = int(player_spec)
        # player_speed = int(player_speed)
        # cpu_phys = int(cpu_phys)
        # cpu_spec = int(cpu_spec)
        # cpu_speed = int(cpu_speed)

        if player_speed == cpu_speed:
            speed_tie = random.randint(1, 2)
            if speed_tie == 1:
                player_faster = True
            if speed_tie == 2:
                cpu_faster = True

        elif player_speed > cpu_speed:
            player_faster = True
        elif player_speed < cpu_speed:
            cpu_faster = True

        print(
            f"{player_name}  Phys:{player_phys}  Spec:{player_spec}  Speed:{player_speed}"
        )
        print(f"{cpu_name}  Phys:{cpu_phys}  Spec:{cpu_spec}  Speed:{cpu_speed}\n")

        if player_faster == True:
            # the player selected is faster than the cpu selected--------------------------------------------------------------------

            # select a move to use
            typo = True
            while typo == True:
                print(f"{player_name}s Moves: ")
                print("|", end="")
                counter = 0
                while counter < len(player_attacks):
                    print(f" {counter + 1}.{player_attacks[counter]} | ", end="")
                    counter += 1

                move_selected = input("\nSelect a move. ")

                try:
                    if (
                        move_selected == "1"
                        or move_selected.capitalize() == player_attacks[0]
                    ):
                        move_selected = player_attacks[0]
                        typo = False

                    elif (
                        move_selected == "2"
                        or move_selected.capitalize() == player_attacks[1]
                    ):
                        move_selected = player_attacks[1]
                        typo = False

                    elif (
                        move_selected == "3"
                        or move_selected.capitalize() == player_attacks[2]
                    ):
                        move_selected = player_attacks[2]
                        typo = False

                    elif (
                        move_selected == "4"
                        or move_selected.capitalize() == player_attacks[3]
                    ):
                        move_selected = player_attacks[3]
                        typo = False

                    else:
                        print("You typed it in wrong silly\n")
                        typo = True
                except:
                    print("You typed it in wrong silly\n")

            # get the move (power and type)

            (
                move_power,
                move_type,
                player_current_hp,
                player_phys,
                player_spec,
                player_speed,
                cpu_phys,
                cpu_spec,
                cpu_speed,
            ) = get_move_info(
                move_selected,
                player_current_hp,
                player_health,
                player_phys,
                player_spec,
                player_speed,
                cpu_phys,
                cpu_spec,
                cpu_speed,
            )

            if move_type == "phys":
                move_damage = int(
                    damage_calc(player_phys, cpu_phys, player_level, move_power)
                )

            elif move_type == "spec":
                move_damage = int(
                    damage_calc(player_spec, cpu_spec, player_level, move_power)
                )

            elif move_type == "Stat":
                move_damage = 0

            # finish damage calculation with effectiveness multiplier
            effectiveness = get_type_effectiveness(player_type, cpu_type)
            move_damage *= effectiveness

            time.sleep(1)
            # display attack selected and affect of attack
            print(f"\nUsers {player_name} used {move_selected} ")
            time.sleep(1)

            if effectiveness > 1 and move_damage > 0:
                print("\nIts super effective!")
            if effectiveness < 1 and move_damage > 0:
                print("\nIts not very effective.")
            if effectiveness == 1 and move_damage > 0:
                print("\nIt was effective.")

            display_move_changes(move_selected, player_name, cpu_name)

            # re-calculate health stat after damage
            cpu_current_hp -= int(move_damage)
            if cpu_current_hp < 0:
                cpu_current_hp = 0
                break

            time.sleep(1)
            os.system("cls")

            # re-display creatures
            display_creature(
                player_level,
                player_type,
                player_name,
                player_current_hp,
                player_health,
                cpu_level,
                cpu_type,
                cpu_name,
                cpu_current_hp,
                cpu_health,
            )

            player_phys = int(player_phys)
            player_spec = int(player_spec)
            player_speed = int(player_speed)
            cpu_phys = int(cpu_phys)
            cpu_spec = int(cpu_spec)
            cpu_speed = int(cpu_speed)
            print(
                f"{player_name}  Phys:{player_phys}  Spec:{player_spec}  Speed:{player_speed}"
            )
            print(f"{cpu_name}  Phys:{cpu_phys}  Spec:{cpu_spec}  Speed:{cpu_speed}\n")

            if cpu_current_hp > 0:

                # the cpu selected will now be attacking --------------------------------------------------------------------------

                # select a move to use

                move_selected = random.randint(1, len(cpu_attacks))

                if move_selected == 1:
                    move_selected = cpu_attacks[0]

                elif move_selected == 2:
                    move_selected = cpu_attacks[1]

                elif move_selected == 3:
                    move_selected = cpu_attacks[2]

                elif move_selected == 4:
                    move_selected = cpu_attacks[3]

                # get the move (power and type)

                (
                    move_power,
                    move_type,
                    cpu_current_hp,
                    cpu_phys,
                    cpu_spec,
                    cpu_speed,
                    player_phys,
                    player_spec,
                    player_speed,
                ) = get_move_info(
                    move_selected,
                    cpu_current_hp,
                    cpu_health,
                    cpu_phys,
                    cpu_spec,
                    cpu_speed,
                    player_phys,
                    player_spec,
                    player_speed,
                )

                if move_type == "phys":
                    move_damage = int(
                        damage_calc(cpu_phys, player_phys, cpu_level, move_power)
                    )

                if move_type == "spec":
                    move_damage = int(
                        damage_calc(cpu_spec, player_spec, cpu_level, move_power)
                    )

                if move_type == "Stat":
                    move_damage = 0

                # finish damage calculation with effectiveness multiplier
                effectiveness = get_type_effectiveness(cpu_type, player_type)
                move_damage *= effectiveness

                time.sleep(1)
                # display attack selected and affect of attack
                print(f"\nCPUs {cpu_name} used {move_selected} ")
                time.sleep(1)

                if effectiveness > 1 and move_damage > 0:
                    print("\nIts super effective!")
                elif effectiveness < 1 and move_damage > 0:
                    print("\nIts not very effective.")
                elif effectiveness == 1 and move_damage > 0:
                    print("\nIt was effective.")

                display_move_changes(move_selected, cpu_name, player_name)

                # re-calculate health stat after damage
                player_current_hp -= int(move_damage)
                if player_current_hp < 0:
                    player_current_hp = 0
                    break

                os.system("cls")

        elif cpu_faster == True:
            # cpu selected is faster than player selected------------------------------------------------------------------------

            # select a move to use
            typo = True
            while typo == True:
                print(f"{player_name}s Moves: ")
                print("|", end="")
                counter = 0
                while counter < len(player_attacks):
                    print(f" {counter + 1}.{player_attacks[counter]} | ", end="")
                    counter += 1

                player_move_selected = input("\nSelect a move. ")
                try:
                    if (
                        player_move_selected == "1"
                        or player_move_selected.capitalize() == player_attacks[0]
                    ):
                        player_move_selected = player_attacks[0]
                        typo = False

                    elif (
                        player_move_selected == "2"
                        or player_move_selected.capitalize() == player_attacks[1]
                    ):
                        player_move_selected = player_attacks[1]
                        typo = False

                    elif (
                        player_move_selected == "3"
                        or player_move_selected.capitalize() == player_attacks[2]
                    ):
                        player_move_selected = player_attacks[2]
                        typo = False

                    elif (
                        player_move_selected == "4"
                        or player_move_selected.capitalize() == player_attacks[3]
                    ):
                        player_move_selected = player_attacks[3]
                        typo = False

                    else:
                        print("You typed it in wrong silly\n")
                        typo = True
                except:
                    print("You typed it in wrong silly\n")

            # select a move to use

            move_selected = random.randint(1, len(cpu_attacks))

            if move_selected == 1:
                move_selected = cpu_attacks[0]

            elif move_selected == 2:
                move_selected = cpu_attacks[1]

            elif move_selected == 3:
                move_selected = cpu_attacks[2]

            elif move_selected == 4:
                move_selected = cpu_attacks[3]

            # get the move (power and type)

            (
                move_power,
                move_type,
                cpu_current_hp,
                cpu_phys,
                cpu_spec,
                cpu_speed,
                player_phys,
                player_spec,
                player_speed,
            ) = get_move_info(
                move_selected,
                cpu_current_hp,
                cpu_health,
                cpu_phys,
                cpu_spec,
                cpu_speed,
                player_phys,
                player_spec,
                player_speed,
            )

            if move_type == "phys":
                move_damage = int(
                    damage_calc(cpu_phys, player_phys, cpu_level, move_power)
                )

            if move_type == "spec":
                move_damage = int(
                    damage_calc(cpu_spec, player_spec, cpu_level, move_power)
                )

            if move_type == "Stat":
                move_damage = 0

            # finish damage calculation with effectiveness multiplier
            effectiveness = get_type_effectiveness(cpu_type, player_type)
            move_damage *= effectiveness

            time.sleep(1)
            # display attack selected and affect of attack
            print(f"\nCPUs {cpu_name} used {move_selected} ")
            time.sleep(1)

            if effectiveness > 1 and move_damage > 0:
                print("\nIts super effective!")
            elif effectiveness < 1 and move_damage > 0:
                print("\nIts not very effective.")
            elif effectiveness == 1 and move_damage > 0:
                print("\nIt was effective.")

            display_move_changes(move_selected, cpu_name, player_name)

            # re-calculate health stat after damage
            player_current_hp -= int(move_damage)
            if player_current_hp < 0:
                player_current_hp = 0
                break

            os.system("cls")

            display_creature(
                player_level,
                player_type,
                player_name,
                player_current_hp,
                player_health,
                cpu_level,
                cpu_type,
                cpu_name,
                cpu_current_hp,
                cpu_health,
            )

            player_phys = int(player_phys)
            player_spec = int(player_spec)
            player_speed = int(player_speed)
            cpu_phys = int(cpu_phys)
            cpu_spec = int(cpu_spec)
            cpu_speed = int(cpu_speed)
            print(
                f"{player_name}  Phys:{player_phys}  Spec:{player_spec}  Speed:{player_speed}"
            )
            print(f"{cpu_name}  Phys:{cpu_phys}  Spec:{cpu_spec}  Speed:{cpu_speed}\n")
            # player selected will now attack--------------------------------------------------------------------------------------

            move_selected = player_move_selected
            # get the move (power and type)

            (
                move_power,
                move_type,
                player_current_hp,
                player_phys,
                player_spec,
                player_speed,
                cpu_phys,
                cpu_spec,
                cpu_speed,
            ) = get_move_info(
                move_selected,
                player_current_hp,
                player_health,
                player_phys,
                player_spec,
                player_speed,
                cpu_phys,
                cpu_spec,
                cpu_speed,
            )

            if move_type == "phys":
                move_damage = int(
                    damage_calc(player_phys, cpu_phys, player_level, move_power)
                )

            if move_type == "spec":
                move_damage = int(
                    damage_calc(player_spec, cpu_spec, player_level, move_power)
                )

            if move_type == "Stat":
                move_damage = 0

            # finish damage calculation with effectiveness multiplier
            effectiveness = get_type_effectiveness(player_type, cpu_type)
            move_damage *= effectiveness

            time.sleep(1)
            # display attack selected and affect of attack
            print(f"\nUsers {player_name} used {move_selected} ")
            time.sleep(1)

            if effectiveness > 1 and move_damage > 0:
                print("\nIts super effective!")
            elif effectiveness < 1 and move_damage > 0:
                print("\nIts not very effective.")
            elif effectiveness == 1 and move_damage > 0:
                print("\nIt was effective.")

            display_move_changes(move_selected, player_name, cpu_name)

            # re-calculate health stat after damage
            cpu_current_hp -= int(move_damage)
            if cpu_current_hp < 0:
                cpu_current_hp = 0
                break
            os.system("cls")

    os.system("cls")
    display_creature(
        player_level,
        player_type,
        player_name,
        player_current_hp,
        player_health,
        cpu_level,
        cpu_type,
        cpu_name,
        cpu_current_hp,
        cpu_health,
    )
    time.sleep(2)

    if player_current_hp == 0:
        print(f"Users {player_name} has fainted.\n")

        for creature in player_team:
            if creature[2] == True:
                creature[2] = False
                battle(player_team, cpu_team)

    if cpu_current_hp == 0:
        print(f"CPUs {cpu_name} has fainted.\n")

        for creature in cpu_team:
            if creature[2] == True:
                creature[2] = False
                battle(player_team, cpu_team)

    time.sleep(0.75)

    print("Battle has ended.\n")


player_team = build_team()
cpu_team = generate_team(player_team)
battle(player_team, cpu_team)
