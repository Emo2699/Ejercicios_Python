# author:             Ramirez Morales Erick Hazel
# descripcion:        Programa que implementa un perceptron simple de dos entradas con un solo ejemplo  # noqa: E501
# date:               09/09/23



import math


def calcularH(x1,x2,bias,w1,w2):
    return ((x1*w1) + (x2*w2) + bias)


def evaluandoFuncionActivacion(h):
    prediccion = 1 / (1 + (math.exp(-h)))
    return prediccion




#Funciones para el descenso del gradiente
def calcularDerivada(prediccion):
    return (prediccion * (1-prediccion))


def calcularDelta(valorEsperado, valorObtenido,fPrima):
    return ((valorEsperado - valorObtenido) * fPrima)


#Entradas
x1 = 0.5
x2 = 0.3
bias = 0.9

#Pesos
w1 = 0.2
w2 = 0.7

#Factor de aprendizaje
eta = 1


#Primer valor de prediccion
h = calcularH(x1,x2,bias,w1,w2)
prediccion = evaluandoFuncionActivacion(h)

print(prediccion)