#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""-----------------------------------------------------------------
File:   test.py
Author: Procesadores de Lenguajes-University of Zaragoza
Date:   febrero 2026
Coms:   "script" para compilar y ejecutar los fuentes de prueba de cpt
        Ejecutar como
            python <path_hasta_programas>
        Hay que asegurarse de que el "script" "compila_ejecuta.sh"
        tenga los paths correctos, y que la herramientas en pcode_tools"
        tienen permisos de ejecución
-----------------------------------------------------------------"""
import os
import sys
import shutil

OS_DIR = ''
EXT = '.cpt'

#Comprueba que se invoque con un parámetro
if len(sys.argv) != 2:
    print('------------------------------------------')
    sys.exit('Invocar como: ' + sys.argv[0] + ' <path_dir_fuentes>') 
else:
    path_fuentes = sys.argv[1]

fuentes = os.listdir(path_fuentes)
fuentes = [os.path.splitext(f)[0] for f in fuentes if os.path.splitext(f)[1] == EXT]

ENSAMBLADOR = './ensamblador'
MAQUINAP = './maquinap'

print('\n---------------------------------------------------------------')
for f in fuentes:

    cmd_compilar = f'java -jar esqueleto_proyecto/dist/cpt.jar {path_fuentes}/{f}{EXT}'
    cmd_ensamblar = f'{ENSAMBLADOR} {path_fuentes}/{f}'
    cmd_ejecutar = f'{MAQUINAP} {path_fuentes}/{f}'

    if f == 'invertir_pgm':
        os.system(cmd_compilar)
        os.system(cmd_ensamblar)
        os.system(f'{cmd_ejecutar} < {path_fuentes}/einstein.pgm > {path_fuentes}/einstein_inv.pgm')
    else:
        os.system(cmd_compilar)
        os.system(cmd_ensamblar)
        os.system(cmd_ejecutar)
        
    print('\n--------------------- ' + f + ' --------------------- (Return para continuar)', end=' ')
    res = input()
