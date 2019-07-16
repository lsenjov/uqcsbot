from uqcsbot import bot, Command
from re import match
from typing import Optional

POKEDEX = {"bulbasaur": 1,
           "ivysaur": 2,
           "venusaur": 3,
           "charmander": 4,
           "charmeleon": 5,
           "charizard": 6,
           "squirtle": 7,
           "wartortle": 8,
           "blastoise": 9,
           "caterpie": 10,
           "metapod": 11,
           "butterfree": 12,
           "weedle": 13,
           "kakuna": 14,
           "beedrill": 15,
           "pidgey": 16,
           "pidgeotto": 17,
           "pidgeot": 18,
           "rattata": 19,
           "raticate": 20,
           "spearow": 21,
           "fearow": 22,
           "ekans": 23,
           "arbok": 24,
           "pikachu": 25,
           "raichu": 26,
           "sandshrew": 27,
           "sandslash": 28,
           "nidoran(f)": 29,
           "nidorina": 30,
           "nidoqueen": 31,
           "nidoran(m)": 32,
           "nidorino": 33,
           "nidoking": 34,
           "clefairy": 35,
           "clefable": 36,
           "vulpix": 37,
           "ninetales": 38,
           "jigglypuff": 39,
           "wigglytuff": 40,
           "zubat": 41,
           "golbat": 42,
           "oddish": 43,
           "gloom": 44,
           "vileplume": 45,
           "paras": 46,
           "parasect": 47,
           "venonat": 48,
           "venomoth": 49,
           "diglett": 50,
           "dugtrio": 51,
           "meowth": 52,
           "persian": 53,
           "psyduck": 54,
           "golduck": 55,
           "mankey": 56,
           "primeape": 57,
           "growlithe": 58,
           "arcanine": 59,
           "poliwag": 60,
           "poliwhirl": 61,
           "poliwrath": 62,
           "abra": 63,
           "kadabra": 64,
           "alakazam": 65,
           "machop": 66,
           "machoke": 67,
           "machamp": 68,
           "bellsprout": 69,
           "weepinbell": 70,
           "victreebel": 71,
           "tentacool": 72,
           "tentacruel": 73,
           "geodude": 74,
           "graveler": 75,
           "golem": 76,
           "ponyta": 77,
           "rapidash": 78,
           "slowpoke": 79,
           "slowbro": 80,
           "magnemite": 81,
           "magneton": 82,
           "farfetchd": 83,
           "doduo": 84,
           "dodrio": 85,
           "seel": 86,
           "dewgong": 87,
           "grimer": 88,
           "muk": 89,
           "shellder": 90,
           "cloyster": 91,
           "gastly": 92,
           "haunter": 93,
           "gengar": 94,
           "onix": 95,
           "drowzee": 96,
           "hypno": 97,
           "krabby": 98,
           "kingler": 99,
           "voltorb": 100,
           "electrode": 101,
           "exeggcute": 102,
           "exeggutor": 103,
           "cubone": 104,
           "marowak": 105,
           "hitmonlee": 106,
           "hitmonchan": 107,
           "lickitung": 108,
           "koffing": 109,
           "weezing": 110,
           "rhyhorn": 111,
           "rhydon": 112,
           "chansey": 113,
           "tangela": 114,
           "kangaskhan": 115,
           "horsea": 116,
           "seadra": 117,
           "goldeen": 118,
           "seaking": 119,
           "staryu": 120,
           "starmie": 121,
           "mr. mime": 122,
           "scyther": 123,
           "jynx": 124,
           "electabuzz": 125,
           "magmar": 126,
           "pinsir": 127,
           "tauros": 128,
           "magikarp": 129,
           "gyarados": 130,
           "lapras": 131,
           "ditto": 132,
           "eevee": 133,
           "vaporeon": 134,
           "jolteon": 135,
           "flareon": 136,
           "porygon": 137,
           "omanyte": 138,
           "omastar": 139,
           "kabuto": 140,
           "kabutops": 141,
           "aerodactyl": 142,
           "snorlax": 143,
           "articuno": 144,
           "zapdos": 145,
           "moltres": 146,
           "dratini": 147,
           "dragonair": 148,
           "dragonite": 149,
           "mewtwo": 150,
           "mew": 151}

