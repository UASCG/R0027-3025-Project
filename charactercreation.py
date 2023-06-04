from os import system, name

# importoidaan sleep joka pitää printtauksen tietyn ajan ruudulla.
from time import sleep

def clear():

	
	if name == 'nt':
		_ = system('cls')

	else:
		_ = system('clear')
clear()

def teksti1():


  print(f"                     . ")
  print(f"(__________________´   `____________________)")
  print(".                                           .")
  print (f".           Tervetuloa Limssin \t            .\n. \t  ihmeelliseen maailmaan!           . ")
  print(".                                           .")
  print(f" _________________       ___________________")
  print(f"(_                 ` . ´                    _)")



def teksti2():
  print(f"                     . ")
  print(f"(__________________´   `____________________)")
  print(".                                           .")
  print (f".           Täällä pääset komemaan  \t    .\n.      opiskelijaelämän upeimmat puolet.    . ")
  print(".                                           .")
  print(f" _________________       ___________________")
  print(f"(_                 ` . ´                    _)")


def teksti3():
  print(f"                     . ")
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













