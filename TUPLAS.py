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

# Calcula los cuadrados de la tupla con una función de compresión

tuplaCuadrados = tuple(x**2 for x in tupla3)

# Imprimir la nueva tupla con los cuadrados
print(tuplaCuadrados)

# Desempaqueta la tupla en tantas variables como elementos tenga

tupla4 = 4,2,6,7,"3"
a,b,c,d,e = tupla4
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")