PREFIX = {1: "Bulb",
          2: "Ivy",
          3: "Venu",
          4: "Char",
          5: "Char",
          6: "Char",
          7: "Squirt",
          8: "War",
          9: "Blast",
          10: "Cater",
          11: "Meta",
          12: "Butter",
          13: "Wee",
          14: "Kak",
          15: "Bee",
          16: "Pid",
          17: "Pidg",
          18: "Pidg",
          19: "Rat",
          20: "Rat",
          21: "Spear",
          22: "Fear",
          23: "Ek",
          24: "Arb",
          25: "Pika",
          26: "Rai",
          27: "Sand",
          28: "Sand",
          29: "Nido",
          30: "Nido",
          31: "Nido",
          32: "Nido",
          33: "Nido",
          34: "Nido",
          35: "Clef",
          36: "Clef",
          37: "Vul",
          38: "Nine",
          39: "Jiggly",
          40: "Wiggly",
          41: "Zu",
          42: "Gol",
          43: "Odd",
          44: "Gloo",
          45: "Vile",
          46: "Pa",
          47: "Para",
          48: "Veno",
          49: "Veno",
          50: "Dig",
          51: "Dug",
          52: "Meow",
          53: "Per",
          54: "Psy",
          55: "Gol",
          56: "Man",
          57: "Prime",
          58: "Grow",
          59: "Arca",
          60: "Poli",
          61: "Poli",
          62: "Poli",
          63: "Ab",
          64: "Kada",
          65: "Ala",
          66: "Ma",
          67: "Ma",
          68: "Ma",
          69: "Bell",
          70: "Weepin",
          71: "Victree",
          72: "Tenta",
          73: "Tenta",
          74: "Geo",
          75: "Grav",
          76: "Gol",
          77: "Pony",
          78: "Rapi",
          79: "Slow",
          80: "Slow",
          81: "Magne",
          82: "Magne",
          83: "Far",
          84: "Do",
          85: "Do",
          86: "See",
          87: "Dew",
          88: "Gri",
          89: "Mu",
          90: "Shell",
          91: "Cloy",
          92: "Gas",
          93: "Haunt",
          94: "Gen",
          95: "On",
          96: "Drow",
          97: "Hyp",
          98: "Krab",
          99: "King",
          100: "Volt",
          101: "Electr",
          102: "Exegg",
          103: "Exegg",
          104: "Cu",
          105: "Maro",
          106: "Hitmon",
          107: "Hitmon",
          108: "Licki",
          109: "Koff",
          110: "Wee",
          111: "Rhy",
          112: "Rhy",
          113: "Chan",
          114: "Tang",
          115: "Kangas",
          116: "Hors",
          117: "Sea",
          118: "Gold",
          119: "Sea",
          120: "Star",
          121: "Star",
          122: "Mr.",
          123: "Scy",
          124: "Jyn",
          125: "Electa",
          126: "Mag",
          127: "Pin",
          128: "Tau",
          129: "Magi",
          130: "Gyara",
          131: "Lap",
          132: "Dit",
          133: "Ee",
          134: "Vapor",
          135: "Jolt",
          136: "Flare",
          137: "Pory",
          138: "Oma",
          139: "Oma",
          140: "Kabu",
          141: "Kabu",
          142: "Aero",
          143: "Snor",
          144: "Artic",
          145: "Zap",
          146: "Molt",
          147: "Dra",
          148: "Dragon",
          149: "Dragon",
          150: "Mew",
          151: "Mew"}

