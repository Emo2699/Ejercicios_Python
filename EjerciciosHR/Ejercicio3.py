# 
# @Author:                    Ramirez Morales Erick Hazel
# @Date:                      09-11-22
# @Descripcion:               Ejercicio 3

# Ejercicio:
#     Leer un numero desde el teclado, despues imprimir el cuadrado de todos los numeros
#     no negativos menores al numero leido
# 
# 
# NOTA: La funcion pow de la biblioteca math nos arroja los resultados de tipo flotante
# 
n = int(input())

if(n >= 1 and n <= 20):
    i = 0
    while(i < n):
        #print(pow(i,2))
        print(i*i)
        i+=1
    