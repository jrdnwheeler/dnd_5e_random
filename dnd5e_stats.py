#! python3
# -*- coding: utf-8 -*-

"""
Dungeons and Dragons 5th Edition Character Generator

Stats Generator and Calculator
"""

import random

__author__ = 'Dustin Rowland'
__email__ = 'lee.rowland@gmail.com'
__copyright__ = '2016, Dustin Rowland'
__status__ = 'Development'

stats = {
    "proficiency": {
        1: 2,
        2: 2,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 4,
        10: 4,
        11: 4,
        12: 4,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 6,
        18: 6,
        19: 6,
        20: 6
    },
    "statRolls": {
        'str': 0,
        'dex': 0,
        'con': 0,
        'int': 0,
        'wis': 0,
        'cha': 0
    },
    "abilityMod": {
        'str': 0,
        'dex': 0,
        'con': 0,
        'int': 0,
        'wis': 0,
        'cha': 0
    },
    "skills": {
        'athletics': 0,
        'acrobatics': 0,
        'slight_of_hand': 0,
        'stealth': 0,
        'arcana': 0,
        'history': 0,
        'investigation': 0,
        'nature': 0,
        'religion': 0,
        'animal_handling': 0,
        'insight': 0,
        'medicine': 0,
        'perception': 0,
        'survival': 0,
        'deception': 0,
        'intimidation': 0,
        'performance': 0,
        'persuasion': 0
    }
}

def rollStats():
    x = 0

    while x < 4:
        for sR in stats['statRolls']:
            stats['statRolls'][sR] += random.randint(1, 6)
        x += 1
    rolledStat = stats['statRolls']
    return rolledStat

def calcAbilityMod(statRolled, mods):
    for aM in statRolled: # add rolled stats to dict
        stats['abilityMod'][aM] += statRolled[aM]

    for aM in mods: # add mods on top of rolled stats
        stats['abilityMod'][aM] += mods[aM]

    for aM in stats['abilityMod']: # calc the abilityMod, reassign
        stats['abilityMod'][aM] = ((stats['abilityMod'][aM] - 10) // 2)

    abilityMod = stats['abilityMod']
    return abilityMod

def getProficiency(level):
    if level in stats['proficiency']:
        return stats['proficiency'][level]
