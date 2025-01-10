import random
import datetime
import json

def generar_numeros_aleatorios(cantidad=1000, rango=(0, 99999)):
    """Genera una cantidad específica de números aleatorios entre el rango especificado."""
    return {str(random.randint(rango[0], rango[1])).zfill(5) for _ in range(cantidad)}

def mostrar_reglas():
    """Muestra las reglas o detalles de los premios disponibles."""
    print("Reglas del programa de premios:")
    print("1. Premios fijos para ciertos números.")
    print("2. Premios por 'serie' (números que comienzan con 724, 400, 118, o 777).")
    print("3. Premios por terminación en ciertas cifras.")
    print("4. Premios aleatorios de 100 € asignados a 1000 números.")
    print("\n¡Introduce tu número para saber si has ganado!")

def calcular_premio(numero, random_numeros_aleatorios):
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
    
    # Premio por terminar en 0 (esto es lo que faltaba verificar correctamente)
    if numero.endswith("0"):
        premio_total += 20
    
    # Premiar aleatoriamente 1000 números con 100€
    if numero in random_numeros_aleatorios:
        premio_total += 100

    return premio_total

def mostrar_saldo_acumulado(historial):
    """Muestra el saldo acumulado de premios ganados."""
    saldo = sum(historial)
    print(f"Tu saldo acumulado es: {saldo} euros")

def generar_informe(numero, premio, archivo="informe_premios.txt"):
    """Genera un informe detallado sobre el número verificado y el premio obtenido."""
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo, "a") as file:
        file.write(f"{fecha} - Número: {numero}, Premio: {premio} euros\n")
    print(f"Informe generado para el número {numero} con un premio de {premio} euros.")

def repetir_verificacion(numero, random_numeros_aleatorios):
    """Permite repetir la verificación de un número sin tener que ingresarlo de nuevo."""
    print(f"Revisando el número {numero} nuevamente...")
    return calcular_premio(numero, random_numeros_aleatorios)

def mostrar_estadisticas(historial):
    """Muestra estadísticas sobre los premios obtenidos por el usuario."""
    premios = {
        "100": 0,
        "1000": 0,
        "2000": 0,
        "6000": 0,
        "20000": 0,
        "50000": 0,
        "125000": 0,
        "400000": 0
    }
    
    for premio in historial:
        if premio >= 100000:
            premios["400000"] += 1
        elif premio >= 125000:
            premios["125000"] += 1
        elif premio >= 50000:
            premios["50000"] += 1
        elif premio >= 20000:
            premios["20000"] += 1
        elif premio >= 6000:
            premios["6000"] += 1
        elif premio >= 2000:
            premios["2000"] += 1
        elif premio >= 1000:
            premios["1000"] += 1
        elif premio >= 100:
            premios["100"] += 1
    
    print("Estadísticas de premios obtenidos:")
    for premio, cantidad in premios.items():
        print(f"Premios de {premio} euros: {cantidad}")

def main():
    random_numeros_aleatorios = generar_numeros_aleatorios()
    historial_premios = []
    
    while True:
        mostrar_reglas()
        numero = input("Introduce tu número de décimo (del 00000 al 99999): ")
        resultado = calcular_premio(numero, random_numeros_aleatorios)
        
        if isinstance(resultado, int):
            print(f"Has ganado {resultado} euros.")
            historial_premios.append(resultado)
            generar_informe(numero, resultado)  # Generar informe por cada verificación
        else:
            print(resultado)
        
        otra_verificacion = input("¿Quieres verificar otro número? (sí/no): ").strip().lower()
        if otra_verificacion == "sí":
            repetir = input("¿Quieres repetir la verificación del último número ingresado? (sí/no): ").strip().lower()
            if repetir == "sí":
                repetir_verificacion(numero, random_numeros_aleatorios)
        else:
            break

    mostrar_saldo_acumulado(historial_premios)
    mostrar_estadisticas(historial_premios)

if __name__ == "__main__":
    main()


