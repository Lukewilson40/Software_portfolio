import os
import time

no_effect = []
not_very_effectives = []
normal_effectives = []
super_effectives = []
pokemon_types = []

typo = True
while typo == True:
    try:
        num_types = int(input("\nHow many types does your pokemon have? "))
        typo = False
    except:
        os.system("cls")

type_list = [
    "normal",
    "fire",
    "water",
    "electric",
    "grass",
    "ice",
    "fighting",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dragon",
    "dark",
    "steel",
    "fairy",
]

get_types = 0
while get_types < num_types:
    print(
        """
The pokemon Types are:
normal, fire, water, electric, grass, ice, fighting, poison, ground,  
flying, psychic, bug, rock, ghost, dragon, dark, steel, and fairy.
"""
    )
    if len(pokemon_types) > 0:
        print("Type Combo: ", end="")

    for type in pokemon_types:
        print(f"{type} ", end="")

    input_type = str(input("\nEnter a pokemon type: "))
    if input_type.lower() in type_list:
        pokemon_types.append(input_type)
        get_types += 1
        os.system("cls")
    else:
        os.system("cls")
        print("\nSorry, there was a typo, try again.")
        time.sleep(1)
        os.system("cls")

print(f"\nYour pokemon's type is {'-'.join(pokemon_types)}\n")

normal = {
    "normal": 1,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 1,
    "fighting": 1,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 1,
    "bug": 1,
    "rock": 0.5,
    "ghost": 0,
    "dragon": 1,
    "dark": 1,
    "steel": 0.5,
    "fairy": 1,
}
fire = {
    "normal": 1,
    "fire": 0.5,
    "water": 0.5,
    "electric": 1,
    "grass": 2,
    "ice": 2,
    "fighting": 1,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 1,
    "bug": 2,
    "rock": 0.5,
    "ghost": 1,
    "dragon": 0.5,
    "dark": 1,
    "steel": 2,
    "fairy": 1,
}
water = {
    "normal": 1,
    "fire": 2,
    "water": 0.5,
    "electric": 1,
    "grass": 0.5,
    "ice": 1,
    "fighting": 1,
    "poison": 1,
    "ground": 2,
    "flying": 1,
    "psychic": 1,
    "bug": 1,
    "rock": 2,
    "ghost": 1,
    "dragon": 0.5,
    "dark": 1,
    "steel": 1,
    "fairy": 1,
}
electric = {
    "normal": 1,
    "fire": 1,
    "water": 2,
    "electric": 0.5,
    "grass": 0.5,
    "ice": 1,
    "fighting": 1,
    "poison": 1,
    "ground": 0,
    "flying": 2,
    "psychic": 1,
    "bug": 1,
    "rock": 1,
    "ghost": 1,
    "dragon": 0.5,
    "dark": 1,
    "steel": 1,
    "fairy": 1,
}
grass = {
    "normal": 1,
    "fire": 0.5,
    "water": 2,
    "electric": 1,
    "grass": 0.5,
    "ice": 1,
    "fighting": 1,
    "poison": 0.5,
    "ground": 2,
    "flying": 0.5,
    "psychic": 1,
    "bug": 0.5,
    "rock": 2,
    "ghost": 1,
    "dragon": 0.5,
    "dark": 1,
    "steel": 0.5,
    "fairy": 1,
}
ice = {
    "normal": 1,
    "fire": 0.5,
    "water": 0.5,
    "electric": 1,
    "grass": 2,
    "ice": 0.5,
    "fighting": 1,
    "poison": 1,
    "ground": 2,
    "flying": 2,
    "psychic": 1,
    "bug": 1,
    "rock": 1,
    "ghost": 1,
    "dragon": 2,
    "dark": 1,
    "steel": 0.5,
    "fairy": 1,
}
fighting = {
    "normal": 2,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 2,
    "fighting": 1,
    "poison": 0.5,
    "ground": 1,
    "flying": 0.5,
    "psychic": 0.5,
    "bug": 0.5,
    "rock": 2,
    "ghost": 0,
    "dragon": 1,
    "dark": 2,
    "steel": 2,
    "fairy": 0.5,
}
poison = {
    "normal": 1,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 2,
    "ice": 1,
    "fighting": 1,
    "poison": 0.5,
    "ground": 0.5,
    "flying": 1,
    "psychic": 1,
    "bug": 1,
    "rock": 0.5,
    "ghost": 0.5,
    "dragon": 1,
    "dark": 1,
    "steel": 0,
    "fairy": 2,
}
ground = {
    "normal": 1,
    "fire": 2,
    "water": 1,
    "electric": 2,
    "grass": 0.5,
    "ice": 1,
    "fighting": 1,
    "poison": 2,
    "ground": 1,
    "flying": 0,
    "psychic": 1,
    "bug": 0.5,
    "rock": 2,
    "ghost": 1,
    "dragon": 1,
    "dark": 1,
    "steel": 2,
    "fairy": 1,
}
flying = {
    "normal": 1,
    "fire": 1,
    "water": 1,
    "electric": 0.5,
    "grass": 2,
    "ice": 1,
    "fighting": 2,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 1,
    "bug": 2,
    "rock": 0.5,
    "ghost": 1,
    "dragon": 1,
    "dark": 1,
    "steel": 0.5,
    "fairy": 1,
}
psychic = {
    "normal": 1,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 1,
    "fighting": 2,
    "poison": 2,
    "ground": 1,
    "flying": 1,
    "psychic": 0.5,
    "bug": 1,
    "rock": 1,
    "ghost": 1,
    "dragon": 1,
    "dark": 0,
    "steel": 0.5,
    "fairy": 1,
}
bug = {
    "normal": 1,
    "fire": 0.5,
    "water": 1,
    "electric": 1,
    "grass": 2,
    "ice": 1,
    "fighting": 0.5,
    "poison": 0.5,
    "ground": 1,
    "flying": 0.5,
    "psychic": 2,
    "bug": 1,
    "rock": 1,
    "ghost": 0.5,
    "dragon": 1,
    "dark": 2,
    "steel": 0.5,
    "fairy": 0.5,
}
rock = {
    "normal": 1,
    "fire": 2,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 2,
    "fighting": 0.5,
    "poison": 1,
    "ground": 0.5,
    "flying": 2,
    "psychic": 1,
    "bug": 2,
    "rock": 1,
    "ghost": 1,
    "dragon": 1,
    "dark": 1,
    "steel": 0.5,
    "fairy": 1,
}
ghost = {
    "normal": 0,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 1,
    "fighting": 1,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 2,
    "bug": 1,
    "rock": 1,
    "ghost": 2,
    "dragon": 1,
    "dark": 0.5,
    "steel": 1,
    "fairy": 1,
}
dragon = {
    "normal": 1,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 1,
    "fighting": 1,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 1,
    "bug": 1,
    "rock": 1,
    "ghost": 1,
    "dragon": 2,
    "dark": 1,
    "steel": 0.5,
    "fairy": 0,
}
dark = {
    "normal": 1,
    "fire": 1,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 1,
    "fighting": 0.5,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 2,
    "bug": 1,
    "rock": 1,
    "ghost": 2,
    "dragon": 1,
    "dark": 0.5,
    "steel": 1,
    "fairy": 0.5,
}
steel = {
    "normal": 1,
    "fire": 0.5,
    "water": 0.5,
    "electric": 0.5,
    "grass": 1,
    "ice": 2,
    "fighting": 1,
    "poison": 1,
    "ground": 1,
    "flying": 1,
    "psychic": 1,
    "bug": 1,
    "rock": 2,
    "ghost": 1,
    "dragon": 1,
    "dark": 1,
    "steel": 0.5,
    "fairy": 2,
}
fairy = {
    "normal": 1,
    "fire": 0.5,
    "water": 1,
    "electric": 1,
    "grass": 1,
    "ice": 1,
    "fighting": 2,
    "poison": 0.5,
    "ground": 1,
    "flying": 1,
    "psychic": 1,
    "bug": 1,
    "rock": 1,
    "ghost": 1,
    "dragon": 2,
    "dark": 2,
    "steel": 0.5,
    "fairy": 1,
}


