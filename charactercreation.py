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

valinta = input()
if valinta == 1:
     valitsehattu()

elif valinta == 2:
     valitsenimi()

elif valinta == 3:
     valitsevarit()

#  n
#  o
#.-I-.
# / \


charHat = 0
charHead = 0
charLeftHand= 0 
charLeftArm = 0 
charTorso= 0
charRightArm= 0 
charRightHand= 0
charLeftLeg = 0 
charRightLeg = 0

#def valitsenimi():
     


def valitsehattu():

  print("""
  1. Hattu A
  2. Hattu B
  3. Hattu C
""")






#def hahmomenu():
     
     













