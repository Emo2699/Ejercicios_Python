# '''
# @author:                    Ramirez Morales Erick Hazel
# @date:                      16/11/22
# @Descripcion:               Ejercicio5.py

# Ejercicio 5:
#     Leer un numero N desde el STDIN y sin usar ninguna funcion de strings
#     imprimir lo siguiente.
#         OUTPUT = 1234...N       
#
numero = int(input())

if(1 <= numero <= 150):
    for i in range(numero):
        print(i+1,end='')
