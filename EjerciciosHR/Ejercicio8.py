'''
author:         Ramirez Morales Erick Hazel
date:           20/07/2023
description:    Ejercicio 8 en python

Ejercicio:
    Dados los nombres y calificaciones de cada estudiante de una clase con N estudiantes. 
    Almacenalos en una lista anidada e imprime el/los nombre de cualquier estudiante(s) 
    que tenga la segunda calificacion más baja

NOTA: Si existe multiples estudiantes con la segunda calificacion más baja, ordena sus nombres
alfabéticamente e imprime cada nombre en una nueva linea.

Ejemplo:
    records = [["chi",20.0], ["beta",50.0], ["alpha",50.0]]
    El orden de las calificaciones es [20.0,50.0], entonces la segunda calificacion más baja
    es 50.0. Existen dos estudiantes con esa calificación: "beta" y "alpha". Ordenamos 
    alfabéticamente quedan asi
        alpha
        beta

Entrada:
    La primera linea contiene un entero N, el numero de estudiantes
    La siguientes lineas describen a cada estudiante
    Una linea contiene el nombre del estudiante
    La siguiente linea contiene la calificacion de dicho estudiante.

Restricciones.
    2<= N <= 5
    Debe de existir siempre uno o mas estudiantes con la segunda calificacion más baja

Salida
    Imprime el resultado más alto

'''

# for _ in range(int(input())):
#     nombre = input()
#     score = float(input())

numeroEstudiantes = int(input("Ingresa el numero de estudiantes: "))
# print(numeroEstudiantes)

listaInterna = []
for x in range(numeroEstudiantes):
    nombre = input()
    calificacion = float(input())
    listaInterna.append([nombre,calificacion])
    
calificaciones = []    
for x in range(numeroEstudiantes):
    calificaciones.append(listaInterna[x][1])
print(calificaciones)    