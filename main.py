import requests
from bs4 import BeautifulSoup
import pandas as pd
from items import *
from skills import *






print("""
  __  __      _         _____ _      _____ 
 |  \/  |    | |       / ____| |    |_   _|
 | \  / | ___| |_ __ _| |    | |      | |  
 | |\/| |/ _ | __/ _` | |    | |      | |  
 | |  | |  __| || (_| | |____| |____ _| |_ 
 |_|  |_|\___|\__\__,_|\_____|______|_____|

Formato: Campeon {rol}
Roles: top - jungle - mid - adc - support
Ejemplo: ashe jungle

Aun no se implementa manejo de errores.

""")
while True:
    arg = input(">> ")
    if arg == "exit":
        break
    
    Champ, Rol = (arg.strip().split(" "))
    URL = f"https://www.metasrc.com/5v5/champion/{Champ}/{Rol}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"lxml")
    print(f"Items iniciales para \033[1m\033[4m{Champ.upper()} {Rol.upper()}" + '\033[0m\033[0m:')
    get_initial_items(soup)
    print("")
    print(f"Items para \033[1m\033[4m{Champ.upper()} {Rol.upper()}" + '\033[0m\033[0m:')
    get_items(soup)
    print("")
    print("Orden de habilidades:")
    get_skill_table(soup)

