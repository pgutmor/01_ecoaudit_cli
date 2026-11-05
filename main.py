
# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: [pgutmor] & [pgarmen]
# =====================================================================

from calculadora import estimar_consumo_wh, calcular_huella_co2

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")

    entrada = input("\nSeleccione una opción (1-3): ").strip()

    # Validación de la opción introducida
    try:
        opcion = int(entrada)
    except ValueError:
        print("⚠️ Error: Debe introducir un número entero.")
        continue

    if opcion == 1:
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")

        proceso = input("Nombre del equipo/proceso: ").strip()

        try:
            potencia = float(input("Potencia consumida en Vatios (W): "))
            horas = float(input("Horas de uso diario: "))
            iteraciones = int(input("Introduce número de iteraciones: "))

            # Validación de potencia
            if potencia <= 0:
                print("⚠️ La potencia debe ser mayor que 0.")
                continue

            # Validación de horas
            if horas < 0:
                print("⚠️ Las horas no pueden ser negativas.")
                continue

            # Validación de iteraciones
            if iteraciones < 0:
                print("⚠️ Las iteraciones no pueden ser menores que 0.")
                continue

            print(f"✔️ Configurado con éxito para {iteraciones} iteraciones.")

            # Cálculo del consumo energético
            consumo = estimar_consumo_wh(potencia, horas, iteraciones)

            # Cálculo de la huella de carbono
            huella = calcular_huella_co2(consumo)

            # Mostrar resultados
            print(f"\n✅ Resultados calculados para '{proceso}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono estimada: {huella:.4f} g CO2")

            # Guardado persistente en el archivo CSV
            with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
                archivo.write(
                    f"{proceso},{potencia},{horas},{iteraciones},{consumo:.2f},{huella:.4f}\n"
                )

            print("💾 Registro guardado con éxito en 'auditorias.csv'.")

        except ValueError:
            print("⚠️ Error de formato: introduce valores numéricos válidos.")

    elif opcion == 2:
        print("\n================ HISTORIAL DE AUDITORÍAS ================")

        try:
            # Abrimos el archivo CSV en modo lectura
            with open("auditorias.csv", mode="r", encoding="utf-8") as archivo:

                # Leemos todo el contenido
                contenido = archivo.read()

                # Mostramos el histórico
                print(contenido)

        except FileNotFoundError:
            print("ℹ️ Aún no existen registros. Realiza una auditoría primero.")

    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break

    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")

