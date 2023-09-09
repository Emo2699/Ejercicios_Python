'''
author:         Ramirez Morales Erick Hazel
date:           25/07/2023
description:    Ejercicio 10 en python

Ejercicio:
    Considera una lista (list = []). Tu puedes ejecutar los siguientes comandos
    intert i e => Inserta el entero 'e' en la posicion i
    print => imprime la lista
    remove e => Borra la primera ocurrencia del elemento 'e' en la lista
    append e => Inserta el elemento 'e' al final de la lista.
    sort => ordena la lista de forma ascendente, si no se le pasa ningún parametro
    pop => Elimina el último elemento en la lista.
    reverse => Revierte la lista

    Inicializa tu lista y lee en el valor de N seguido de N lineas con los comandos enlistados anteriormente. Itera a travez de cada comando en orden y ejecuta su correspondiente operacion en tu lista

Ejemplo:
    

Entrada:
    

Restricciones.
    

Salida
    
'''
# n = int(input())
# for _ in range(n):
#     *args = input().split()

n = int(input())
for _ in range(n):
    command, *args = input().split()
    operation = commands.get(command, lambda : None)
    operation(*map(int, args))