SUFFIX = {1: "basaur",
          2: "ysaur",
          3: "usaur",
          4: "mander",
          5: "meleon",
          6: "izard",
          7: "tle",
          8: "tortle",
          9: "toise",
          10: "pie",
          11: "pod",
          12: "free",
          13: "dle",
          14: "una",
          15: "drill",
          16: "gey",
          17: "eotto",
          18: "eot",
          19: "tata",
          20: "icate",
          21: "row",
          22: "row",
          23: "kans",
          24: "bok",
          25: "chu",
          26: "chu",
          27: "shrew",
          28: "slash",
          29: "oran",
          30: "rina",
          31: "queen",
          32: "ran",
          33: "rino",
          34: "king",
          35: "fairy",
          36: "fable",
          37: "pix",
          38: "tales",
          39: "puff",
          40: "tuff",
          41: "bat",
          42: "bat",
          43: "ish",
          44: "oom",
          45: "plume",
          46: "ras",
          47: "sect",
          48: "nat",
          49: "moth",
          50: "lett",
          51: "trio",
          52: "th",
          53: "sian",
          54: "duck",
          55: "duck",
          56: "key",
          57: "ape",
          58: "lithe",
          59: "nine",
          60: "wag",
          61: "whirl",
          62: "wrath",
          63: "ra",
          64: "bra",
          65: "kazam",
          66: "chop",
          67: "choke",
          68: "champ",
          69: "sprout",
          70: "bell",
          71: "bell",
          72: "cool",
          73: "cruel",
          74: "dude",
          75: "eler",
          76: "em",
          77: "ta",
          78: "dash",
          79: "poke",
          80: "bro",
          81: "mite",
          82: "ton",
          83: "fetchd",
          84: "duo",
          85: "drio",
          86: "eel",
          87: "gong",
          88: "mer",
          89: "uk",
          90: "der",
          91: "ster",
          92: "tly",
          93: "ter",
          94: "gar",
          95: "ix",
          96: "zee",
          97: "no",
          98: "by",
          99: "ler",
          100: "orb",
          101: "ode",
          102: "cute",
          103: "utor",
          104: "bone",
          105: "wak",
          106: "lee",
          107: "chan",
          108: "tung",
          109: "fing",
          110: "zing",
          111: "horn",
          112: "don",
          113: "sey",
          114: "gela",
          115: "khan",
          116: "sea",
          117: "dra",
          118: "deen",
          119: "king",
          120: "yu",
          121: "mie",
          122: "mime",
          123: "ther",
          124: "nx",
          125: "buzz",
          126: "mar",
          127: "sir",
          128: "ros",
          129: "karp",
          130: "dos",
          131: "ras",
          132: "to",
          133: "vee",
          134: "eon",
          135: "eon",
          136: "eon",
          137: "gon",
          138: "nyte",
          139: "star",
          140: "to",
          141: "tops",
          142: "dactyl",
          143: "lax",
          144: "cuno",
          145: "dos",
          146: "tres",
          147: "tini",
          148: "nair",
          149: "nite",
          150: "two",
          151: "ew"}


def lookup(command: Command, arg: str) -> Optional[int]:
    """
    converts a string representing a pokemon's name or number to an integer
    """
    try:
        num = int(arg)
    except ValueError:
        if arg not in POKEDEX:
            bot.post_message(command.channel_id, f"Could Not Find Pokemon: {arg}")
            return None
        num = POKEDEX[arg]
    if num <= 0 or num > 151:
        bot.post_message(command.channel_id, f"Out of Range: {arg}")
        return None
    return num


@bot.on_command('pokemash')
def handle_pokemash(command: Command):
    """
    `!pokemash pokemon pokemon` - Returns the pokemash of the two Pokemon.
    Can use Pokemon names or Pokedex numbers (first gen only)
    """
    cmd = command.arg.lower()
    # checks for exactly two pokemon
    # mr. mime is the only pokemon with a space in it's name
    if not cmd or (cmd.count(" ") - cmd.count("mr. mime")) != 1:
        bot.post_message(command.channel_id, "Incorrect Number of Pokemon")
        return

    # two pokemon split
    arg_left, arg_right = match(r"(mr\. mime|\S+) (mr\. mime|\S+)", cmd).group(1, 2)

    num_left = lookup(command, arg_left)
    num_right = lookup(command, arg_right)
    if num_left is None or num_right is None:
        return

    bot.post_message(command.channel_id,
                     f"_{PREFIX[num_left]+SUFFIX[num_right]}_\n"
                     f"https://images.alexonsager.net/pokemon/fused/"
                     + f"{num_right}/{num_right}.{num_left}.png")