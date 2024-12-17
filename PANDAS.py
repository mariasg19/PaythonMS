import pandas as pd

# SERIES
serie1 = pd.Series([40, 20, 20, 40])
serie2 = pd.Series([10, 20, 10, 20])

print(f"Mi serie en Pandas es: {serie1}")

# Quiero el segundo elemento
print("\nValor en el índice 'c':", serie1[2])

#SUMA
suma = serie1 + serie2
print("Suma:\n", suma)

#RESTA
resta = serie1 + serie2
print("Suma:\n", resta)

# Slicing (primeros 2 elementos)
slicing_serie1 = serie1[:2]
slicing_serie2 = serie2[2:]
print(f"mis Slicing son \n {slicing_serie1} y {slicing_serie2}")

#Combinar ambas subseries
serie_combinada = pd.concat([slicing_serie1, slicing_serie2], ignore_index=True)
print("Serie combinada:\n", serie_combinada)

# Operaciones básicas en la serie combinada
suma = serie_combinada.sum()  # Suma de todos los elementos
maximo = serie_combinada.max()  # Valor máximo

print("\nSuma:", suma)
print("Valor máximo:", maximo)
