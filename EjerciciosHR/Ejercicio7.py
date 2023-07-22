'''
author:         Ramirez Morales Erick Hazel
date:           21/06/2023
description:    Ejercicio 7 en python

Ejercicio:
    Dada la hoja de resultados de los corredores
    participantes de tu escuela del dia de deportes. se te
    solicita encontrar el puntaje del sub campeon
    alto.
Entrada:
    La primera linea contiene el numero n de participantes
    La segunda linea contiene un arreglo A de n elementos
    separados cada uno por un espacio.

Restricciones.
    2<= n <= 10
    -100 <= A[i] <= 100

Salida
    Imprime el resultado más alto

'''
n = int(input())
#convertimos en una lista los numeros separados por espacios que ingresa el usuario
arr = map(int, input().split())
lista = list(arr)
maximo = lista[0]
i = 1
while i<n:
    if(maximo < lista[i]):
        maximo = lista[i]
    i+=1    
print(maximo)
#Convertimos a conjunto para eliminar duplicados
conjunto = set(lista)
#quitamos del conjunto el maximo elemento
conjunto.discard(maximo)
print(conjunto)
lista = list(conjunto)    
#buscamos al segundo maximo    
n = len(lista)
maximo = lista[0]
i = 1
while i<n:
    if(maximo < lista[i]):
        maximo = lista[i]
    i+=1    
print(maximo)   
  