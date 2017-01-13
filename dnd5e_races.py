#! python3
# -*- coding: utf-8 -*-

"""
Dungeons and Dragons 5th Edition Character Generator.

Race Selector.
"""

import random
import dnd5e_misc as dndMisc
import dnd5e_stats as dndStats

__author__ = 'Dustin Rowland'
__email__ = 'lee.rowland@gmail.com'
__copyright__ = '2016, Dustin Rowland'
__status__ = 'Development'

skillTree = []
for skill in dndStats.stats['skills']:
    skillTree.append(skill)

races = {
    "elf_high": {
        "race": "elf",
        "subrace": "high",
        "size": "medium",
        "alignment": ["chaotic", "good"],
        "age": [100, 750],  # min (adult), max (elderly)
        "statMod": {
            "dex": 2,
            "int": 1
        },
        "baseHeight": 54,  # height 2d10, weight 1d4
        "baseWeight": 90,
        "modHeight": (random.randint(1, 10) + random.randint(1, 10)),
        "modWeight": (random.randint(1, 4)),
        "speed": 30,
        "vision": "dark60",
        "skill": ["perception"],
        "equipment": ["longsword", "shortsword", "shortbow", "longbow"],
        "resist": [""],
        "language": ["common", "elvish",
                     random.choice(dndMisc.misc['languages'])],
        "spells": [""],
        "misc": {
            "power": ["fey ancestry", "trance", "sunlight sensitivity",
                      "cantrip"]
        }
    },
    "elf_wood": {
        "race": "elf",
        "subrace": "wood",
        "size": "medium",
        "alignment": ["chaotic", "good"],
        "age": [100, 750],  # min (adult), max (elderly)
        "statMod": {
            "dex": 2,
            "wis": 1
        },
        "baseHeight": 54,  # height 2d10, weight 1d4
        "baseWeight": 100,
        "modHeight": (random.randint(1, 10) + random.randint(1, 10)),
        "modWeight": (random.randint(1, 4)),
        "speed": 35,
        "vision": "dark60",
        "skill": ["perception"],
        "equipment": ["longsword", "shortsword", "shortbow", "longbow"],
        "resist": [""],
        "language": ["common", "elvish"],
        "spells": [""],
        "misc": {
            "power": ["fey ancestry", "trance", "sunlight sensitivity",
                      "mask of the wild"]
        }
    },
    "elf_dark": {
        "race": "elf",
        "subrace": "dark",
        "size": "medium",
        "alignment": ["chaotic", "evil"],
        "age": [100, 750],  # min (adult), max (elderly)
        "statMod": {
            "dex": 2,
            "cha": 1
        },
        "baseHeight": 53,  # height 2d6, weight 1d6
        "baseWeight": 75,
        "modHeight": (random.randint(1, 6) + random.randint(1, 6)),
        "modWeight": (random.randint(1, 6)),
        "speed": 30,
        "vision": "dark120",
        "skill": ["perception"],
        "equipment": ["rapier", "shortsword", "hand crossbow"],
        "resist": [""],
        "language": ["common", "elvish"],
        "spells": ["dancing lights", "faerie fire", "darkness"],
        "misc": {
            "power": ["fey ancestry", "trance", "sunlight sensitivity"]
        }
    },
    "dwarf_hill": {
        "race": "dwarf",
        "subrace": "hill",
        "size": "medium",
        "alignment": ["lawful"],
        "age": [50, 350],  # min (adult), max (elderly)
        "statMod": {
            "con": 2,
            "wis": 1
        },
        "baseHeight": 44,  # height 2d4, weight 2d6
        "baseWeight": 115,
        "modHeight": (random.randint(1, 4) + random.randint(1, 4)),
        "modWeight": (random.randint(1, 6) + random.randint(1, 6)),
        "speed": 25,
        "vision": "dark60",
        "skill": [""],
        "equipment": ["battleaxe", "handaxe", "throwing hammer", "warhammer"],
        "resist": [""],
        "language": ["common", "dwarvish"],
        "spells": ["", ""],
        "misc": {
            "power": ["dwarven resiliance",  "tool proficiency",
                      "stonecunning", "dwarven toughness"]
        }
    },
    "dwarf_mtn": {
        "race": "dwarf",
        "subrace": "mountain",
        "size": "medium",
        "alignment": ["lawful"],
        "age": [50, 350],  # min (adult), max (elderly)
        "statMod": {
            "con": 2,
            "str": 2
        },
        "baseHeight": 48,  # height 2d4, weight 2d6
        "baseWeight": 130,
        "modHeight": (random.randint(1, 4) + random.randint(1, 4)),
        "modWeight": (random.randint(1, 6) + random.randint(1, 6)),
        "speed": 25,
        "vision": "dark60",
        "skill": [""],
        "equipment": ["battleaxe", "handaxe", "throwing hammer", "warhammer",
                      "light armor", "medium armor"],
        "resist": [""],
        "language": ["common", "dwarvish"],
        "spells": ["", ""],
        "misc": {
            "power": ["dwarven resiliance",  "stonecunning",
                      "tool proficiency"]
        }
    },
    "gnome_forest": {
        "race": "gnome",
        "subrace": "forest",
        "size": "small",
        "alignment": ["good"],
        "age": [35, 450],  # min (adult), max (elderly)
        "statMod": {
            "int": 2,
            "dex": 1
        },
        "baseHeight": 35,  # height 2d4, weight 1
        "baseWeight": 35,
        "modHeight": (random.randint(1, 4) + random.randint(1, 4)),
        "modWeight": (1),
        "speed": 25,
        "vision": "dark60",
        "skill": [""],
        "equipment": [""],
        "resist": [""],
        "language": ["common", "gnomish"],
        "spells": ["", ""],
        "misc": {
            "power": ["Gnome Cunning", "illusion", "speak with beasts"]
        }
    },
    "gnome_rock": {
        "race": "gnome",
        "subrace": "rock",
        "size": "small",
        "alignment": ["good"],
        "age": [35, 450],  # min (adult), max (elderly)
        "statMod": {
            "int": 2,
            "con": 1
        },
        "baseHeight": 35,  # height 2d4, weight 1
        "baseWeight": 35,
        "modHeight": (random.randint(1, 4) + random.randint(1, 4)),
        "modWeight": (1),
        "speed": 25,
        "vision": "dark60",
        "skill": [""],
        "equipment": [""],
        "resist": [""],
        "language": ["common", "gnomish"],
        "spells": ["", ""],
        "misc": {
            "power": ["Gnome Cunning", "artificer's lore", "tinker"]
        }
    },
    "human": {
        "race": "human",
        "subrace": "",
        "size": "medium",
        "alignment": [""],
        "age": [18, 80],  # min (adult), max (elderly)
        "statMod": {
            "str": 1,
            "dex": 1,
            "con": 1,
            "int": 1,
            "wis": 1,
            "cha": 1
        },
        "baseHeight": 56,  # height 2d10, weight 2d4
        "baseWeight": 110,
        "modHeight": (random.randint(1, 10) + random.randint(1, 10)),
        "modWeight": (random.randint(1, 4) + random.randint(1, 4)),
        "speed": 30,
        "vision": "normal",
        "skill": [""],
        "equipment": [""],
        "resist": [""],
        "language": ["common", random.choice(dndMisc.misc['languages'])],
        "spells": ["", ""],
        "misc": {
            "power": ["", ""]
        }
    },
    "half-elf": {
        "race": "half-elf",
        "subrace": "",
        "size": "medium",
        "alignment": ["chaotic"],
        "age": [20, 200],  # min (adult), max (elderly)
        "statMod": {
            "cha": 2,
            random.choice(["str", "dex", "con", "int", "wis"]): 1  # select 2x
        },
        "baseHeight": 57,  # height 2d8, weight 2d4
        "baseWeight": 110,
        "modHeight": (random.randint(1, 8) + random.randint(1, 8)),
        "modWeight": (random.randint(1, 4) + random.randint(1, 4)),
        "speed": 30,
        "vision": "dark60",
        "skill": [random.choice(skillTree), random.choice(skillTree)],
        "equipment": [""],
        "resist": [""],
        "language": ["common", "elven",
                     random.choice(dndMisc.misc['languages'])],
        "spells": ["", ""],
        "misc": {
            "power": ["Fey Ancestry"]
        }
    },
    "half-orc": {
        "race": "half-orc",
        "subrace": "",
        "size": "medium",
        "alignment": ["chaotic", "evil"],
        "age": [14, 70],  # min (adult), max (elderly)
        "statMod": {
            "str": 2,
            "con": 1
        },
        "baseHeight": 58,  # height 2d10, weight 2d6
        "baseWeight": 140,
        "modHeight": (random.randint(1, 10) + random.randint(1, 10)),
        "modWeight": (random.randint(1, 6) + random.randint(1, 6)),
        "speed": 30,
        "vision": "dark60",
        "skill": ["intimidation"],
        "equipment": [""],
        "resist": [""],
        "language": ["common", "orc"],
        "spells": ["", ""],
        "misc": {
            "power": ["relentless_endurance", "savage attacks"]
        }
    },
    "halfling_lightfoot": {
        "race": "halfling",
        "subrace": "lightfoot",
        "size": "small",
        "alignment": ["lawful", "good"],
        "age": [20, 250],  # min (adult), max (elderly)
        "statMod": {
            "dex": 2,
            "cha": 1
        },
        "baseHeight": 31,  # height 2d4, weight 1
        "baseWeight": 35,
        "modHeight": (random.randint(1, 4) + random.randint(1, 4)),
        "modWeight": (1),
        "speed": 25,
        "vision": "normal",
        "skill": [""],
        "equipment": [""],
        "resist": [""],
        "language": ["common", "halfling"],
        "spells": ["", ""],
        "misc": {
            "power": ["lucky", "halfling nimbleness",
                      "brave", "naturally stealthy"]
        }
    },
    "halfling_stout": {
        "race": "halfling",
        "subrace": "stout",
        "size": "small",
        "alignment": ["lawful", "good"],
        "age": [20, 250],  # min (adult), max (elderly)
        "statMod": {
            "dex": 2,
            "con": 1
        },
        "baseHeight": 31,  # height 2d4, weight 1
        "baseWeight": 35,
        "modHeight": (random.randint(1, 4) + random.randint(1, 4)),
        "modWeight": (1),
        "speed": 25,
        "vision": "normal",
        "skill": [""],
        "equipment": [""],
        "resist": ["poison"],
        "language": ["common", "halfling"],
        "spells": ["", ""],
        "misc": {
            "power": ["lucky", "halfling nimbleness",
                      "brave", "stout resiliance"]
        }
    },
    "tiefling": {
        "race": "tiefling",
        "subrace": "",
        "size": "medium",
        "alignment": ["chaotic"],
        "age": [18, 90],  # min (adult), max (elderly)
        "statMod": {
            "cha": 2,
            "int": 1
        },
        "baseHeight": 57,  # height 2d8, weight 2d4
        "baseWeight": 110,
        "modHeight": (random.randint(1, 8) + random.randint(1, 8)),
        "modWeight": (random.randint(1, 4) + random.randint(1, 4)),
        "speed": 30,
        "vision": "dark60",
        "skill": [""],
        "equipment": [""],
        "resist": ["fire"],
        "language": ["common", "infernal"],
        "spells": ["thaumaturgy", "darkness"],
        "misc": {
            "power": [""]
        }
    },
    "dragonborn": {
        "race": "dragonborn",
        "subrace": "",
        "size": "medium",
        "alignment": [""],
        "age": [15, 80],  # min (adult), max (elderly)
        "statMod": {
            "str": 2,
            "cha": 1
        },
        "baseHeight": 66,  # height 2d8, weight, 2d6
        "baseWeight": 175,
        "modHeight": (random.randint(1, 8) + random.randint(1, 8)),
        "modWeight": (random.randint(1, 6) + random.randint(1, 6)),
        "speed": 30,
        "vision": "normal",
        "skill": [""],
        "equipment": [""],
        "resist": ["draconic ancestry"],
        "language": ["common", "draconic"],
        "spells": ["", ""],
        "misc": {
            "power": ["breath weapon", ""]
        }
    }
}


