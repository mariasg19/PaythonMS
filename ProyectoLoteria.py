def calcular_premio(numero):
    premio_total = 0
    
    # Comprobar que el número esté entre 00000 y 99999
    if not numero.isdigit() or len(numero) != 5 or int(numero) < 0 or int(numero) > 99999:
        return "El número no es válido, introdúcelo de nuevo"
    
    # Premios fijos por número
    if numero == "72480":
        premio_total += 400000
    elif numero == "40014":
        premio_total += 125000
    elif numero == "11840":
        premio_total += 50000
    elif numero == "77768" or numero == "48020":
        premio_total += 20000
    elif numero in ["37876", "72583", "74778", "45456", "45225", "97345", "75143", "60622"]:
        premio_total += 6000
    elif numero == "72479" or numero == "72481":
        premio_total += 2000
    elif numero == "40013" or numero == "40015":
        premio_total += 1250
    elif numero == "11839" or numero == "11841":
        premio_total += 960
    
    # Premios por "serie" de inicio de número
    if numero.startswith("724") or numero.startswith("400") or numero.startswith("118") or numero.startswith("777"):
        premio_total += 100
    
    # Premios por terminación en ciertas cifras
    if numero.endswith("80") or numero.endswith("14") or numero.endswith("40"):
        premio_total += 100
    
    # Premio por terminar en 0
    if numero.endswith("0"):
        premio_total += 20
    
    return premio_total

# Función principal para pedir el número al usuario
def main():
    while True:
        numero = input("Introduce tu número de décimo (del 00000 al 99999): ")
        resultado = calcular_premio(numero)
        if isinstance(resultado, int):
            print(f"Has ganado {resultado} euros.")
        else:
            print(resultado)  # Muestra mensaje de error si el número no es válido.
            continue
        
        # Preguntar si el usuario quiere verificar otro número
        otra_verificacion = input("¿Quieres verificar otro número? (sí/no): ").strip().lower()
        if otra_verificacion != "sí":
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()
