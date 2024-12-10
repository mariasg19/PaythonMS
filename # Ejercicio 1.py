# Ejercicio 1------------------------------------------------------------
"""
Sumar dos numeros y mostrar su resultado
"""

num1 = 5
num2 = 4

resultado = num1 + num2

print(resultado)

# Ejercicio 2------------------------------------------------------------
"""Calcula el area de un circulo
con un radio dado"""

#Aqui ya empezamos a usar las librerias 
#porque necesitamos la constante de pi

import math

radio = 3
area = math.pi * radio **2
print("El area es ", area)


# Ejercicio 3------------------------------------------------------------
""" Concatena dos cadenas de texto"""

cadena1 = "Hola"
cadena2 = "caracola"

concatenacion = cadena1 + " " + cadena2

print("Mi cadena es ",concatenacion)

# Ejercicio 4------------------------------------------------------------
"Crear una lista con diferentes elementos e imprimirla"

lista1 = [4, True, "Hola"]

print ("elementos: ", lista1)

# Ejercicio 5------------------------------------------------------------
"Operar con una multiplicacion"

multiplicacion = num1*num2
print ("Mi multiplicacion es ", multiplicacion)

#Ejercicio 6-------------------------------------------------------------
"""Crea una cadena de texto 
y muestra su longidud"""

cadena3 = "Holi holi"
longitud = len(cadena3)

print("La longitud de",cadena3, "es",longitud)

# Ejercicio 7------------------------------------------------------------
"Calcula el promedio de una lista de numeros"
numeros = [2,4,5,3,0,4,5]
Promedio = sum(numeros) / len(numeros)

print("La media de mi lista es " , Promedio)


