# Koodi yhdistetään tähän tiedostoon.

# logo ja välkkyvä epilepsia-intro
import time

from os import system, name
# importoidaan sleep joka pitää printtauksen tietyn ajan ruudulla.
from time import sleep

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

def nayta_logo():
    logo = r'''
                        ::::::::::: :::    ::: :::::::::: 
                           :+:     :+:    :+: :+:         
                          +:+     +:+    +:+ +:+          
                         +#+     +#++:++#++ +#++:++#      
                        +#+     +#+    +#+ +#+            
                       #+#     #+#    #+# #+#             
                      ###     ###    ### ##########       
                   :::        :::::::::::   :::   :::    :::::::: 
                  :+:            :+:      :+:+: :+:+:  :+:    :+: 
                 +:+            +:+     +:+ +:+:+ +:+ +:+         
                +#+            +#+     +#+  +:+  +#+ +#++:++#++   
               +#+            +#+     +#+       +#+        +#+    
              #+#            #+#     #+#       #+# #+#    #+#     
             ########## ########### ###       ###  ########        
    '''

# epilepsia-intro jatkuu
    print("\033c", end="")

    for offset in range(1, 25):
        print("\033c", end="")  
        print(" " * offset + logo)
        time.sleep(0.1)

    for _ in range(3):
        print("\033c", end="")  
        print(logo)
        time.sleep(0.5)
        print("\033c", end="")
        time.sleep(0.5)

# päävalikko
def nayta_main_menu():
    print("""                        ::::::::::: :::    ::: :::::::::: 
                           :+:     :+:    :+: :+:         
                          +:+     +:+    +:+ +:+          
                         +#+     +#++:++#++ +#++:++#      
                        +#+     +#+    +#+ +#+            
                       #+#     #+#    #+# #+#             
                      ###     ###    ### ##########       
                   :::        :::::::::::   :::   :::    :::::::: 
                  :+:            :+:      :+:+: :+:+:  :+:    :+: 
                 +:+            +:+     +:+ +:+:+ +:+ +:+         
                +#+            +#+     +#+  +:+  +#+ +#++:++#++   
               +#+            +#+     +#+       +#+        +#+    
              #+#            #+#     #+#       #+# #+#    #+#     
             ########## ########### ###       ###  ########       
     
       """)
    print("""
                       *****************************
                       * Opiskeluelämäsimulaattori *
                       *****************************
    """)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │                          1. Aloita                              │
    ├─────────────────────────────────────────────────────────────────┤
    │                          2. Info                                │
    ├─────────────────────────────────────────────────────────────────┤
    │                          3. Credits                             │
    ├─────────────────────────────────────────────────────────────────┤
    │                          4. Lopeta                              │
    └─────────────────────────────────────────────────────────────────┘
    """)

nayta_logo()

# info
def nayta_info():
    print(""" 
    ┌─────────────────────────────────────────────────────────────────┐
    │                            Info                                 │
    │                           ******                                │
    │                                                                 │
    │  Opiskeluelämäsimulaattori The Lims™ on simulaatiopeli, jossa   │ 
    │  tarkoituksenasi on luoda oma opiskelijahahmo. Tehtävänäsi on   │
    │  auttaa hahmoasi selviämään opinnoistaan ja keräämään tarvit-   │
    │  tava määrä opintopisteitä valmistumista varten.                │
    │                                                                 │
    │  Pelissä voit valita eri toimintoja, jotka vaikuttavat hahmosi  │
    │  tarpeisiin, rahatilanteeseen sekä opintopisteisiin. Päämäärä-  │                                                           
    │  nä on pitää opiskelija hengissä tämän valmistumiseen saakka.   │
    │                                                                 │
    │                                                                 │
    │                                   zzzzz  |\      _,,,--,,_      │
    │                                          /,`.-'`'   ._  \-;;,_  │
    │                                         |,4-  ) )_   .;.(  `'-' │
    │                                        '---''(_/._)-'(_\_)      │
    └─────────────────────────────────────────────────────────────────┘
    """)
    input("                 Paina Enter palataksesi päävalikkoon.")
    print("\033c", end="") # Tyhjentää terminaalin näkymän.    

# kunnia keille se kuuluu, credits-sivu
def nayta_credits():
    print(""" 
    ┌─────────────────────────────────────────────────────────────────┐
    │                           Credits                               │
    │                           *******                               │
    │                                                                 │
    │   Logo by Text to ASCII Art Generator (patorjk)                 │
    │   https://patorjk.com/software/taag/                            │
    │                                                                 │
    │   Bed by Joan G. Stark (jgs)                                    │
    │   https://www.asciiart.eu/buildings-and-places/furniture/other  │
    │                                                                 │
    │   SSt/JaWa                                                      │
    │   https://ascii.co.uk/art/rooms                                 │
    │                                                                 │
    │   Frame inspiration                                             │
    │   https://stonestoryrpg.com/                                    │
    │                                                                 │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘    
    """)
    input("                 Paina Enter palataksesi päävalikkoon.")
    print("\033c", end="") # Tyhjentää terminaalin näkymän.    

def clear():
 #määrittää clearfunktion toiminaallisuuden
	if name == 'nt':
		_ = system('cls')

	else:
		_ = system('clear')
clear()                           

charName= ""
charHat = ""
charHead = "o"
charLeftHand = "."
charLeftArm = "-"
charTorso = "I"
charRightArm = "-"
charRightHand = "."
charLeftLeg = "/"
charRightLeg = "\\"

def teksti1():

  print(f" _                   .                     _") 
  print(f"(__________________´   `____________________)")
  print(".                                           .")
  print (f".           Tervetuloa Limssin \t            .\n. \t  ihmeelliseen maailmaan!           . ")
  print(".                                           .")
  print(f" _________________       ___________________")
  print(f"(_                 ` . ´                    _)")

