# Ejercicio 10 USANDO FUNCION TYPE
"""Imprime una cadena con distintos datos
e indica el tipo de datos que son"""
cadena = (5,4,True,"Holi")
print(cadena)
#El type no se puede aplicar directamente sobre una cadena
print(type("Ho"),type(4),type(True))

#Ejercicio 11 OPERADORES ARITMETICOS
num1 = 3
num2 = 5
print(num1+num2)
print(num1-num2)
print(num1*num2)
#EXPONENTE 3*3*3*3*3
print(num1**num2)
print(num1/num2)
#DIVISION CON RDO SIN DECIMALES REDONDEANDO A LA BAJA
print(num1//num2)
print(num2%num1)

#Ejercicio 11
# Realiza la potencia de un numero
base = 2
exponente = 3
print(base**exponente)

#Ejercicio 12
#Invertir una cadena

cadena = "cadena"
invertir = cadena[::-1]
print(f"Mi cadena inversa es {invertir}")

#Ejercicio 13
#Calcula el area de un rectangulo 
#pide base y altura al usuario

base = int(input("Ingresa la base "))
altura = int(input("Ingresa la altura "))

area = base*altura
print("El area es ", area)


#Ejercicio 14
#Convierte un numero entero en cadena
numero2 = 40
print(type(numero2))
cadena2 = str(numero2)
print(type(cadena2))
