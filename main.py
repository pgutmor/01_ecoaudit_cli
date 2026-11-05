
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
            num_iter = int(input("Introduce número de iteraciones: "))

            # Validación de potencia
            if potencia <= 0:
                print("⚠️ La potencia debe ser mayor que 0.")
                continue

            # Validación de horas
            if horas < 0:
                print("⚠️ Las horas no pueden ser negativas.")
                continue

            # Validación de iteraciones
            if num_iter < 0:
                print("⚠️ Las iteraciones no pueden ser menores que 0.")
                continue

            print(f"✔️ Configurado con éxito para {num_iter} iteraciones.")

            # Cálculo del consumo energético
            consumo = estimar_consumo_wh(potencia, horas, num_iter)

            # Cálculo de la huella de carbono
            huella = calcular_huella_co2(consumo)

            # Mostrar resultados
            print(f"\n✅ Resultados calculados para '{proceso}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono estimada: {huella:.4f} g CO2")

        except ValueError:
            print("⚠️ Error de formato: introduce valores numéricos válidos.")

    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")

    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break

    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")
