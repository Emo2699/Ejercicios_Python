# '''
# author:         Ramirez Morales Erick Hazel
# date:           20/07/2023
# description:    Ejercicio 8 en python

# Ejercicio:
#     Dados los nombres y calificaciones de cada estudiante de una clase con N estudiantes. 
#     Almacenalos en una lista anidada e imprime el/los nombre de cualquier estudiante(s) 
#     que tenga la segunda calificacion más baja

# NOTA: Si existe multiples estudiantes con la segunda calificacion más baja, ordena sus nombres
# alfabéticamente e imprime cada nombre en una nueva linea.

# Ejemplo:
#     records = [["chi",20.0], ["beta",50.0], ["alpha",50.0]]
#     El orden de las calificaciones es [20.0,50.0], entonces la segunda calificacion más baja
#     es 50.0. Existen dos estudiantes con esa calificación: "beta" y "alpha". Ordenamos 
#     alfabéticamente quedan asi
#         alpha
#         beta

# Entrada:
#     La primera linea contiene un entero N, el numero de estudiantes
#     La siguientes lineas describen a cada estudiante
#     Una linea contiene el nombre del estudiante
#     La siguiente linea contiene la calificacion de dicho estudiante.

# Restricciones.
#     2<= N <= 5
#     Debe de existir siempre uno o mas estudiantes con la segunda calificacion más baja

# Salida
#     Imprime los nombres de los estudiantes con la segunda calificacion
#     más baja

# '''
#Funcion que regresa el segundo valor más bajo de una lista
def encontrarSegundaCalificacionBaja(calificaciones:list):
    sinDuplicados = set(calificaciones)
    lista = list(sinDuplicados)
    lista.sort()
    return lista[1]

numeroEstudiantes = int(input("Ingresa el numero de estudiantes: "))
print(numeroEstudiantes)

estudiantes = []
calificaciones = []    
for x in range(numeroEstudiantes):
    nombre = input("Ingresa el nombre del estudiante: ")
    calificacion = float(input("Ingresa su calificacion: "))
    estudiantes.append([nombre,calificacion])
    calificaciones.append(calificacion)

segundaCalificacionBaja = encontrarSegundaCalificacionBaja(calificaciones)
nombres = []
for x in range(len(estudiantes)):
    if segundaCalificacionBaja in estudiantes[x]:
        # print(estudiantes[x][0])
        nombres.append(estudiantes[x][0])    
nombres.sort()
for nombre in nombres:
    print(nombre)