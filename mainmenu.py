# logo ja välkkyvä epilepsia-intro
import time

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
    print()

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
    print()
    
# päävalikon toiminnot, looppi
     
while True:
    nayta_main_menu()
    valinta = input("                     Valitse toiminto (1-4): ")

    if valinta == "1":
        print()
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
