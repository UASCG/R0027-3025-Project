import time

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

def gameRoomAndStats():
  print(f"   _________________________________________________________________") # Tulostaa hahmon ja ympäristön
  print(f"""  |                                                   |             |
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
  |_________________________________________________________________|""")

  if gameHours >= 10: # Tarkistaa onko kellonaika 1 vai 2 merkin pituinen
    gameHoursDoubleDigits = "" # Poistaa ylimääräisen nollan
  else:
    gameHoursDoubleDigits = "0" # Lisää nollan kellonajan alkuun (00:00, ei 0:00)
  gameTimePrint = f"| Päivä {gameDays : <5}| {gameHoursDoubleDigits}{gameHours}:00 |"

  charHealthPrint = f"{charHealth}" # Tulostettava viesti joka perustuu charHealth-arvoon
  # Luvun väritys
  if charHealth > 75:
    charHealthPrint = f"{color.GREEN}{charHealth}{color.END}"
  elif charHealth > 25:
    charHealthPrint = f"{color.YELLOW}{charHealth}{color.END}"
  else:
    charHealthPrint = f"{color.RED}{charHealth}{color.END}"

  charEnergyPrint = f"{charEnergy}" # Tulostettava viesti joka perustuu charEnergy-arvoon
  # Luvun väritys
  if charEnergy > 75:
    charEnergyPrint = f"{color.GREEN}{charEnergy}{color.END}"
  elif charEnergy > 25:
    charEnergyPrint = f"{color.YELLOW}{charEnergy}{color.END}"
  else:
    charEnergyPrint = f"{color.RED}{charEnergy}{color.END}"

  charHungerPrint = f"{charHunger}" # Tulostettava viesti joka perustuu charHunger-arvoon
  # Luvun väritys
  if charHunger > 75:
    charHungerPrint = f"{color.GREEN}{charHunger}{color.END}"
  elif charHunger > 25:
    charHungerPrint = f"{color.YELLOW}{charHunger}{color.END}"
  else:
    charHungerPrint = f"{color.RED}{charHunger}{color.END}"

  # Tulostaa infolaatikon, jossa näkyy päivä, aika, ja hahmon tilanne
  infoSpace1 = (56 - len(charName)) # Määrittelee asettelun päivän ja kellonajan välillä
  infoSpace2 = (22 - len(str(f"{charMoney:.2f}"))) # Määrittelee asettelun rahalaatikolle
  infoSpace3 = (5 - len(str(charOP))) # Määrittelee asettelun opintopiste-viivalle
  print(f"""  |    {charName}{gameTimePrint : >{infoSpace1}} | | {"|" : >1}
  |  | Terveys: {charHealthPrint : >12} |     | Energia: {charEnergyPrint : >12} |{"|" : >27}
  |  |   Nälkä: {charHungerPrint : >12} |{"|" : >48}
  |{"|" : >66}
  |  |   Rahat: {color.GREEN}{charMoney:.2f} €{color.END} {infoSpace2 * " "}| Opintopisteet: {color.BLUE}{charOP} OP{color.END} {"|" : >{infoSpace3}}{"|" : >2}
  |_________________________________________________________________|""")

def gameInteractMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100):
  print(f"""  |    Toiminnot:                                                   |
  |  |{color.DARKCYAN} 1. Syö         {color.END}|   |{color.DARKCYAN} 2. Nuku         {color.END}|   |{color.DARKCYAN} 3. Ympäristö   {color.END}|  |
  |  |{color.DARKCYAN} 4. Opiskele    {color.END}|   |{color.DARKCYAN} 5. Työskentele  {color.END}|   |{color.DARKCYAN} 6. Finanssit   {color.END}|  |
  |  |{color.DARKCYAN} 7.             {color.END}|   |{color.DARKCYAN} 8.              {color.END}|   |{color.RED} 9. Lopeta peli {color.END}|  |
  |_________________________________________________________________|""")

  if charHungerMessage_100 == True:
    print(f"       {charName} ei jaksa syödä enempää...")
  if charHungerMessage_0 == True:
    print(f"       {charName} on nälkäinen...")
  if charEnergyMessage_100 == True:
    print(f"       {charName} on nyt todella energinen! Hän ei malta maata enää sängyssä.")
  if charEnergyMessage_0 == True:
    print(f"       {charName} alkaa olla melko väsynyt...")
  if charHealthMessage_100 == True:
    print(f"       {charName} tuntee olevansa maailman tervein ihminen!")
  if charHealth < 10:
    print(f"       {charName} ei voi hyvin...")

  gameInput = input(f"       Valitse toiminto: ")
  return(gameInput)

