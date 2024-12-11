#Listas por comprension


temperaturas = [0, 4, -150, -196, -400, 0, 10]
limite = -196

# Seleccionamos las que si que son gaseosas
tempGas = [x for x in temperaturas if x > limite]

# Imprimir las temperaturas resultantes
print(f"Las temeperaturas de nuestro experimento que si que valen son: {tempGas}")