def teksti2():
  varip = "\033[91mupeimmat puolet. \033[0m"
  print(f" _                   .                     _") 
  print(f"(__________________´   `____________________)")
  print(".                                           .")
  print (f".           Täällä pääset kokemaan  \t    .\n.      opiskelijaelämän {varip}   . ")
  print(".                                           .")
  print(f" _________________       ___________________")
  print(f"(_                 ` . ´                    _)")

def teksti3():
  print(f" _                   .                     _") 
  print(f"(__________________´   `____________________)")
  print(".                                           .")
  print (f".      Aloitetaan luomalla sinulle keho     .\n.         joka kuljettaa sinut läpi         . ")
  print(".           tulevien haasteiden.            .")
  print(f" _________________       ___________________")
  print(f"(_                 ` . ´                    _)")

def valitsehattu():
    global charHat 
    while True: #printataan vaihtoehdot
        valintahattu = input(f"""Valitse hatun numero. (1-16)
        ______    ______    ______    _______  ______    ______   ______    ______
       |1.    |  |2.    |  |3.    |  |4.    | |5.    |  |6.    | |7.    |  |8.    | 
       |  U   |  |  Δ   |  |  P   |  |  Q   | |  #   |  |  Д   | |  の  |  |   Ψ  |
       |______|  |______|  |______|  |______| |______|  |______| |______|  |______|
        ______    ______    ______    _______  ______    ______   ______    ______
       |9.    |  |10.   |  |11.   |  |12.   | |13.   |  |14.   | |15.   |  |16.   |
       |  Б   |  |  Ω   |  |  Ж   |  |  Ѫ   | |  П   |  |  Ѧ   | |  Л   |  |  个  |
       |______|  |______|  |______|  |______| |______|  |______| |______|  |______|
        
         
        """)

        if valintahattu.isdigit():  # Tarkistetaan, että syöte on numero
            numero = int(valintahattu)
            if 1 <= numero <= 16:  # Tarkistetaan, että numero on välillä 1-16
                # Muutetaan charHat-arvoa käskyn mukaan
                if numero == 1:
                    charHat = "U"
                elif numero == 2:
                    charHat = "Δ"   
                elif numero == 3:
                    charHat = "P"
                elif numero == 4:
                    charHat = "Q"
                elif numero == 5:
                    charHat = "#"
                elif numero == 6:
                    charHat = "Д"
                elif numero == 7:
                    charHat = "の"
                elif numero == 8:
                    charHat = "Ψ"
                elif numero == 9:
                    charHat = "Б"
                elif numero == 10:
                    charHat = "Ω"
                elif numero == 11:
                    charHat = "Ж"
                elif numero == 12:
                    charHat = "Ѫ"
                elif numero == 13:
                    charHat = "П"
                elif numero == 14:
                    charHat = "Ѧ"
                elif numero == 15:
                    charHat = "Л"
                elif numero == 16:
                    charHat = "个"          
                
                while True:
                    clear()
                    vahvistus = input(f"""Olet valinnut numeron {valintahattu}. 
                                       
       {charHat}                                                    
       {charHead}                                                    
     {charLeftHand}{charLeftArm}{charTorso}{charRightArm}{charRightHand}                                                
      {charLeftLeg} {charRightLeg} 
      
      Oletko varma? (Y/N): """)
                    
  
                    if vahvistus.upper() == "Y":
                        clear()
                        return charHat  # Palautetaan ohjelman suoritus takaisin pääohjelmaan

                    elif vahvistus.upper() == "N":
                        break  # Palataan takaisin kysymään syötettä 1-16
                    else:
                        print("Syötä 'Y' tai 'N'!")
            else:
                print("Syötä numero väliltä 1-16!")
                input("Paina Enter jatkaaksesi...")
        else:
            print("Syötä numero väliltä 1-16!")
            input("Paina Enter jatkaaksesi...")     

