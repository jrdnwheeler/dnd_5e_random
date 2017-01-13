#! python3
# -*- coding: utf-8 -*-

"""
Dungeons and Dragons 5th Edition Character Generator.

Background Selector
-You either spend coin on gear, or use the gear from your background.
-2x personality, 1x idea, 1x bond, 1x flaw.
"""

import random

__author__ = 'Dustin Rowland'
__email__ = 'lee.rowland@gmail.com'
__copyright__ = '2016, Dustin Rowland'
__status__ = 'Development'

backgrounds = {
    "acolyte": {
        "skills": ["insight", "religion"],
        "tools": [""],
        "language": "2x players choice",
        "equipment": ["holy symbol", "prayer book", "5 sticks of incense",
                      "vestments", "set of common clothes"],
        "wealth": {"gp": 15},
        "feature": """Shelter of the Faithful - As an acolyte, you command the
                      respect of those who share your faith, and you can
                      perform the religious ceremonies of your diety. You and
                      your adventuring companions can expect to receive free
                      healing and care at a temple, shribe, or other
                      established presence of your faith, though you must
                      provide material components needed for your spells.
                      Those who share your religion will support you (but only
                      you) at a modest lifestyle. \n You might also have ties
                      to a specific pantheon, and you have a residence there.
                      This could be the temple where you used to serve, if you
                      remain on good terms with it, or a temple where you have
                      found a new home. While near your temple, you can call
                      upon the priests for assistance, provided the assistance
                      you ask if not hazardous and you remain in good standing
                      with your temple.""",
        "misc": {},
        "personality": {
            1: "I idolize a particular hero of my faith, and constantly refer \
                to that person's deeds and example.",
            2: "I can find common ground between the fiercest enemies, \
                empathizing with them and always working toward peace.",
            3: "I see omens in every event and action. The gods try to speak \
                to us, we just need to listen.",
            4: "Nothing can shake my optimistic attitude.",
            5: "I quote (or misquote) sacred texts and proverbs in almost \
                every situation.",
            6: "I am tolerant (or intolerant) of other faiths and respect \
                (or condemn) the worship of other gods.",
            7: "I've enjoyed fine food, drink, and high society among my \
                temple's elite. Rough living grates on me.",
            8: "I've spent so long in the temple that I have little practical \
                experience dealing with people in the outside world."
        },
        "ideal": {
            1: "Tradition - The ancient traditions of worship and sacrifice \
                must be preserved and upheld. (Lawful)",
            2: "Charity - I always try to help those in need, no matter what \
                the personal cost. (Good)",
            3: "Change - We must help bring about the changes the gods are \
                constantly working in the world. (Chaotic)",
            4: "Power - I hope to one day rise to the top of my faith's \
                religious hierarchy. (Lawful)",
            5: "Faith - I trust that my deity will guide my actions. I have \
                faith that if I work hard, things will go well. (Lawful)",
            6: "Aspiration - I seek to prove myself worthy of my god's favor \
                by matching my actions against his or her teachings. (Any)"
        },
        "bond": {
            1: "I would die to recover an ancient relic of my faith that was \
                lost long ago.",
            2: "I will someday get revenge on the corrupt temple hierarchy \
                who branded me a heretic.",
            3: "I owe my life to the priest who took me in when my parents \
                died.",
            4: "Everything I do is for the common people.",
            5: "I will do anything to protect the temple where I served.",
            6: "I seek to preserve a sacred text that my enemies consider \
                heretical and seek to destroy."
        },
        "flaw": {
            1: "I judge others too harshly, and myself even more severely.",
            2: "I put too much trust in those who wield power within my \
                temple's hierarchy.",
            3: "My piety sometimes leads me to blindly trust those that \
                profess faith in my god.",
            4: "I am inflexible in my thinking.",
            5: "I am suspicious of strangers and expect the worst of them.",
            6: "Once I pick a goal, I become obsessed with it to the \
                detriment of everything else in my life."
        }
    },
    "charlatan": {
        "skills": ["deception", "slight of hand"],
        "tools": ["disguise kit", "forgery kit"],
        "language": "",
        "equipment": ["set of fine clothes", "tools related to your scam"],
        "wealth": {"gp": 15},
        "feature": """False Identity - You have created a second identity that
                    includes documentation, established acquaintances, and
                    disguises that allow you to assume that persona.
                    Additionally, you can forge documents including official
                    papers and personal letters, as long as you have seen an
                    example of the kind of document or the handwriting you
                    are trying to copy.""",
        "misc": {
            "varient": {
                1: "I cheat at games of chance.",
                2: "I shave coins or forge documents.",
                3: "I insinuate myself into people's lives to prey on their \
                    weakness and secure their fortunes.",
                4: "I put on new identities like clothes.",
                5: "I run sleight of hand cons on street corners.",
                6: "I convince people that worthless junk is worth their \
                    hard-earned money."
            }
        },
        "personality": {
            1: "I fall in and out of love easily, and am always pursuing \
                someone.",
            2: "I have a joke for every occasion, especially occasions where \
                humor is inappropriate.",
            3: "Flattery is my preferred trick for getting what I want.",
            4: "I'm a born gambler who can't resist taking a risk for a \
                potential payoff.",
            5: "I lie about almost everything, even when there's no good \
                reason to.",
            6: "Sarcasm and insults are my weapons of choice.",
            7: "I keep multiple holy symbols on me and invoke whatever deity \
                might come in useful at any given moment.",
            8: "I pocket anything I see that might have some value."
        },
        "ideal": {
            1: "Independence - I am a free spirit, no one tells me what to \
                do. (Chaotic)",
            2: "Fairness - I never target people who can't afford to lose a \
                few coins. (Lawful)",
            3: "Charity - I distribute the money I acquire to the people who \
                really need it. (Good)",
            4: "Creativity - I never run the same con twice. (Chaotic)",
            5: "Friendship - Material goods come and go. Bonds of friendship \
                last forever. (Good)",
            6: "Aspiration - I'm determined to make something of myself. (Any)"
        },
        "bond": {
            1: "I fleeced the wrong person and must work to ensure that this \
                individual never crosses paths with me or those I care about.",
            2: "I owe everything to my mentor - a horrible person who's \
                probably rotting in jail somewhere.",
            3: "Somewhere out there, I have a child who doesn't know me. I'm \
                making the world better for him or her.",
            4: "I come from a noble family, and one day I'll reclaim my lands \
                and title from those who stole them from me.",
            5: "A powerful person killed someone I love. Someday soon, I'll \
                have my revenge.",
            6: "I swindled and ruined a person who didn't deserve it. I seek \
                to atone for my misdeeds but might never be able to forgive \
                myself."
        },
        "flaw": {
            1: "I can't resist a pretty face.",
            2: "I'm always in debt. I spend my ill-gotten gains on decadent \
                luxuries faster than I bring them in.",
            3: "I'm convinced that no one could ever fool me the way I fool \
                others.",
            4: "I'm too greedy for my own good. I can't resist taking a risk \
                if there's money involved.",
            5: "I can't resist swindling people who are more powerful than \
                me.",
            6: "I hate to admit it and will hate myself for it, but I'll run \
                and preserve my own hide if the going gets tough."
        }
    },
    "criminal": {
        "skills": ["deception", "stealth"],
        "tools": ["one type of gaming set", "thieves' tools"],
        "language": "",
        "equipment": ["A crowbar", "a set of dark common clothes", "hood"],
        "wealth": {"gp": 15},
        "feature": """Criminal Contact - You have a reliable and trustworthy
                    contact who acts as your liason to a network of other
                    criminals. You know how to get messages to and from your
                    contact, even over great distances; specifically, you
                    know the local messengers, corrupt caravan masters, and
                    seedy sailors who can deliver messages for you.""",
        "misc": {
            "varient": {
                1: "blackmailer",
                2: "burglar",
                3: "enforcer",
                4: "fence",
                5: "highway robber",
                6: "hired killer",
                7: "pickpocket",
                8: "smuggler"
            }
        },
        "personality": {
            1: "I always have a plan for what to do when things go wrong.",
            2: "I am always calm, no matter what the situation. I never raise \
                my voice or let my emotions control me.",
            3: "The first thing I do in a new place is note the locations of \
                everything valuable or where such things could be hidden.",
            4: "I would rather make a new friend than a new enemy.",
            5: "I am incredibly slow to trust. Those who seem the fairest \
                often have the most to hide.",
            6: "I don't pay attention to the risks in a situation. Never tell \
                me the odds.",
            7: "The best way to get me to do something is to tell me I can't \
                do it.",
            8: "I blow up at the slightest insult."
        },
        "ideal": {
            1: "Honor - I don't steal from others in the trade. (Lawful)",
            2: "Freedom - Chains are meant to be broken, as are those who \
                would forge them. (Chaotic)",
            3: "Charity - I steal from the wealthy so that I can help people \
                in need. (Good)",
            4: "Greed - I will do whatever it takes to become wealthy. (Evil)",
            5: "People - I'm loyal to my friends, not to any ideais, and \
                everyone else can take a trip down the Styx for all I care. \
                (Neutral)",
            6: "Redemption - There's a spark of good in everyone. (Good)"
        },
        "bond": {
            1: "I'm trying to pay off an old debt I owe to a generous \
                benefactor.",
            2: "My ill-gotten gains go to support my family.",
            3: "Something important was taken from me, and I aim to steal it \
                back.",
            4: "I will become the greatest thief that ever lived.",
            5: "I'm guilty of a terrible crime. I hope I can redeem myself \
                for it.",
            6: "Someone I loved died because of I mistake I made. That will \
                never happen again."
        },
        "flaw": {
            1: "When I see something valuable, I can't think about anything \
                but how to steal it.",
            2: "When faced with a choice between money and my friends, I \
                usually choose the money.",
            3: "If there's a plan, I'll forget it. If I don't forget it, I'll \
                ignore it.",
            4: "I have a \"tell\" that reveals when I'm lying.",
            5: "I turn tail and run when things look bad.",
            6: "An innocent person is in prison for a crime that I committed. \
                I'm okay with that."
        }
    },
    "entertainer": {
        "skills": ["acrobatics", "performance"],
        "tools": ["disguise kit", "one type of instrument"],
        "language": "",
        "equipment": ["a musical instrument", "a costume",
                      "the favor of an admirer (lock of hair, trinket, etc)"],
        "wealth": {"gp": 15},
        "feature": """By Popular Demand - You can always find a place to
                    perform, usually in an inn or tavern but possibly with a
                    circus, at a theater, or even in a noble's court. At such
                    a place, you receive free lodging and food of a modest or
                    comfortable standard (depending on the quality of the
                    establishment), as long as you perform each night. In
                    addition, your performance makes you something of a local
                    figure. When strangers recognize you in a town where you
                    have performed, they typically take a liking to you.""",
        "misc": {
            "varient": {
                1: "actor",
                2: "dancer",
                3: "fire-eater",
                4: "jester",
                5: "juggler",
                6: "instrumentalist",
                7: "poet",
                8: "singer",
                9: "storyteller",
                10: "tumbler"
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "folk_hero": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": {
            "varient": {
                1: "I stood up to a tyrent's agents.",
                2: "I saved people during a natural disaster.",
                3: "I stood alone against a terrible monster.",
                4: "I stole from a corrupt merchant to help the poor.",
                5: "I led a militia to fight off an invading army.",
                6: "I broke into a tyrant's castle and stole weapons to arm \
                    the people.",
                7: "I trained the peasantry to use farm implements as weapons \
                    against a tyrant's soldiers.",
                8: "A lord rescinded an unpopuler decree after I led a \
                    symbolic act of protest against it.",
                9: "A celestial, fey, or similar creature gave me a blessing \
                    or revealed my secret origins.",
                10: "Recruited into a lord's army, I rose to leadership and \
                     was commended for my heroism."
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "guild_artisan": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": {
            "varient": {
                1: "Alchemists and apothecaries",
                2: "Armorers, locksmiths, and finesmiths",
                3: "Brewers, distillers, and vintners",
                4: "Calligraphers, scribes, and scriveners",
                5: "Carpenters, roofers, and plasterers",
                6: "Cartographers, surveyors, and chart-makers",
                7: "Cobblers and shoemakers",
                8: "Cooks and bakers",
                9: "Glassblowers and glaziers",
                10: "Jewelers and gemcutters",
                11: "Leatherworkers, skinners, and tanners",
                12: "Masons and stonecutters",
                13: "Painters, limners, and sign-makers",
                14: "Potters and tile-makers",
                15: "Shipwrights and sailmakers",
                16: "Smiths and metal-forgers",
                17: "Tinkers, pewterers, and casters",
                18: "Wagon-makers and wheelwrights",
                19: "Weavers and dyers",
                20: "Woodcarvers, coopers, and bowyers"
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "hermit": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": {
            "varient": {
                1: "I was searching for spiritual enlightenment.",
                2: "I was partaking of communal living in accordance with the \
                    dictates of a religious order.",
                3: "I was exiled for a crime I didn't commit.",
                4: "I retreated from society after a life-altering event.",
                5: "I needed a quiet place to work on my art, literature, \
                    music, or manifesto.",
                6: "I needed to commune with nature, far from civilization.",
                7: "I was the caretaker of an ancient ruin or relic.",
                8: "I was a pilgrim in search of a person, place, or relic of \
                    spiritual significance."
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "noble": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": "",
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "outlander": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": {
            "varient": {
                1: "",
                2: "",
                3: "",
                4: "",
                5: "",
                6: "",
                7: "",
                8: "",
                9: "",
                10: ""
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "sage": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": {
            "varient": {
                1: "Alchmist",
                2: "Astronomer",
                3: "Discredited acadmic",
                4: "Librarian",
                5: "Professor",
                6: "Researcher",
                7: "Wizard's Apprentice",
                8: "Scribe"
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "sailor": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": "",
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "soldier": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": {
            "varient": {
                1: "Officer",
                2: "Scout",
                3: "Infantry",
                4: "Cavalry",
                5: "Healer",
                6: "Quartermaster",
                7: "Standard Bearer",
                8: "Support staff (cook, blacksmith, etc)"
            }
        },
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    },
    "urchin": {
        "skills": ["", ""],
        "tools": [""],
        "language": "",
        "equipment": [""],
        "wealth": {"gp": 0},
        "feature": "",
        "misc": "",
        "personality": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        },
        "ideal": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "bond": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        },
        "flaw": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
    }
}


def chooseBG():
    """
    chooseBG function.

    Appends all the background names to a list for quick reference, then
    randomly selects a background and the attributes for that background.

    The weird line breaks below are to meet PEP8.
    """
    bgList = []
    for bg in backgrounds:
        bgList.append(bg)

    charBG = random.choice(bgList)
    charBGskills = backgrounds[charBG]['skills']
    charBGtools = backgrounds[charBG]['tools']
    charBGlanguage = backgrounds[charBG]['language']
    charBGequipment = backgrounds[charBG]['equipment']
    charBGwealth = backgrounds[charBG]['wealth']
    charBGpersonality = [backgrounds[charBG]['personality'][
                            random.randint(1, 8)],
                         backgrounds[charBG]['personality']
                         [random.randint(1, 8)]]
    charBGideal = backgrounds[charBG]['ideal'][random.randint(1, 6)]
    charBGbond = backgrounds[charBG]['bond'][random.randint(1, 6)]
    charBGflaw = backgrounds[charBG]['flaw'][random.randint(1, 6)]

    if 'varient' in backgrounds[charBG]['misc']:
        charBGvarient = backgrounds[charBG]['misc']['varient'][
                            random.randint(1,
                                           len(backgrounds[charBG]['misc']
                                               ['varient']))]
    else:
        charBGvarient = ""

    return charBG, charBGpersonality, charBGideal, charBGbond, charBGflaw, \
        charBGskills, charBGlanguage, charBGequipment, charBGwealth, \
        charBGtools, charBGvarient
