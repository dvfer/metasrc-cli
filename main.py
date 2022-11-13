import requests
from bs4 import BeautifulSoup
import pandas as pd
from items import *
from skills import *






print(""""
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
    print("Items con mayor winrate:")
    get_items(soup)
    print("")
    print("orden de habilidades:")
    get_skill_table(soup)