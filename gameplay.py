# Määrittelee värit
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\x1B[3m'
   BOLDITALIC = '\x1B[1;3m'
   UNDERLINE = '\033[4m'
   REVERSE = '\033[7m'
   END = '\033[0m'

gfxSun = f"{color.YELLOW}☼{color.END}" # Väritetty aurinko

print("\033c", end="") # Tyhjentää terminaalin näkymän.

gameHours = 9 # Kellonaika
gameDays = 0 # Päiviä aloituksen jälkeen

# Debug hahmoarvot
"""
charHat = "x"
charHead = "x"
charLeftHand = "x"
charLeftArm = "x"
charTorso = "x"
charRightArm = "x"
charRightHand = "x"
charLeftLeg = "x"
charRightLeg = "x"
"""

charHat = "n"
charHead = "o"
charLeftHand = "."
charLeftArm = "-"
charTorso = "I"
charRightArm = "-"
charRightHand = "."
charLeftLeg = "/"
charRightLeg = "\\"

charName = "Pasi V.K. Mattinen"

charJob = "" # Pelaajan hahmon työpaikka, aluksi NULL.
charResidence = "Myyrmäki" # Pelaajan hahmo asuu tässä sijainnissa.
charMoney = 100.00 # Raha euroissa ja senteissä.
charHealth = 100 # Hahmon terveys.
charEnergy = 100 # Energiamittari, nousee kun hahmo nukkuu, kuluu kun hahmo tekee asioita.
charHunger = 100 # Nälkämittari, nousee kun hahmo syö, kuluu kun hahmo tekee asioita.
charOP = 0 # Opintopisteet. Näitä pitää saada jotta voittaa elämässä.

charKarma = 100 # Toimintoa ei olla toteutettu vielä.

print("")

# Debug valuetest
print(f"gameHours: {gameHours}")
print(f"gameDays: {gameDays}")

print(f"charJob: {charJob}")
print(f"charResidence: {charResidence}")
print(f"charMoney: {charMoney:.2f}")
print(f"charHealth: {charHealth}")
print(f"charEnergy: {charEnergy}")
print(f"charHunger: {charHunger}")
print(f"charOP: {charOP}")

print(f"charKarma: {charKarma}")

print(f" _________________________________________________________________") # Tulostaa hahmon ja ympäristön
print(f"""|                                                   |             |
|                                 ____________      |             |
|                                ||    ||  `O||     |             |
|                                ||    ||  ´ ||     |             |
|                                ||____||____||     |             |
|                                                ___()            |
|                                ()_____________(\__\\\()          |
|                                ||\() \_\ \_\ \_(___)||          |
|________________________________||\|| |_| |_| |_|____||          |
|                                   || |_| |_| |_|    ||          |
|                                                       `.        |
|          {charHat}                                              `.      |
|          {charHead}                                                `.    |
|        {charLeftHand}{charLeftArm}{charTorso}{charRightArm}{charRightHand}                                                `.  |
|         {charLeftLeg} {charRightLeg}                                                   `.|
 _________________________________________________________________""")

if gameHours >= 10: # Tarkistaa onko kellonaika 1 vai 2 merkin pituinen
  gameHoursDoubleDigits = "" # Poistaa ylimääräisen nollan
else:
  gameHoursDoubleDigits = "0" # Lisää nollan kellonajan alkuun (00:00, ei 0:00)
gameTimePrint = f"Päivä {gameDays}, {gameHoursDoubleDigits}{gameHours}:00."

charHealthPrint = f"Terveys: {charHealth}" # Tulostettava viesti joka perustuu charHealth-arvoon
# Luvun väritys
if charHealth > 75:
  charHealthPrint = f"Terveys: {color.GREEN}{charHealth}{color.END}"
elif charHealth > 25:
  charHealthPrint = f"Terveys: {color.YELLOW}{charHealth}{color.END}"
else:
  charHealthPrint = f"Terveys: {color.RED}{charHealth}{color.END}"

charEnergyPrint = f"Energia: {charEnergy}" # Tulostettava viesti joka perustuu charEnergy-arvoon
# Luvun väritys
if charEnergy > 75:
  charEnergyPrint = f"Energia: {color.GREEN}{charEnergy}{color.END}"
elif charEnergy > 25:
  charEnergyPrint = f"Energia: {color.YELLOW}{charEnergy}{color.END}"
else:
  charEnergyPrint = f"Energia: {color.RED}{charEnergy}{color.END}"

charHungerPrint = f"Nälkä: {charHunger}" # Tulostettava viesti joka perustuu charHunger-arvoon
# Luvun väritys
if charHunger > 75:
  charHungerPrint = f"Nälkä: {color.GREEN}{charHunger}{color.END}"
elif charHunger > 25:
  charHungerPrint = f"Nälkä: {color.YELLOW}{charHunger}{color.END}"
else:
  charHungerPrint = f"Nälkä: {color.RED}{charHunger}{color.END}"

# Tulostaa infolaatikon, jossa näkyy päivä, aika, ja hahmon tilanne
print(f""" _________________________________________________________________
| {charName : >25}              {gameTimePrint : ^25}{"|" : <32}
| {charHealthPrint : >25} {charEnergyPrint : >25}{"|" : >32}
| {charHungerPrint : >25}|
||
| Rahat: {charMoney:.2f} €|
| Opintopisteet: {charOP} OP|
|_________________________________________________________________|
""")

# INFOBOX TEMP TEST 1 /////////////////////////////////////////
gameHours = 23
gameDays = 9999
charName = "Todellapitkäetunimi Tosipitkäsukunimi"
charMoney = 1000000000.00
charHealth = 100
charEnergy = 100
charHunger = 100
charOP = 209

if gameHours >= 10: # Tarkistaa onko kellonaika 1 vai 2 merkin pituinen
  gameHoursDoubleDigits = "" # Poistaa ylimääräisen nollan
else:
  gameHoursDoubleDigits = "0" # Lisää nollan kellonajan alkuun (00:00, ei 0:00)
gameTimePrint = f"Päivä {gameDays}, {gameHoursDoubleDigits}{gameHours}:00."

print(f""" _________________________________________________________________
| {charName : >25}              {gameTimePrint : ^25}{"|" : <32}
| {charHealthPrint : >25} {charEnergyPrint : >25}{"|" : >32}
| {charHungerPrint : >25}|
||
| Rahat: {charMoney:.2f} €|
| Opintopisteet: {charOP} OP|
|_________________________________________________________________|
""")

# INFOBOX TEMP TEST 2
print(f""" _________________________________________________________________
| {charName : >25}              {gameTimePrint : ^25}{"|" : <32}
| {charHealthPrint : >25} {charEnergyPrint : >25}{"|" : >32}
| {charHungerPrint : >25}|
||
| Rahat: {charMoney:.2f} €|
| Opintopisteet: {charOP} OP|
|_________________________________________________________________|
""")

gameHours = 0
gameDays = 0
charName = "X"
charMoney = 0.00
charHealth = 0
charEnergy = 0
charHunger = 0
charOP = 0

if gameHours >= 10: # Tarkistaa onko kellonaika 1 vai 2 merkin pituinen
  gameHoursDoubleDigits = "" # Poistaa ylimääräisen nollan
else:
  gameHoursDoubleDigits = "0" # Lisää nollan kellonajan alkuun (00:00, ei 0:00)
gameTimePrint = f"Päivä {gameDays}, {gameHoursDoubleDigits}{gameHours}:00."

print(f""" _________________________________________________________________
| {charName : >25}              {gameTimePrint : ^25}{"|" : <32}
| {charHealthPrint : >25} {charEnergyPrint : >25}{"|" : >32}
| {charHungerPrint : >25}|
||
| Rahat: {charMoney:.2f} €|
| Opintopisteet: {charOP} OP|
|_________________________________________________________________|
""")

# INFOBOX TEMP TEST END /////////////////////////////////////////

if charHealth <= 0:
  print(f"Ded amen :(")
elif charOP >= 210:
  print(f"Hahmo valmistuu!!!1")
else:
  print(f"Valitse toiminto:")