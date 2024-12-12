#Sesion12dicTarde
# Solicita al usuario la cantidad de números
n = int(input("¿Cuántos números deseas ingresar? "))

# Crea la lista solicitando números al usuario
numeros = []
for x in range(n):
    numero = float(input(f"Ingresa el número {x+1}: "))
    numeros.append(numero)

# Ordena la lista en orden descendente
numeros.sort(reverse=True)

# Muestra la lista ordenada
print("Lista ordenada de manera descendente:", numeros)

# Solicita la cantidad de números
n = int(input("¿Cuántos números deseas ingresar? "))

# Solicita los números al usuario
numeros = []
for i in range(n):
    numero = float(input(f"Ingresa el número {i+1}: "))
    numeros.append(numero)

# Calcula el promedio
promedio = sum(numeros) / len(numeros)

# Encuentra los números mayores que el promedio
mayores_que_promedio = [num for num in numeros if num > promedio]

# Muestra los resultados
print(f"El promedio es: {promedio}")
print("Números mayores que el promedio:", mayores_que_promedio)