normal_effect = 1
fire_effect = 1
water_effect = 1
electric_effect = 1
grass_effect = 1
ice_effect = 1
fighting_effect = 1
poison_effect = 1
ground_effect = 1
flying_effect = 1
psychic_effect = 1
bug_effect = 1
rock_effect = 1
ghost_effect = 1
dragon_effect = 1
dark_effect = 1
steel_effect = 1
fairy_effect = 1

get_effect = 0

while get_effect < len(pokemon_types):
    normal_effect = float(normal_effect * normal[pokemon_types[get_effect]])
    fire_effect = float(fire_effect * fire[pokemon_types[get_effect]])
    water_effect = float(water_effect * water[pokemon_types[get_effect]])
    electric_effect = float(electric_effect * electric[pokemon_types[get_effect]])
    grass_effect = float(grass_effect * grass[pokemon_types[get_effect]])
    ice_effect = float(ice_effect * ice[pokemon_types[get_effect]])
    fighting_effect = float(fighting_effect * fighting[pokemon_types[get_effect]])
    poison_effect = float(poison_effect * poison[pokemon_types[get_effect]])
    ground_effect = float(ground_effect * ground[pokemon_types[get_effect]])
    flying_effect = float(flying_effect * flying[pokemon_types[get_effect]])
    psychic_effect = float(psychic_effect * psychic[pokemon_types[get_effect]])
    bug_effect = float(bug_effect * bug[pokemon_types[get_effect]])
    rock_effect = float(rock_effect * rock[pokemon_types[get_effect]])
    ghost_effect = float(ghost_effect * ghost[pokemon_types[get_effect]])
    dragon_effect = float(dragon_effect * dragon[pokemon_types[get_effect]])
    dark_effect = float(dark_effect * dark[pokemon_types[get_effect]])
    steel_effect = float(steel_effect * steel[pokemon_types[get_effect]])
    fairy_effect = float(fairy_effect * fairy[pokemon_types[get_effect]])

    get_effect += 1

