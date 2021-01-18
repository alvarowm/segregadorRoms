import os
import shutil

SEGREGADOR_EXE = Segregador.exe

S = "Segregador.py"

segregar_por_gd_str = input('''Segregar por [!] "Verified Good Dump?"\n''')
segregar_por_gd = False

segregar_por_regiao_str = input('''Segregar por região?\n''')
segregar_por_regiao = False

if segregar_por_gd_str.startswith("S") \
        or segregar_por_gd_str.startswith("s") \
        or segregar_por_gd_str.startswith("Y") \
        or segregar_por_gd_str.startswith("y"):
    segregar_por_gd = True

if segregar_por_regiao_str.startswith("S") \
        or segregar_por_regiao_str.startswith("s") \
        or segregar_por_regiao_str.startswith("Y") \
        or segregar_por_regiao_str.startswith("y"):
    segregar_por_regiao = True

regioes = {
    "(1)",
    "(4)",
    "(A)",
    "(J)",
    "(B)",
    "(K)",
    "(C)",
    "(NL)",
    "(E)",
    "(PD)",
    "(PD)",
    "(F)",
    "(S)",
    "(FC)",
    "(SW)",
    "(FN)",
    "(U)",
    "(G)",
    "(UK)",
    "(GR)",
    "(UNK)",
    "(HK)",
    "(I)",
    "(H)",
    "(UNL)"}

GOODDUMP = "[!]"

for arquivo in next(os.walk('.'))[2]:
    path = os.path.sep
    path += arquivo[0].upper() + os.path.sep

    if arquivo == S or arquivo == SEGREGADOR_EXE:
        continue

    if segregar_por_regiao:
        for regiao in regioes:
            if arquivo.upper().find(regiao) != -1:
                path += regiao.replace('(', '').replace(')', '') + os.path.sep

    if segregar_por_gd:
        if arquivo.find(GOODDUMP) != -1:
            path += os.path.sep + "GD" + os.path.sep

    if not os.path.exists(os.path.realpath('.') + path):
        os.makedirs(os.path.realpath('.') + path)

    shutil.copy2(os.path.realpath('.') + os.path.sep + arquivo, os.path.realpath('.') + path)
