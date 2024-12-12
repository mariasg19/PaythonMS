#Sesion 12/12

#Ejercicio 1
# Solicita un número
num = int(input("Ingresa un número: "))


#Ejercicio 2
# Comprueba si es par o impar
if num % 2 == 0:
    print(f"{num} es un número par.")
else:
    print(f"{num} es un número impar.")


#Ejercicio 3
# Solicita el número hasta donde contar
n = int(input("Contemos hasta el número: "))


#Ejercicio 4
# Muestra los números del 1 hasta n
for i in range(1, n + 1):
    print(i)

    import math  # Importa la librería matemática


#Ejercicio 5
# Solicita el radio
radio = float(input("Ingresa el radio del círculo: "))

# Calcula el área
area = math.pi * radio**2

# Muestra el resultado
print(f"El área del círculo es: {area}")

# Solicita una cadena
texto = input("Ingresa una cadena: ")

# Calcula la longitud de la cadena
cantidad_caracteres = len(texto)

# Muestra el resultado
print(f"La cadena '{texto}' tiene {cantidad_caracteres} caracteres.")