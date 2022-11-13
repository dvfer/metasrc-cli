import pandas as pd
def skill_to_list(toParse):
    """ Funcion que recibe una sopita con los td de la tabla de skills\n
        Considerar que el 0 corresponde a un icono que corresponde a la imagen de la habilidad.
    """
    skillset = [0]*19 
    for idx,elem in enumerate(toParse):
        x = elem.contents
        if idx != 0:

            if x != []:
                skillset[idx] = "*"
            elif x == []:
                skillset[idx] = ""
    skillset.remove(0)
    return skillset

def get_skill_table(soup):
    skills_soup = soup.find_all('table')
    levels = [str(i) for i in range(1,19)]
    levels.insert(0,"skill/level")

    for id_toParse_skill,toParse_skill in enumerate(skills_soup[0].find_all('tr')):
        # los ids corresponden a un td de cada habilidad
        # 0: el td de la pasiva, o mas bien de los niveles
        # 1: td de la Q 
        # 2: td de la W
        # 3: td de la E
        # 4: td de la R

        if id_toParse_skill == 0:
            continue
        if id_toParse_skill == 1:
            Q_skill = skill_to_list(toParse_skill)
            Q_skill.insert(0, "Q")
        elif id_toParse_skill == 2:
            W_skill = skill_to_list(toParse_skill)
            W_skill.insert(0, "W")
        elif id_toParse_skill == 3:
            E_skill = skill_to_list(toParse_skill)
            E_skill.insert(0, "E")
        elif id_toParse_skill == 4:
            R_skill = skill_to_list(toParse_skill)
            R_skill.insert(0, "R")
    skill_matrix = [Q_skill,W_skill,E_skill,R_skill]
    dataframe = pd.DataFrame(skill_matrix,columns=levels)
    print(dataframe.to_string(index=False))
