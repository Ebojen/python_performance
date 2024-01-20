from random import choice, choices, randint
from string import ascii_letters, digits

NAMES = [
    "James Smith",
    "Michael Smith",
    "Robert Smith",
    "Maria Garcia",
    "David Smith",
    "Maria Rodriguez",
    "Mary Smith",
    "Maria Hernandez",
    "Maria Martinez",
    "James Johnson",
]

RACES = [
    "White",
    "Black or African American",
    "American Indian or Alaska Native",
    "Asian",
    "Native Hawaiian or Other Pacific Islander",
]

STREET_NAMES = [
    "main",
    "center",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "oak",
    "elm",
    "pine",
    "maple",
    "hickory",
]


STREET_TYPES = ["St.", "Dr.", "Ave.", "Blvd.", "Rd."]


def generate_street_address():
    return f"{randint(0, 999)} {choice(STREET_NAMES)} {choice(STREET_TYPES)}"


CITIES = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose",
]

STATES = [
    "New York",
    "California",
    "Illinois",
    "Texas",
    "Arizona",
    "Pennsylvania",
    "Washington",
    "Minnesota",
    "Florida",
    "New Jersey",
]


def generate_phone_number():
    return f"{randint(100, 999)}-{randint(100, 999)}-{randint(1_000, 9_999)}"


PHONE_TYPES = ["home", "mobile", "business"]


EMAIL_DOMAINS = ["gmail", "outlook", "yahoo", "proton"]

CHARS = ascii_letters + digits


def generate_email():
    return f"{choices(CHARS, k=randint(5, 10))}@{choice(EMAIL_DOMAINS)}.com"


EMAIL_TYPES = ["personal", "business"]


def generate_customer():
    return {
        "id": randint(1_000_000_000, 9_999_999_999),
        "name": choice(NAMES),
        "gender": choice(["male", "female", "other"]),
        "race": choice(RACES),
        "active": choice([True, False]),
        "internal": choice([True, False]),
        "address": {
            "street_address": generate_street_address(),
            "city": choice(CITIES),
            "state": choice(STATES),
            "postal_code": randint(10_000, 99_999),
        },
        "phone_numbers": [
            {
                "number": generate_phone_number(),
                "type": choice(PHONE_TYPES),
            }
            for _ in range(randint(0, 3))
        ],
        "emails": [{"email": generate_email(), "type": choice(EMAIL_TYPES)}],
    }


CHAR_NAMES = [
    "Tav",
    "Shadowheart",
    "Astarion",
    "Karlach",
    "Gale",
    "Wyll",
    "Lae'zel",
    "The Dark Urge",
    "Halsin",
    "Minthara",
    "Jaheira",
    "Minsc",
    "Boo",
    "Withers",
    "Scratch",
    "Volo",
    "Braccus",
    "Isobel",
    "Yenna",
    "Tarra",
    "Ulder",
    "Eldra",
    "Brinna",
    "Zenith",
    "Danton",
    "Varanna",
    "Sina'zith",
    "Kerz",
    "Ver'yll",
    "Maddala",
    "Jacelyn",
    "Kree",
    "Cazador",
    "Mizora",
    "Elminster",
]


CLASSES = [
    "alchemist",
    "barbarian",
    "fighter",
    "investigator",
    "psychic",
    "ranger",
    "thaumaturge",
    "witch",
    "bard",
    "champion",
    "kineticist",
    "magus",
    "rogue",
    "sorcerer",
    "wizard",
    "cleric",
    "druid",
    "monk",
    "oracle",
    "summoner",
    "gunslinger",
    "inventor",
]


P2E_RACES = [
    "dwarf",
    "elf",
    "gnome",
    "goblin",
    "halfling",
    "human",
    "azarketi",
    "catfolk",
    "fetchling",
    "gnoll",
    "grippli",
    "hobgoblin",
    "kitsune",
    "kobold",
    "leshy",
    "lizardfolk",
    "nagaji",
    "ork",
    "ratfolk",
    "tengu",
    "vanara",
]


def generate_character():
    return {
        "name": choice(NAMES),
        "class": choice(CLASSES),
        "race": choice(P2E_RACES),
        "stats": {
            "strength": randint(0, 20),
            "dexterity": randint(0, 20),
            "constitution": randint(0, 20),
            "intelligence": randint(0, 20),
            "wisdom": randint(0, 20),
            "charisma": randint(0, 20),
        },
        "skills": {
            "acrobatics": randint(0, 10),
            "arcana": randint(0, 10),
            "athletics": randint(0, 10),
            "crafting": randint(0, 10),
            "deception": randint(0, 10),
            "diplomacy": randint(0, 10),
            "intimidation": randint(0, 10),
            "lore": randint(0, 10),
            "medicine": randint(0, 10),
            "nature": randint(0, 10),
            "occultism": randint(0, 10),
            "performance": randint(0, 10),
            "religion": randint(0, 10),
            "society": randint(0, 10),
            "stealth": randint(0, 10),
            "survival": randint(0, 10),
            "thievery": randint(0, 10),
        },
        "armor_class": randint(10, 30),
    }
