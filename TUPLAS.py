#TUPLAS

# Crea una tupla 
tupla = 1,2,3

# Tupla mixta
tuplaMixta = 1, 2, "di"
# Imprimimos type para cada elemento
for elemento in tuplaMixta:
    print(f"{elemento} => {type(elemento)}")

# Convierte la tupla_mixta a un list e imprímela
listaDeTupla = list(tuplaMixta)
print(tuplaMixta)

# Modifica el elemento 1 ("dos") de la lista y vuelve a pasar la lista a tupla. 
# Imprime la tupla para ver que se ha modificado el elemento tupla_mixta[1]
listaDeTupla[1] = "Dos"
NuevaTupla = tuple(listaDeTupla)
print(NuevaTupla)

# Crea una tupla numérica y realiza las operaciones de suma, maximo y mínimo

# Si queremos hacerlo directamente
TuplaAritmetica = 1,2,3*4,4*2
print(TuplaAritmetica)

#Sumas, min y max
tupla3 = 1,2,3,4

suma = sum(tupla3)
print(f"La suma es {suma}")

maximo = max(tupla3)
print(f"El maximo de mi tupla es {maximo}")

minimo = min(tupla3)
print(f"El minimo de mi tupla es {minimo}")