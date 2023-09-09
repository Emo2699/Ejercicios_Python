# '''
# @Author:                    Ramirez Morales Erick Hazel
# @date:                      09/11/22
# @Descripcion:               Ejercicio 3 en python

# Ejercicio.
#     Un dia extra es añadido al calendario al menos cada cuatro
#     años como 29 de Febrero, ese dia es conocido como dia 
#     intercalar o dia bisiesto. Esto corrige al calendario
#     debido a que nuestro planeta toma aproximadamente 365.25
#     dias en dar una vuelta al sol. Un año bisiesto tiene un 
#     dia bisiesto o intercalar.

#     En el calendario Gregoriano usa tres condiciones para 
#     identificar si un año es bisiesto.
#     1. El año puede ser dividido en 4
#     2. Si el año es divisible entre 100, entonces NO ES BISIESTO, a menos que
#         3. El año puede ser dividio en 400

#     Prueba:
#         Dado un año, determinar si es un año bisiesto, Si lo es regresar el valor booleano TRUE,
#         en caso contrario regresar FALSE        
# '''
#FUNCIONES
def is_leap(year):
    leap = False
    if(year%4 == 0 and year%100 != 0):
        leap = True
    if(year%4 == 0 and year%100 == 0 and year%400 == 0):
        leap = True    
    return leap            

year = int(input())

if(year >= 1900 and year <= pow(10,5)):
    print(is_leap(year))