def gameInteractMenu_1():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Syö:                                             |
  |  |{color.DARKCYAN} 1. Tee ruokaa kotona {color.END}                  |                     |
  |  |{color.DARKCYAN} 2. Käy syömässä opiskelijaravintolassa {color.END}|                     |
  |  |{color.DARKCYAN} 3. Tilaa ruoka kotiinkuljetuksena {color.END}     |    |{color.RED} 9. Takaisin {color.END}|  |
  |_________________________________________________________________|""")
  gameInput = input(f"       Valitse toiminto: ")
  return(gameInput)

def gameEnd_Fail_0Health():
  print(f"""  |    Ded amen :(                                                  |
  |                                                                 |
  |                                                                 |
  |                                                                 |
  |_________________________________________________________________|""")

def gameEnd_Win_210OP():
  print(f"""  |    Hahmo valmistuu!!!1                                          |
  |                                                                 |
  |                                                                 |
  |                                                                 |
  |_________________________________________________________________|""")

# v Aloitusarvot v

gameHours = 9 # Kellonaika
gameDays = 0 # Päiviä aloituksen jälkeen

# Hahmon ulkonäkö koostuu näistä muuttujista
charHat = "n"
charHead = "o"
charLeftHand = "."
charLeftArm = "-"
charTorso = "I"
charRightArm = "-"
charRightHand = "."
charLeftLeg = "/"
charRightLeg = "\\"

charName = "John J. Smith" # Hahmon nimi

charJob = "" # Pelaajan hahmon työpaikka, aluksi NULL.
charResidence = "Myyrmäki" # Pelaajan hahmo asuu tässä sijainnissa.
charMoney = 100.00 # Raha euroissa ja senteissä.
charHealth = 100 # Hahmon terveys.
charEnergy = 100 # Energiamittari, nousee kun hahmo nukkuu, kuluu kun hahmo tekee asioita.
charHunger = 100 # Nälkämittari, nousee kun hahmo syö, kuluu kun hahmo tekee asioita.
charOP = 0 # Opintopisteet. Näitä pitää saada jotta voittaa elämässä.

# Pääsilmukka alkaa tästä
while True:
  charHungerMessage_100 = False # Asetetaan viestit default-asetuksiin, eli ei tulosteta mitään
  charHungerMessage_0 = False
  charEnergyMessage_100 = False
  charEnergyMessage_0 = False
  charHealthMessage_100 = False
#  charHealthMessage_0 = False
  if charHunger > 100: # Tarkistaa onko Hunger yli 100
    charHunger = 100 # Palauttaa Hunger-arvon 100:aan mikäli se on yli 100
    charHungerMessage_100 = True # Tulostetaan viesti asiaan liittyen - samaan malliin seuraavissa if-lauseissa
#      print(f"       {charName} ei jaksa syödä enempää...")
  if charHunger < 0:
    charHunger = 0
    charHungerMessage_0
#      print(f"       {charName} on nälkäinen...")
  if charEnergy > 100:
    charEnergy = 100
    charEnergyMessage_100
#      print(f"       {charName} on nyt todella energinen! Hän ei malta maata enää sängyssä.")
  if charEnergy < 0:
    charEnergy = 0
    charEnergyMessage_0
#      print(f"       {charName} alkaa olla melko väsynyt...")
  if charHealth > 100:
    charHealth = 100
    charHealthMessage_100
#      print(f"       {charName} tuntee olevansa maailman tervein ihminen!")

  gameRoomAndStats() # Tulostetaan huone ja hahmon tilanne

  if charHealth <= 0: # Tarkistaa onko hahmo kuollut
    gameEnd_Fail_0Health() # Tulostetaan game over
    break # Lopettaa pelin
  elif charOP >= 210: # Tarkistaa onko hahmo saanut tarvittavan määrän opintopisteitä
    gameEnd_Win_210OP() # Tulostetaan voittonäkymä
    break # Lopettaa pelin
  else:
    gameInput = (gameInteractMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100))

  if gameInput == "1":
    gameInput = gameInteractMenu_1() # (Toiminnot > Syö) valikko
    if gameInput == "1":
      charHunger += 50
      charMoney -= 5
      charEnergy -= 12
    elif gameInput == "2":
      charHunger += 50
      charMoney -= 2.10
      charEnergy -= 7
    elif gameInput == "3":
      charHunger += 50
      charMoney -= 17.50
      charEnergy -= 2
    elif gameInput == "9": # Takaisin edelliseen näkymään
      print("\033c", end="") # Tyhjentää terminaalin näkymän.    
      continue # Palaa silmukan alkuun
    print("\033c", end="") # Tyhjentää terminaalin näkymän.    
    gameHours += 1

  elif gameInput == "2":
    print("\033c", end="") # Tyhjentää terminaalin näkymän.
    charOP += 300  
  else:
    print("\033c", end="") # Tyhjentää terminaalin näkymän.
    print("En ymmärtänyt komentoasi.")

  if gameHours == 24: # Tarkistaa onko kello 24
    gameHours = 0 # Palauttaa kellon arvon takaisin nollaan
    gameDays += 1 # 24 h = 1 day