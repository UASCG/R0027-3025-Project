from os import system, name
# importoidaan sleep joka pitää printtauksen tietyn ajan ruudulla.
from time import sleep

def clear():

	if name == 'nt':
		_ = system('cls')

	else:
		_ = system('clear')
                            

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

clear()

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
print("Aika surullisen näköinen kaveri.") 
sleep(3)
clear()

print("Nimi, hattu ja värit voisivat tehdä hänelle hyvää.") 
sleep(3)
clear()

print(f""" 
                     o
                   .-I-.
                    / \ \n""") 

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
         |___________________________| \n""")

charHat = ""
charHead = "o"
charLeftHand = "."
charLeftArm = "-"
charTorso = "I"
charRightArm = "-"
charRightHand = "."
charLeftLeg = "/"
charRightLeg = "\\"

def valitsehattu():
    global charHat
    while True:
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

def valitsenimi():
    print("valitsenimi")
     
def hahmomenu():
    print("hahmonenu")

valinta = input("Syötä valinta: ")

if valinta == "2":
    charHat = valitsehattu()

elif valinta == "1":
    valitsenimi()

#elif valinta == "3":
     #valitsevarit()

print(f"""
       {charHat}                                                    
       {charHead}                                                    
     {charLeftHand}{charLeftArm}{charTorso}{charRightArm}{charRightHand}                                                
      {charLeftLeg} {charRightLeg} 
      
      Olet valmis! """)

   


     
     













