'''
@Autor:                 Ramirez Morales Erick Hazel
@Date:                  07/11/22
@Descripcion:           Breve introdducion a python
@version de python:     3.10.15  

Para ejecutar en la terminal un programa de python se realiza lo siguiente
$python nombre_programa.py

'''


#funcion type(x) --> Regresa la clase (tipo de dato) al que pertenece X

print(type("Hola Mundo"))

#funcion upper() --> Cambia toda una string a mayuscula
print("hola mundo".upper())

#Funcion lower() --> cambia toda una string a minuscula
print("ERICK".lower())

#Funcion capitalize() --> pone la primer letra de una cadena en mayuscula

#Funcion strip() --> quita los espacios iniciales y finales de una cadena
cadena = "          Esto es      una cadena    con muchos espacios      "
print(cadena)
print(cadena.strip())


#Funcion replace(cadena_a_remplazar, cadena_nueva) --> remplaza una cadena, o parte de una, por la nueva cadena
cadena2 = "Esto es una cadena sin reemplazo"
print(cadena2)
print(cadena2.replace("sin reemplazo", "con REEMPLAZO"))

'''
Operadores matemáticos
+-*/ --> Suma, resta multiplicacion y division
a**b --> elevar a a la potencia b
x//y --> division entera 
x%y --> modulo

Operadores de comparacion
    < --> menor 
    > --> mayor
    == --> igualdad
    != --> diferentes 

Operadores logicos
    AND
    OR
    NOT
Valores booleanos 
    True
    False
Las constantes en python se escriben en mayusculas
PASSWORD = 1234 ; tenemos una variable constante con nombre PASSWORD y guarda el valor '1234'

La funcion input() permite leer datos a traves del teclado, con la peculiaridad de que lo recibe como STRING
si deseamos guardar otro tipo de dato hay que castearlo
    lectura = input() --> guarda lo introducido por el teclado como una cadena
    lectura = int(input()) --> guarda lo introducido por el teclado como un INT 
De la forma anterior se hace el casteo de tipos de datos
'''

numero = 1326
print(type(numero))
print(f"El numero almacenado es {numero}")
print(f"El numero almacenado es {numero + 5}")


'''
CONDICIONALES
if(condicion):
    codigo si se cumple la condicion
else
    codigo si la condicion NO se cumple

EXISTE LA SENTENCIA elif        
'''

'''
BUCLES
While

while(condicion):
    sentencias a repetir
'''