if normal_effect > 1:
    super_effectives.append("normal")
elif normal_effect == 0:
    no_effect.append("normal")
elif normal_effect < 1:
    not_very_effectives.append("normal")
elif normal_effect == 1:
    normal_effectives.append("normal")

if fire_effect > 1:
    super_effectives.append("fire")
elif fire_effect == 0:
    no_effect.append("fire")
elif fire_effect < 1:
    not_very_effectives.append("fire")
elif fire_effect == 1:
    normal_effectives.append("fire")

if water_effect > 1:
    super_effectives.append("water")
elif water_effect == 0:
    no_effect.append("water")
elif water_effect < 1:
    not_very_effectives.append("water")
elif water_effect == 1:
    normal_effectives.append("water")

if electric_effect > 1:
    super_effectives.append("electric")
elif electric_effect == 0:
    no_effect.append("electric")
elif electric_effect < 1:
    not_very_effectives.append("electric")
elif electric_effect == 1:
    normal_effectives.append("electric")

if grass_effect > 1:
    super_effectives.append("grass")
elif grass_effect == 0:
    no_effect.append("grass")
elif grass_effect < 1:
    not_very_effectives.append("grass")
elif grass_effect == 1:
    normal_effectives.append("grass")

if ice_effect > 1:
    super_effectives.append("ice")
elif ice_effect == 0:
    no_effect.append("ice")
elif ice_effect < 1:
    not_very_effectives.append("ice")
elif ice_effect == 1:
    normal_effectives.append("ice")

if fighting_effect > 1:
    super_effectives.append("fighting")
elif fighting_effect == 0:
    no_effect.append("fighting")
elif fighting_effect < 1:
    not_very_effectives.append("fighting")
elif fighting_effect == 1:
    normal_effectives.append("fighting")

if poison_effect > 1:
    super_effectives.append("poison")
elif poison_effect == 0:
    no_effect.append("poison")
elif poison_effect < 1:
    not_very_effectives.append("poison")
elif poison_effect == 1:
    normal_effectives.append("poison")

if ground_effect > 1:
    super_effectives.append("ground")
elif ground_effect == 0:
    no_effect.append("ground")
elif ground_effect < 1:
    not_very_effectives.append("ground")
elif ground_effect == 1:
    normal_effectives.append("ground")

if flying_effect > 1:
    super_effectives.append("flying")
elif flying_effect == 0:
    no_effect.append("flying")
elif flying_effect < 1:
    not_very_effectives.append("flying")
elif flying_effect == 1:
    normal_effectives.append("flying")

if psychic_effect > 1:
    super_effectives.append("psychic")
elif psychic_effect == 0:
    no_effect.append("psychic")
elif psychic_effect < 1:
    not_very_effectives.append("psychic")
elif psychic_effect == 1:
    normal_effectives.append("psychic")

if bug_effect > 1:
    super_effectives.append("bug")
elif bug_effect == 0:
    no_effect.append("bug")
elif bug_effect < 1:
    not_very_effectives.append("bug")
elif bug_effect == 1:
    normal_effectives.append("bug")

if rock_effect > 1:
    super_effectives.append("rock")
elif rock_effect == 0:
    no_effect.append("rock")
elif rock_effect < 1:
    not_very_effectives.append("rock")
elif rock_effect == 1:
    normal_effectives.append("rock")

if ghost_effect > 1:
    super_effectives.append("ghost")
elif ghost_effect == 0:
    no_effect.append("ghost")
elif ghost_effect < 1:
    not_very_effectives.append("ghost")
elif ghost_effect == 1:
    normal_effectives.append("ghost")

if dragon_effect > 1:
    super_effectives.append("dragon")
elif dragon_effect == 0:
    no_effect.append("dragon")
elif dragon_effect < 1:
    not_very_effectives.append("dragon")
elif dragon_effect == 1:
    normal_effectives.append("dragon")

if dark_effect > 1:
    super_effectives.append("dark")
elif dark_effect == 0:
    no_effect.append("dark")
elif dark_effect < 1:
    not_very_effectives.append("dark")
elif dark_effect == 1:
    normal_effectives.append("dark")

if steel_effect > 1:
    super_effectives.append("steel")
elif steel_effect == 0:
    no_effect.append("steel")
elif steel_effect < 1:
    not_very_effectives.append("steel")
elif steel_effect == 1:
    normal_effectives.append("steel")

if fairy_effect > 1:
    super_effectives.append("fairy")
elif fairy_effect == 0:
    no_effect.append("fairy")
elif fairy_effect < 1:
    not_very_effectives.append("fairy")
elif fairy_effect == 1:
    normal_effectives.append("fairy")

print("Move type effectiveness against your pokemon: \n")
print(f'No effect: {", ".join(no_effect)}')
print(f'Not very effective: {", ".join(not_very_effectives)}')
print(f'Normal effectiveness: {", ".join(normal_effectives)}')
print(f'Supereffective: {", ".join(super_effectives)}\n')
