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

print("\033c", end="") # Tyhjentää terminaalin näkymän.

def tutorialMessage():
  print(f"       Varmista, että näet koko pelinäytön, mukaanlukien huoneen yläreunan.")
  print(f"       Valitse toiminto kirjoittamalla numero tai yksi kirjain.")
  print(f"       Esimerkiksi '1' tai 'x' ovat toimivia komentoja.")

def charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100):
  if charHunger > 100: # Tarkistaa onko Hunger yli 100
    charHunger = 100 # Palauttaa Hunger-arvon 100:aan mikäli se on yli 100
    charHungerMessage_100 = True # Tulostetaan viesti asiaan liittyen - samaan malliin seuraavissa if-lauseissa
#      print(f"       {charName} ei jaksa syödä enempää...")
  if charHunger < 0:
    charHunger = 0
    charHungerMessage_0 = True
#      print(f"       {charName} on nälkäinen...")
  if charEnergy > 100:
    charEnergy = 100
    charEnergyMessage_100 = True
#      print(f"       {charName} on nyt todella energinen! Hän ei malta maata enää sängyssä.")
  if charEnergy < 0:
    charEnergy = 0
    charEnergyMessage_0 = True
#      print(f"       {charName} alkaa olla melko väsynyt...")
  if charHealth > 100:
    charHealth = 100
    charHealthMessage_100 = True
#      print(f"       {charName} tuntee olevansa maailman tervein ihminen!")
  return(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)

def charStatCheck_Message(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth):
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
  return()

def gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP):
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
  return()

def gameInteractMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth, tutorialMessageCheck):
  print(f"""  |    Toiminnot:                                                   |
  |  |{color.DARKCYAN} 1. Syö         {color.END}|   |{color.DARKCYAN} 2. Nuku         {color.END}|   |{color.DARKCYAN} 3. Ympäristö   {color.END}|  |
  |  |{color.DARKCYAN} 4. Opiskele    {color.END}|   |{color.DARKCYAN} 5. Työskentele  {color.END}|   |{color.DARKCYAN} 6. Finanssit   {color.END}|  |
  |  |{color.DARKCYAN}                {color.END}|   |{color.DARKCYAN}                 {color.END}|   |{color.RED} x. Lopeta peli {color.END}|  |
  |_________________________________________________________________|""")

  charStatCheck_Message(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)

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

  if tutorialMessageCheck == False:
    tutorialMessage()
  gameInput = input(f"       Valitse toiminto: ")
  return(gameInput)

def gamePseudoMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth):
  print(f"""  |    Toiminnot:                                                   |
  |  |{color.DARKCYAN} 1. Syö         {color.END}|   |{color.DARKCYAN} 2. Nuku         {color.END}|   |{color.DARKCYAN} 3. Ympäristö   {color.END}|  |
  |  |{color.DARKCYAN} 4. Opiskele    {color.END}|   |{color.DARKCYAN} 5. Työskentele  {color.END}|   |{color.DARKCYAN} 6. Finanssit   {color.END}|  |
  |  |{color.DARKCYAN}                {color.END}|   |{color.DARKCYAN}                 {color.END}|   |{color.RED} x. Lopeta peli {color.END}|  |
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

  return()

def gameInteractMenu_1():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Syö:                                             |
  |  |{color.DARKCYAN} 1. Tee ruokaa kotona {color.END}                  |                     |
  |  |{color.DARKCYAN} 2. Käy syömässä opiskelijaravintolassa {color.END}|                     |
  |  |{color.DARKCYAN} 3. Tilaa ruoka kotiinkuljetuksena {color.END}     |    |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
        print("En ymmärtänyt komentoasi.")
        continue
    elif int(gameInput) > 0 and int(gameInput) <= 3:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue

"""
def gameInteractMenu_2():
  print(f"   _________________________________________________________________
  |    Toiminnot > Nuku:                                            |
  |  |{color.DARKCYAN} Kuinka monta tuntia? {color.END}|                                       |
  |  |{color.DARKCYAN} (Valitse 1 - 24)     {color.END}|                                       |
  |                                                |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
      print("En ymmärtänyt komentoasi.")
      continue
    elif int(gameInput) <= 24 and int(gameInput) > 0:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue
"""

def gameInteractMenu_3():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Ympäristö:                                       |
  |    {color.DARKCYAN}{charName}{color.END} asuu sijainnissa: {color.DARKCYAN}{charResidence}{color.END}                     |
  |    Vuokra on {color.DARKCYAN}{charResidence_Rent:.2f} €{color.END} kuukaudessa.                              |
  |  |{color.DARKCYAN} 1. Katso ulos ikkunasta {color.END}|                   |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
      print("En ymmärtänyt komentoasi.")
      continue
    elif int(gameInput) == 1:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue

def gameInteractMenu_4():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Opiskele:                                        |
  |  |{color.DARKCYAN} 1. Mene oppitunnille {color.END}    |                                   |
  |  |{color.DARKCYAN} 2. Osallistu etätunnille {color.END}|                                   |
  |  |{color.DARKCYAN} 3. Opiskele itsenäisesti {color.END}|                  |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
      print("En ymmärtänyt komentoasi.")
      continue
    elif int(gameInput) <= 3 and int(gameInput) > 0:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue

def gameInteractMenu_5():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Työskentele:                                     |
  |  |{color.DARKCYAN} 1. Työpaikkatiedot {color.END}|                                         |
  |  |{color.DARKCYAN} 2. Hae töitä {color.END}      |                                         |
  |  |{color.DARKCYAN} 3. Mene töihin {color.END}    |                        |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
      print("En ymmärtänyt komentoasi.")
      continue
    elif int(gameInput) <= 24 and int(gameInput) > 0:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue

def gameInteractMenu_6():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Finanssit:                                       |
  |  |{color.DARKCYAN} 1. Investoi osakkeisiin {color.END}       |                             |
  |  |{color.DARKCYAN} 2. Investoi kryptovaluuttoihin {color.END}|                             |
  |  |{color.DARKCYAN} 3. Lottoa {color.END}                     |            |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
      print("En ymmärtänyt komentoasi.")
      continue
    elif int(gameInput) <= 24 and int(gameInput) > 0:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue

def gameInteractMenu_SelectTime(gameInput_Chosen):
  gameInput_Chosen_Message = gameInput_Chosen_Messages(gameInput_Chosen)
  print(f"""   _________________________________________________________________
  |    Toiminnot > {gameInput_Chosen_Message} > Ajastin:{"|" : >{39 - len(gameInput_Chosen_Message)}}
  |  |{color.DARKCYAN} Kuinka monta tuntia? {color.END}|                                       |
  |  |{color.DARKCYAN} (Valitse 1 - 24)     {color.END}|                                       |
  |                                                |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")

  while True:
    gameInput = input(f"       Valitse toiminto: ")
    if gameInput.upper() == "X":
      return(gameInput)
    elif gameInput.isnumeric() == False:
      print("En ymmärtänyt komentoasi.")
      continue
    elif int(gameInput) <= 24 and int(gameInput) > 0:
      return(gameInput)
    else:
        print("En ymmärtänyt komentoasi.")
        continue

def gameInteractMenu_X():
  print(f"""   _________________________________________________________________
  |    Toiminnot > Lopeta peli:                                     |
  |    Haluatko varmasti lopettaa pelin? Pelissä ei (vielä) ole     |
  |    tallennusmekaniikkaa, joten menetät hahmosi! Jos haluat      |
  |    varmasti lopettaa pelin, kirjoita "{color.RED}exit{color.END}" ja paina Enter      |
  |    vahvistaaksesi päätöksesi.                                   |
  |                                                |{color.RED} x. Takaisin {color.END}|  |
  |_________________________________________________________________|""")
  gameInput = input(f"       Haluatko varmasti lopettaa pelin? ")
  return(gameInput)

def gameInput_Chosen_Messages(gameInput_Chosen):
  if gameInput_Chosen == "1":
    gameInput_Chosen = "Syö"
  elif gameInput_Chosen == "2":
    gameInput_Chosen = "Nuku"
  elif gameInput_Chosen == "3":
    gameInput_Chosen = "Ympäristö"
  elif gameInput_Chosen == "4":
    gameInput_Chosen = "Opiskele"
  elif gameInput_Chosen == "5":
    gameInput_Chosen = "Työskentele"
  elif gameInput_Chosen == "6":
    gameInput_Chosen = "Finanssit"
  return(gameInput_Chosen)

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
charResidence_Rent = 600.00

def mainGameplay(charHat, charHead, charLeftHand, charLeftArm, charTorso, charRightArm, charRightHand, charLeftLeg, charRightLeg, charName, charResidence, charResidence_Rent):
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
  charResidence_Rent = 600.00
  charMoney = 100.00 # Raha euroissa ja senteissä.
  charHealth = 100 # Hahmon terveys.
  charEnergy = 100 # Energiamittari, nousee kun hahmo nukkuu, kuluu kun hahmo tekee asioita.
  charHunger = 100 # Nälkämittari, nousee kun hahmo syö, kuluu kun hahmo tekee asioita.
  charOP = 0 # Opintopisteet. Näitä pitää saada jotta voittaa elämässä.

  tutorialMessageCheck = False

  # Pääsilmukka alkaa tästä
  while True:
    charHungerMessage_100 = False # Asetetaan viestit default-asetuksiin, eli ei tulosteta mitään
    charHungerMessage_0 = False
    charEnergyMessage_100 = False
    charEnergyMessage_0 = False
    charHealthMessage_100 = False
  #  charHealthMessage_0 = False

    gameHoursCounter = 0 # Palauttaa ajanlaskentamekaniikan oletusarvoille

    gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP) # Tulostetaan huone ja hahmon tilanne

    if charHealth <= 0: # Tarkistaa onko hahmo kuollut
      gameEnd_Fail_0Health() # Tulostetaan game over
      break # Lopettaa pelin
    elif charOP >= 210: # Tarkistaa onko hahmo saanut tarvittavan määrän opintopisteitä
      gameEnd_Win_210OP() # Tulostetaan voittonäkymä
      break # Lopettaa pelin
    else:
      gameInput = (gameInteractMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth, tutorialMessageCheck))

    tutorialMessageCheck = True

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
      elif gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun
      print("\033c", end="") # Tyhjentää terminaalin näkymän.    
      gameHours += 1

    elif gameInput == "2":
      gameInput_Chosen = gameInput
      gameInput_Chosen = gameInput_Chosen_Messages(gameInput_Chosen)
      gameInput = gameInteractMenu_SelectTime(gameInput_Chosen) # (Toiminnot > Nuku > Ajastin) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun
      print("\033c", end="") # Tyhjentää terminaalin näkymän.    