def readycheck(): #kun käyttäjä valitsee hahmovalikosta vaihtoehdon 4, readycheck tarkistaa onko hahmolla nimeä, jos ei niin readycheckin suorittaminen päättyy 
  #palataan takaisin hahmovalikkoon.
  while True:
    if charName != "":
      print(f"""
       {charHat}                                                    
       {charHead}                                                    
     {charLeftHand}{charLeftArm}{charTorso}{charRightArm}{charRightHand}                                                
      {charLeftLeg} {charRightLeg} 

    Nimesi: {charName}\n""")
      
      readycheck1 = input("Oletko tyytyväinen muokkaukseen? Y/N ? ")
      if readycheck1.upper() == "Y":
        clear()
        print(f""" _                   .                     _
(__________________´   `____________________)
.                                           .
.           Customisointi valmis!           . 
.                                           .
 _________________       ___________________
(_                 ` . ´                   _)
              """)
        sleep(3)
        clear()
        print(f""" _                   .                     _
(__________________´   `____________________)
.                                           .
.               Olet valmis                 . 
.            aloittamaan matkasi!           .
._________________       ___________________.
(_                 ` . ´                   _)
              """) 
        sleep(3)
        clear()
        break #readycheck poistaa meidät hahmo-menusta ja jatkaa koodin suorittamista
      elif readycheck1.upper() == "N":
          hahmomenu()
      else:
          "Valitse joko Y/N "
          input("Paina Enter jatkaaksesi...")
    else:
      print("Valitse ensin itsellesi nimi jatkaaksesi")
      input("Paina Enter jatkaaksesi...")
      hahmomenu()
  
def hahmomenu():
  while True: #menu pysyy näkyvillä niin kauan kunnes käyttäjä valitsee toiminnan joka vie funktiosuoritukseen
    print(f"""
                
                    {charHat}                                                    
                    {charHead}                                                    
                  {charLeftHand}{charLeftArm}{charTorso}{charRightArm}{charRightHand}                                                
                   {charLeftLeg} {charRightLeg} 

                Nimesi: {charName}\n""")

    print("Voitko aloittaa hahmon muokkaamisen valitsemalla komennon 1-3: ")

    print(f"""          ___________________________
         |                           |
         | 1.Valitse hahmollesi nimi |
         |___________________________|""")
    print(f"""          ___________________________
         |                           |
         |2.Valitse hahmollesi hattu |
         |___________________________| """)
    print(f"""          ___________________________
         |                           |
         |3.Valitse hahmollesi värit |
         |___________________________| """)
    print(f"""          ___________________________
         |                           |
         |        4.Valmis           |
         |___________________________| \n""")
  
    valinta = input("Syötä valinta: ")

    if valinta == "2":
      valitsehattu()

    elif valinta == "1":
      valitsenimi()
    elif valinta == "3":
      print("\033[93mUPCOMING DLC!!!!!!1 :OO \033[0m")
      input("Paina Enter")
      clear()
      
      #tähän ei riittänyt aika

    elif valinta == "4":
        readycheck()
        break
    else:
      print("Virheellinen valinta. Valitse toiminto 1-4.")
      input("Paina Enter jatkaaksesi...")

