#! python3
# -*- coding: utf-8 -*-

"""
Dungeons and Dragons 5th Edition Character Generator

Misc Calculators and Generators
"""

import random

__author__ = 'Dustin Rowland'
__email__ = 'lee.rowland@gmail.com'
__copyright__ = '2016, Dustin Rowland'
__status__ = 'Development'

misc = {
    "gender": ["male", "female"],
    "languages": [
        'common', 'dwarvish', 'elvish', 'giant', 'gnomish', 'goblin',
        'halfling', 'orc', 'abyssal', 'celestial', 'draconic', 'deep speech',
        'infernal', 'primordial', 'sylvan', 'undercommon'
    ]
}

def getGender():
    return random.choice(misc['gender'])
