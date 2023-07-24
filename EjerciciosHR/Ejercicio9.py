'''
author:         Ramirez Morales Erick Hazel
date:           23/07/2023
description:    Ejercicio 9 en python

Ejercicio:
    El codigo proporcionado leera un diccionario las parejas clave/valor con el nombre [marks] de una lista de estudiantes. Imprime el promedio de las marcas del arreglo por nombre de estudiante proporcionado, mostrando 2 numeros despues del punto decimal

Ejemplo:
    marks key:value; las parejas son:
    'alpha':[20,30,40]
    'beta': [30,50,70]
    query_name = 'beta'
    El nombre proporcionado es 'beta', por lo que su promedio es (30+50+70)/3 = 50

Entrada:
    La primer linea contiene el entero N, el numero de estudiantes en el diccionario. las siguientes lineas contienen el nombre y marcas obtenidas por estudiante cada valor separado por un espacio.
    La última linea contiene el nombre buscado para obtener su promedio.

Restricciones.
    2 <= N <= 10
    0 <= marcas[i] <= 100
    longuitud del arreglo de marcas/records = 3

Salida
    Imprimir el promedio de las marcas del alumnos solicitado, mostrando dos numeros despues del punto decimal
'''

def obtenerPromedio(records: list):
    suma= 0
    for x in records:
        suma+=x
    return suma/3    

n = int(input("Ingresa el numero de estudiantes: ")) #numero de estudiantes
student_marks = {} #diccionario
for _ in range(n):
    name, *line = input("Ingresa los valores: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Ingresa el nombre del estudiante buscado: ")
print(student_marks)
print("{:.2f}".format(obtenerPromedio(student_marks[query_name])))
