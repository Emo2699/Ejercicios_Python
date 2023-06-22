'''
author:         Ramirez Morales Erick Hazel
date:           21/06/2023
description:    Ejercicio 6 en python

Ejercicio: 
    Comencemos a aprender acerca de las listas.
    Se te proporcionan tres numeros enteros X,Y y Z los cuales
    representan las dimensiones de un cubo, además de un número
    entero N. Imprime una lista de todas las posibles coordenadas
    dadas por (i,j,k) en tres dimensiones donde la suma de los 
    valores i+j+k no sea N.

    además se debe de cumplir la siguiente condición

    0 <= i <= x
    0 <= j <= y
    0 <= k <= z
    NOTA: Se recomienda no usar loops para la solución de este problema 
'''
#Ingresamos los valores de los enteros
# print("Ingresa los valores para X, Y, Z y N")
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())


#NOTA, LOS VALORES DE X,Y,Z, y N son ingresados desde el teclado, sin embargo, para hacer pruebas
#de forma rápida se asignan desde el inicio.
x = 1
y = 1
z = 2
n = 3
#Creamos la lista con todas las combinaciones posibles de acuerdo a los valores dados
lista = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

#comenzamos el proceso de busqueda para obtener las coordenadas que cumplan i+j+k != N
#Primer forma de hacerlo
suma = 0
resultado=[]
for elemento in lista:
    for numero in elemento:
        suma+=numero
    if suma!=n:
            resultado.append(elemento)
    suma=0        
print(lista)
print(resultado)

#segunda forma de hacerlo 
#de acuerdo con la página de hacker rank no se deben de usar loops, esta opcion es la que aceptan 
print("Segunda forma de hacerlo")
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
