#! python3
# -*- coding: utf-8 -*-

"""
Dungeons and Dragons 5th Edition Character Generator.

The player enters some basic choices and a new character is generated for the
player with all available stats, armor, and weapons chosen randomly. This is
not for making a badass custom character, this is for quick character creation.
"""

import dnd5e_races as dndRaces
import dnd5e_classes as dndClasses
import dnd5e_backgrounds as dndBG
import dnd5e_equipment as dndEQ
import dnd5e_stats as dndStats
import dnd5e_misc as dndMisc

__author__ = 'Dustin Rowland'
__email__ = 'lee.rowland@gmail.com'
__copyright__ = '2016, Dustin Rowland'
__status__ = 'Development'

# Choose your starting level
while True:
    try:
        charLevel = int(input("Character level: "))
    except ValueError:
        print("Not a valid level number")
        continue
    else:
        if charLevel in range(1, 20):
            break
        else:
            print("Enter a level between 1 and 20")
            continue

charProf = dndStats.getProficiency(charLevel)
charStats = dndStats.rollStats()  # Roll random stats
charRace = dndRaces.chooseRace()  # Choose a Race
charAbility = dndStats.calcAbilityMod(charStats, charRace[5])  # calc Mod
charClass = dndClasses.chooseClass()  # Choose a Class
charAlign = dndRaces.chooseAlignment(charRace[2])  # Character Alignment
charHW = dndRaces.calcHW(charRace[2])  # calc height and weight
charBG = dndBG.chooseBG()  # Background selection
charWealth = charBG[8]['gp'] + charClass[1]['gp']  # calc wealth
charEQtrinket = dndEQ.chooseTrinket()  # random d100 trinket

# Display info, write to Excel
print("Race:", charRace[0])
print("Subrace:", charRace[1])
print("Gender:", dndMisc.getGender())
print("Size:", charRace[3])
print("Age:", charRace[4])
print("Proficiency:", charProf)
print("Stats:", charStats)
print("Race Stat Mods:", charRace[5])
print("Ability Mods:", charAbility)
print("Initiative Mod:", charAbility['dex'])
print("Class:", charClass[0])
print("Hit die:", charClass[2])
print("Alignment:", charAlign)
print("Height:", charHW[0])
print("Weight:", charHW[1])
print("Background:", charBG[0])
print("Varient:", charBG[10])
print("Personality:\n-", charBG[1][0], "\n-", charBG[1][1])
print("Ideal:", charBG[2])
print("Bond:", charBG[3])
print("Flaw:", charBG[4])
print("Pre-Equipment Wealth:", charWealth, "gp")  # comment out, show later
print("BG Skills:", charBG[5])
print("BG Tools:", charBG[9])
print("BG Languages:", charBG[6])
# print("BG Equipment:", charBG[7])  # only used if not using purchased
print("Trinket:", charEQtrinket[0], "({})".format(charEQtrinket[1]))