#      charEnergy += (int(gameInput) * 10)
      while gameHoursCounter < int(gameInput):
        gameHours += 1
        gameHoursCounter += 1
        charEnergy += 10
        charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100 = charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
        if gameHours == 24: # Tarkistaa onko kello 24
          gameHours = 0 # Palauttaa kellon arvon takaisin nollaan
          gameDays += 1 # 24 h = 1 day
        gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP)
        gamePseudoMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)
        print("\033c", end="") # Tyhjentää terminaalin näkymän.
        time.sleep(0.3)

    elif gameInput == "3":
      gameInput = gameInteractMenu_3() # (Toiminnot > Ympäristö) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun

    elif gameInput == "4":
      gameInput = gameInteractMenu_4() # (Toiminnot > Opiskele) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun

    elif gameInput == "5":
      gameInput = gameInteractMenu_5() # (Toiminnot > Työskentele) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun

    elif gameInput == "6":
      gameInput = gameInteractMenu_6() # (Toiminnot > Finanssit) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun

    elif gameInput.upper() == "X":
      gameInput = gameInteractMenu_X() # (Toiminnot > Lopeta peli) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun
      elif gameInput.upper() == "EXIT":
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        break

    else:
      print("\033c", end="") # Tyhjentää terminaalin näkymän.
      print("En ymmärtänyt komentoasi.")

    if gameHours == 24: # Tarkistaa onko kello 24
      gameHours = 0 # Palauttaa kellon arvon takaisin nollaan
      gameDays += 1 # 24 h = 1 day

mainGameplay(charHat, charHead, charLeftHand, charLeftArm, charTorso, charRightArm, charRightHand, charLeftLeg, charRightLeg, charName, charResidence, charResidence_Rent)