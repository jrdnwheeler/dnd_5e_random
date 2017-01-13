#! python3
# -*- coding: utf-8 -*-

"""
Dungeons and Dragons 5th Edition Character Generator.

Race Selector
"""

import random

__author__ = 'Dustin Rowland'
__email__ = 'lee.rowland@gmail.com'
__copyright__ = '2016, Dustin Rowland'
__status__ = 'Development'

classes = {
    "barbarian": {
        "hit_die": "d12",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4)) * 10)
        }
    },
    "bard": {
        "hit_die": "d8",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)) * 10)
        }
    },
    "cleric": {
        "hit_die": "d8",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)) * 10)
        }
    },
    "druid": {
        "hit_die": "d8",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4)) * 10)
        }
    },
    "fighter": {
        "hit_die": "d10",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)) * 10)
        }
    },
    "monk": {
        "hit_die": "d8",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)))
        }
    },
    "paladin": {
        "hit_die": "d10",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)) * 10)
        }
    },
    "ranger": {
        "hit_die": "d10",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)) * 10)
        }
    },
    "rogue": {
        "hit_die": "d8",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4)) * 10)
        }
    },
    "sorcerer": {
        "hit_die": "d6",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4)) * 10)
        }
    },
    "warlock": {
        "hit_die": "d8",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4)) * 10)
        }
    },
    "wizard": {
        "hit_die": "d6",
        "wealth": {
            "gp": ((random.randint(1, 4) + random.randint(1, 4) +
                    random.randint(1, 4) + random.randint(1, 4)) * 10)
        }
    }
}


def chooseClass():
    """
    chooseClass funtion.
    
    Appends all the classes from the above dictionary into a quick reference
    list, then randomly selects a class, wealth, and hit die.
    """
    cList = []

    for cla in classes:
        cList.append(cla)

    charClass = random.choice(cList)
    charClasswealth = classes[charClass]['wealth']
    charHitDie = classes[charClass]['hit_die']

    return charClass, charClasswealth, charHitDie
