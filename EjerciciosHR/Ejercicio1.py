# 
# @Autor:                     Ramirez Morales Erick Hazel
# @date:                      07/11/22
# @description:
# Problema 1.
# Dado un entero n, implementar las siguientes acciones condicionales
#     Si n es impar, imprimir Weird
#     Si n es par y esta en el rango inclusivo de 2 a 5, imprimir Not Weird
#     Si n es par y esta en el rango inclusivo de 6 a 20, imprimir Weird
#     Si n es par y es mayor que 20, imprimir Not Weird

#     Constrains 
#     1 <= n <= 100
# 

import math
import os
import random
import re
import sys


n = int(input().strip()) #Leemos desde el teclado y le quitamos los espacios del principio y final
if(n >= 1 and n <= 100):
    if(n%2 != 0):
        #Si n ES IMPAR
        print("Weird")
    else:
        #SI N ES PAR
        if(n >= 2 and n <= 5):
            print("Not Weird")
        elif(n > 5 and n <= 20):
            print("Weird")
        else:
            print("Not Weird")        