def chooseRace():
    """
    chooseRace function.

    Append all the races to a quick reference list, the select all of the
    character attributes related.
    """
    rList = []

    for race in races:
        rList.append(race)

    selectedRace = random.choice(rList)
    charRace = races[selectedRace]['race']
    charSubrace = races[selectedRace]['subrace']
    charSize = races[selectedRace]['size']
    charAge = random.randint(races[selectedRace]['age'][0],
                             races[selectedRace]['age'][1])
    charStatMod = races[selectedRace]['statMod']

    return charRace, charSubrace, selectedRace, charSize, charAge, charStatMod


def chooseAlignment(charRace):
    """
    chooseAlignment function.

    Decide on the characters alignment.
    """
    charAlign = races[charRace]['alignment']

    if 'good' in charAlign:
        if 'lawful' in charAlign:
            charAlign = ["lawful", "good"]
        elif 'chaotic' in charAlign:
            charAlign = ["chaotic", "good"]
        else:
            charAlign = [random.choice(["chaotic", "lawful", "neutral"]),
                         "good"]
    elif 'evil' in charAlign:
        if 'lawful' in charAlign:
            charAlign = ["lawful", "evil"]
        elif 'chaotic' in charAlign:
            charAlign = ["chaotic", "evil"]
        else:
            charAlign = [random.choice(["chaotic", "lawful", "neutral"]),
                         "evil"]
    else:
        if 'lawful' in charAlign:
            charAlign = ["lawful", random.choice(["good", "evil", "neutral"])]
        elif 'chaotic' in charAlign:
            charAlign = ["chaotic", random.choice(["good", "evil", "neutral"])]
        else:
            charAlign = [random.choice(["chaotic", "lawful", "neutral"]),
                         random.choice(["good", "evil", "neutral"])]

    return charAlign


def calcHW(charRace):
    """
    calcHW function.

    Calculate random height and weight.
    """
    for cR in races:
        if cR == charRace:
            modHeight = races[charRace]['modHeight']
            modWeight = races[charRace]['modWeight'] * modHeight
            baseHeight = races[charRace]['baseHeight'] + modHeight
            baseWeight = races[charRace]['baseWeight'] + modWeight

    charHeight = "{0}\'{1}\"".format((baseHeight // 12), (baseHeight % 12))
    charWeight = baseWeight

    return charHeight, charWeight
