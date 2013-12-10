#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fspuerto.py
#       
#       Copyright 2013 Fraph <jfraph@gmail.com>
#       Site: http://fraph.co/
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#    This program is free software: you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by   
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version. 
#   
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.         
#                                                         
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#   
#
#
#
#
######################
#Escaner de Puertos  #
#Simple and Sencillo #
######################
Autor = "Fraph"     #
Version = "1.0"     #
######################    
import os            #
import sys           #
from socket import * #
######################
if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass
    #Colores
class color:
    amarillo = '\033[1;33m'
    azul = '\033[94m'
    rojo = '\033[91m'
    verde = '\033[92m'
    blanco = '\033[0m'
print color.azul + "\t\t########################|>FSpuerto<|########################" + color.blanco
print color.azul + "\t\t#                 Developed By: @Fr4phc0r3                 #" + color.blanco
print color.azul + "\t\t##+>                        V1.0                        <+##" + color.blanco
print color.azul + "\t\t##+>         ################################           <+##" + color.blanco
print color.azul + "\t\t#            #+>    Escaner de Puertos    <+#              #" + color.blanco
print color.azul + "\t\t############################################################\n" + color.blanco 
Host = raw_input("Ingresa la URL==> ")
Puertos = [21, 22, 23, 25, 42, 43, 53, 67, 79, 80, 102, 110, 115, 119, 123, 135, 137, 143, 161, 179, 379, 389, 443, 445, 465, 636, 993, 995, 1026, 1080, 1090, 1433, 1434, 1521, 1677, 1701, 1720, 1723, 1900, 2409, 2082, 2095, 3101, 3306, 3389, 3390, 3535, 4321, 4664, 5190, 5500, 5631, 5632, 5900, 65535, 7070, 7100, 8000, 8080, 8880, 8799, 9100]#Unos cuantos puertos
HomePuerto = raw_input("Ingresa el puerto de inicio==> ")
Puertos.reverse() #Retroceso
Puertos.append(HomePuerto) #Inicio
Puertos.reverse() #Inversion de Lista

def coneccion(Host, Hpuerto): #Hpuerto+Host
    try:
        socalo=socket(AF_INET, SOCK_STREAM)
        socalo.settimeout(10)
        socalo.connect((Host, Hpuerto))
        socalo.settimeout(None)
        print("\033[94m%d\033[1;m:=>\033[1;32m Abierto\033[1;m" % Hpuerto)
    except:
        print("\033[94m%d\033[1;m:=>\033[1;31m Cerrado\033[1;m" % Hpuerto)
        
def Escaneo(Host, Puertos):
    try:
        IPHost = gethostbyname(Host)
    except:
        print("Error: '\033[1;31m%s\033[1;m' Host desconocido" % Host)
        return
    try:
        NombreH = gethostbyaddr(IPHost) 
        print('\nNombre del Host: %s' % NombreH)
    except:
        print('\n\033[1;33mIP del Host:\033[1;m %s' % IPHost)
        print ""
        print color.verde + "=> Escaneando: Objetivo...\n" + color.blanco
    for puerto in Puertos:
        print('\033[1;33mEscaneando puerto\033[1;m %s' % puerto)
        coneccion(Host, int(puerto))
def main():
    Escaneo(Host, Puertos)
if __name__=='__main__':
    main()
    #Ingresa la URL sin (http://) Ejemplo: www.objetivo.com