def valitsenimi():
    clear()
    global charName
    while True:
        nimi = input("Syötä merkkijono (1-33 merkkiä): ")
        if 1 <= len(nimi) <= 33:  # Tarkistetaan merkkijonon pituus
            charName = nimi
            print(f"Syötit merkkijonon: {charName}")
            while True:
                vahvistus = input("Oletko varma? (Y/N): ")
                if vahvistus.upper() == "Y":
                    clear()
                    return  # Palautetaan ohjelman suoritus takaisin pääohjelmaan
                elif vahvistus.upper() == "N":
                    break  # Palataan takaisin kysymään uutta syötettä
                else:
                    print("Syötä 'Y' tai 'N'!")
                    input("Paina Enter jatkaaksesi...")
        else:
            print("Syötä merkkijono, jonka pituus on 1-33 merkkiä!")
            input("Paina Enter jatkaaksesi...")

def mainCharacterCreator():
    teksti1()
    sleep(3)
    clear()

    teksti2()
    sleep(3)
    clear()

    teksti3()
    sleep(3)
    clear()

    print("Tässä olet sinä.")

    print(f""" 
                         o
                       .-I-.
                        / \ \n""") 



    sleep(3)
    clear()
    print(f" _                   .                     _") 
    print(f"(__________________´   `____________________)")
    print(f".                                           .")
    print(f".             Aika surullisen               .")
    print(f".             näköinen kaveri.              .")
    print(f".                                           .")
    print(f" _________________       ___________________")
    print(f"(_                 ` . ´                    _)")
    sleep(3)
    clear()

    #sleep(3) ja clear toistot rytmittävät animaatiota

    print(f" _                   .                     _") 
    print(f"(__________________´   `____________________)")
    print(f".                                           .")
    print(f".        Nimi, hattu ja värit voisivat      .")
    print(f".           tehdä hänelle hyvää.            .")
    print(f".                                           .")
    print(f" _________________       ___________________")
    print(f"(_                 ` . ´                    _)")

    sleep(3)
    clear()

    hahmomenu()
    #readycheck palauttaa tänne

#    print("Oma osuus päättyy! Jeee hyvä sinä!\n")

print("\033c", end="") # Tyhjentää terminaalin näkymän.

# gameplay.py alkaa tästä

def tutorialMessage():
  print(f"       Varmista, että näet koko pelinäytön, mukaanlukien huoneen yläreunan.")
  print(f"       Valitse toiminto kirjoittamalla numero tai yksi kirjain.")
  print(f"       Esimerkiksi '1' tai 'x' ovat toimivia komentoja.")

def charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100):
  if charHunger > 100: # Tarkistaa onko Hunger yli 100
    charHunger = 100 # Palauttaa Hunger-arvon 100:aan mikäli se on yli 100
    charHealth += 1 # Palauttaa Healthia mikäli Health on alle 100
    charHungerMessage_100 = True # Tulostetaan viesti asiaan liittyen - samaan malliin seuraavissa if-lauseissa
#      print(f"       {charName} ei jaksa syödä enempää...")
  if charHunger < 0:
    charHunger = 0
    charHealth -= 1 # Hahmo alkaa kuolla nälkään
    charHungerMessage_0 = True
#      print(f"       {charName} on nälkäinen...")
  if charEnergy > 100:
    charEnergy = 100
    charHealth += 1
    charEnergyMessage_100 = True
#      print(f"       {charName} on nyt todella energinen! Hän ei malta maata enää sängyssä.")
  if charEnergy < 0:
    charEnergy = 0
    charHealth -= 1 # Hahmo on niin väsynyt että sattuu
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

def gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100):
  print(f"   _________________________________________________________________") # Tulostaa hahmon ja ympäristön
  if gameHours >= 9 and gameHours <= 21:
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
  else:
        print(f"""  |                                                   |             |
  |                                 ____________      |             |
  |                                ||    ||   ☽||     |             |
  |                                ||    ||    ||     |             |
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

#  if charHungerMessage_100 == True:
#    print(f"       {charName} ei jaksa syödä enempää...")
#  if charHungerMessage_0 == True:
#    print(f"       {charName} on nälkäinen...")
#  if charEnergyMessage_100 == True:
#    print(f"       {charName} on nyt todella energinen! Hän ei malta maata enää sängyssä.")
#  if charEnergyMessage_0 == True:
#    print(f"       {charName} alkaa olla melko väsynyt...")
#  if charHealthMessage_100 == True:
#    print(f"       {charName} tuntee olevansa maailman tervein ihminen!")
#  if charHealth < 10:
#    print(f"       {charName} ei voi hyvin...")

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

#  charStatCheck_Message(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)

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


def gameInteractMenu_1(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100):
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
  time.sleep(3)
  print("\033c", end="") # Tyhjentää terminaalin näkymän.    
  print(f"""  |                                                                 |
  |                            .---.                                |
  |                            |   |                                |           
  |                         ___|   |___                             | 
  |                        [           ]                            |
  |                        ---.   .---'                            |
  |                            |   |                                |
  |                            |   |                                | 
  |                            |   |                                |
  |                         .-|   |-,                             |
  |                     .-"   "'   "-.                         |
  |                   .'                   '.                       |
  |                                                                 |
  |                                                                 |
  |_________________________________________________________________|""")
  input("                 Paina Enter palataksesi päävalikkoon.")
  print("\033c", end="") # Tyhjentää terminaalin näkymän.  

def gameEnd_Win_210OP():
  print(f"""  |    Hahmo valmistuu!!!1                                          |
  |                                                                 |
  |                                                                 |
  |                                                                 |
  |_________________________________________________________________|""")
  input("                 Paina Enter palataksesi päävalikkoon.")
  print("\033c", end="") # Tyhjentää terminaalin näkymän.  

# v Aloitusarvot v

# charHat = "n"
# charHead = "o"
# charLeftHand = "."
# charLeftArm = "-"
# charTorso = "I"
# charRightArm = "-"
# charRightHand = "."
# charLeftLeg = "/"
# charRightLeg = "\\"

# charName = "John J. Smith" # Hahmon nimi

charJob = "" # Pelaajan hahmon työpaikka, aluksi NULL.
charResidence = "Myyrmäki" # Pelaajan hahmo asuu tässä sijainnissa.
charResidence_Rent = 600.00

def mainGameplay(charHat, charHead, charLeftHand, charLeftArm, charTorso, charRightArm, charRightHand, charLeftLeg, charRightLeg, charName, charResidence, charResidence_Rent):
  gameHours = 9 # Kellonaika
  gameDays = 0 # Päiviä aloituksen jälkeen

  # Hahmon ulkonäkö koostuu näistä muuttujista
#  charHat = "n"
#  charHead = "o"
#  charLeftHand = "."
#  charLeftArm = "-"
#  charTorso = "I"
#  charRightArm = "-"
#  charRightHand = "."
#  charLeftLeg = "/"
#  charRightLeg = "\\"

#  charName = "John J. Smith" # Hahmon nimi

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

    gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100) # Tulostetaan huone ja hahmon tilanne

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
      gameInput = gameInteractMenu_1(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100) # (Toiminnot > Syö) valikko
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
      charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100 = charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
      charStatCheck_Message(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)
      time.sleep(1)
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
        gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
        gamePseudoMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)
        print("\033c", end="") # Tyhjentää terminaalin näkymän.
        time.sleep(0.3)

    elif gameInput == "3":
      gameInput = gameInteractMenu_3() # (Toiminnot > Ympäristö) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        continue # Palaa silmukan alkuun

    elif gameInput == "4":
      gameInput_Chosen = gameInput
      gameInput_Chosen = gameInput_Chosen_Messages(gameInput_Chosen)
      gameInput = gameInteractMenu_4() # (Toiminnot > Opiskele) valikko
      if gameInput.upper() == "X": # Takaisin edelliseen näkymään
        print("\033c", end="") # Tyhjentää terminaalin näkymän.
        continue # Palaa silmukan alkuun

      if gameInput == "1": # Mene oppitunnille
        gameInput = gameInteractMenu_SelectTime(gameInput_Chosen) # (Toiminnot > Opiskele > Ajastin) valikko
        if gameInput.upper() == "X": # Takaisin edelliseen näkymään
          print("\033c", end="") # Tyhjentää terminaalin näkymän.    
          continue # Palaa silmukan alkuun
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        while gameHoursCounter < int(gameInput):
          gameHours += 1
          gameHoursCounter += 1
          charHunger -= 5
          charOP += 1
          charEnergy -= 12
          charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100 = charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
          if gameHours == 24: # Tarkistaa onko kello 24
            gameHours = 0 # Palauttaa kellon arvon takaisin nollaan
            gameDays += 1 # 24 h = 1 day
          gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
          gamePseudoMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)
          print("\033c", end="") # Tyhjentää terminaalin näkymän.
          time.sleep(0.3)

      if gameInput == "2": # Osallistu etätunnille
        gameInput = gameInteractMenu_SelectTime(gameInput_Chosen) # (Toiminnot > Opiskele > Ajastin) valikko
        if gameInput.upper() == "X": # Takaisin edelliseen näkymään
          print("\033c", end="") # Tyhjentää terminaalin näkymän.    
          continue # Palaa silmukan alkuun
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        while gameHoursCounter < int(gameInput):
          gameHours += 1
          gameHoursCounter += 1
          charHunger -= 5
          charOP += 1
          charEnergy -= 10
          charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100 = charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
          if gameHours == 24: # Tarkistaa onko kello 24
            gameHours = 0 # Palauttaa kellon arvon takaisin nollaan
            gameDays += 1 # 24 h = 1 day
          gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
          gamePseudoMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)
          print("\033c", end="") # Tyhjentää terminaalin näkymän.
          time.sleep(0.3)

      if gameInput == "3": # Opiskele itsenäisesti
        gameInput = gameInteractMenu_SelectTime(gameInput_Chosen) # (Toiminnot > Opiskele > Ajastin) valikko
        if gameInput.upper() == "X": # Takaisin edelliseen näkymään
          print("\033c", end="") # Tyhjentää terminaalin näkymän.    
          continue # Palaa silmukan alkuun
        print("\033c", end="") # Tyhjentää terminaalin näkymän.    
        while gameHoursCounter < int(gameInput):
          gameHours += 1
          gameHoursCounter += 1
          charHunger -= 5
          charOP += 1
          charEnergy -= 10
          charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100 = charStatCheck(charHunger, charEnergy, charHealth, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
          if gameHours == 24: # Tarkistaa onko kello 24
            gameHours = 0 # Palauttaa kellon arvon takaisin nollaan
            gameDays += 1 # 24 h = 1 day
          gameRoomAndStats(gameHours, gameDays, charHealth, charEnergy, charHunger, charMoney, charOP, charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100)
          gamePseudoMenu(charHungerMessage_100, charHungerMessage_0, charEnergyMessage_100, charEnergyMessage_0, charHealthMessage_100, charHealth)
          print("\033c", end="") # Tyhjentää terminaalin näkymän.
          time.sleep(0.3)

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

# gameplay.py loppuu tähän

# päävalikon toiminnot, looppi
     
while True:
    nayta_main_menu()
    valinta = input("                     Valitse toiminto (1-4): ")

    if valinta == "1":
        print("\033c", end="")
        mainCharacterCreator()
        mainGameplay(charHat, charHead, charLeftHand, charLeftArm, charTorso, charRightArm, charRightHand, charLeftLeg, charRightLeg, charName, charResidence, charResidence_Rent)
        # PELI
    elif valinta == "2":
        print("\033c", end="")
        nayta_info()
    elif valinta == "3":
        print("\033c", end="")
        nayta_credits()
    elif valinta == "4":
        print("                     Kiitos pelaamisesta! Moikkuli.")
        break
    else:
        print()
