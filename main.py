import requests
from bs4 import BeautifulSoup
import pandas as pd
from recursos import items
from recursos import skills
from recursos import const

def Hello():
    print("""
    =======================================================
    ███╗   ███╗███████╗████████╗ █████╗  ██████╗██╗     ██╗
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║     ██║
    ██╔████╔██║█████╗     ██║   ███████║██║     ██║     ██║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║     ██║     ██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╗███████╗██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝
    =======================================================
    Formato: Campeon {rol}
    Roles: top - jungle - mid - adc - support
    Ejemplo: ashe jungle
    Nota: 
        - Ignorar apóstrofo (')
        - Ignorar espacios
    Ej: Kha'Zix -> Khazix
        Miss Fortune -> Missfortune
    """)
Hello()
while True:
    Champ = ''
    Rol = 'default'
    args = input(">> ")
    if args == "exit":
        break
    if args == "random":
        pass # campeon random

    argsListed = args.strip().split(" ")

    Champ = argsListed[0]
    if Champ.title() not in const.CHAMPIONS:
        print("Campeón no reconocido :(")
        continue

    if len(argsListed) == 2:
        Rol = argsListed[1]
        if Rol not in const.ROLES:
            print("Rol ingresado no respeta el formato :(")
            continue
    elif( len(argsListed) > 2 ):
        print("Demasiados argumentos")
        continue
        
    print(f"Query -> champ {Champ}, rol {Rol}")
    
    URL = const.genURL(Champ,Rol)

    i = 1   
    while i < 6:
        try:
            r = requests.get(URL,timeout=5)
            break
        except requests.exceptions.RequestException as e:
            print(f"Oops! problemas, especificamente \'{e}\', reintento n {i} :)")
            i += 1
    if i >= 6: 
        break

    # si existe redirección implica que el rol fue mal escrito y almacenamos el url de la redirección con el rol default
    if r.history:
        Rol = str(r.url).split('/')[-1]


    soup = BeautifulSoup(r.content,"lxml")
    print(f'\033[1m\033[4m{Champ.upper()} {Rol.upper()}' + '\033[0m\033[0m:')
    print("Items iniciales:")
    items.get_initial_items(soup)
    print("")
    print('Items:')
    items.get_items(soup)
    print("")
    print("Orden de habilidades:")
    skills.get_skill_table(soup)


