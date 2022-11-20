import requests
from bs4 import BeautifulSoup
import pandas as pd
from recursos import items
from recursos import skills



print("""
===========================================
  __  __      _         _____ _      _____ 
 |  \/  |    | |       / ____| |    |_   _|
 | \  / | ___| |_ __ _| |    | |      | |  
 | |\/| |/ _ | __/ _` | |    | |      | |  
 | |  | |  __| || (_| | |____| |____ _| |_ 
 |_|  |_|\___|\__\__,_|\_____|______|_____|
===========================================
Formato: Campeon {rol}
Roles: top - jungle - mid - adc - support
Ejemplo: ashe jungle

""")
Champ = ''
Rol = ''
while True:
    arg = input(">> ")
    if arg == "exit":
        break

    # La idea es que si no me deja separa en una lista de 2 lo convierta en lista pero podria hacer sin el try al final de cuentas pq
    # por ejemplo si ingreso corki mid mid pasaria al except y splitearia y tendria [corki, mid, mid] XD
    # asi que en conclusion esto no está bien pensado.
    try:
        Champ, Rol = (arg.strip().split(" "))
        URL = f"https://www.metasrc.com/5v5/champion/{Champ}/{Rol}"
    except:
        Champ = (arg.strip().split(" "))[0]
        Rol = ''
        print(Champ)
        URL = f"https://www.metasrc.com/5v5/champion/{Champ}/default"
    else:
        print('input incorrecto')
        continue
    # manejo de errores  
    i = 1   
    while i < 6:
        try:
            r = requests.get(URL,timeout=5)
            break
        except requests.exceptions.RequestException as e:

            print(f"Oops! problemas, especificamente \'{e}\', reintento n {i} :)")

            i += 1
    if i >= 6:
        continue
    # manejo de error de input rol
    if Rol not in ['',"top","jungle","mid","adc","support"]:
        print("rol no soportado, recuerda el formato, obteniendo rol default")
    # si existe redirección implica que el rol fue mal escrito y almacenamos el url de la redirección con el rol default
    if r.history:
        print("Request was redirected")
        Rol = str(r.url).split('/')[-1]


    soup = BeautifulSoup(r.content,"lxml")
    print(f"Items iniciales para \033[1m\033[4m{Champ.upper()} {Rol.upper()}" + '\033[0m\033[0m:')
    items.get_initial_items(soup)
    print("")
    print(f"Items para \033[1m\033[4m{Champ.upper()} {Rol.upper()}" + '\033[0m\033[0m:')
    items.get_items(soup)
    print("")
    print("Orden de habilidades:")
    skills.get_skill_table(soup)

