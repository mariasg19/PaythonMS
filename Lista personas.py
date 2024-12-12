personas = [
    {"nombre": "Maria", "edad": 55, "salario": 2500},
    {"nombre": "Lisa", "edad": 35, "salario": 1000},
    {"nombre": "Ana", "edad": 12, "salario": 2700},
    ]

#Media de los salarios
suma_salarios = sum(persona["salario"] for persona in personas)
num_personas = len(personas)

media_salarios = suma_salarios / num_personas

print(media_salarios)

def maximo_salario(personas):
    #Devuelve el salario más alto de la lista
    return max(persona["salario"] for persona in personas)
print(maximo_salario)