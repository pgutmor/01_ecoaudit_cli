# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: [pgutmor] & [pgarmen]
# =====================================================================

from calculadora import estimar_consumo_wh, calcular_huella_co2

while True:
    print("\n=========================================")
    print("  🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")

    entrada = input("\nSeleccione una opción (1-3): ").strip()

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

            if potencia <= 0:
                print("⚠️ La potencia debe ser mayor que 0.")
                continue

            if horas < 0:
                print("⚠️ Las horas no pueden ser negativas.")
                continue

            if iteraciones < 0:
                print("⚠️ Las iteraciones no pueden ser negativas.")
                continue

            # SIMULACIÓN ITERATIVA PASO A PASO
            print("\nIniciando simulación ciclo a ciclo...")

            consumo_ciclo = estimar_consumo_wh(potencia, horas, 1)
            consumo_acumulado = 0.0
            ciclo = 1

            while ciclo <= iteraciones:
                consumo_acumulado = consumo_acumulado + consumo_ciclo
                print(
                    f" [Ciclo {ciclo}] Consumo acumulado parcial: "
                    f"{consumo_acumulado:.2f} Wh"
                )
                ciclo = ciclo + 1

            # Cálculo final
            consumo = estimar_consumo_wh(potencia, horas, iteraciones)
            huella = calcular_huella_co2(consumo)

            print(f"\n✅ Resultados calculados para '{proceso}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono: {huella:.4f} g CO2")

            # Guardado en CSV
            with open("auditoria.csv", mode="a", encoding="utf-8") as archivo:
                archivo.write(
                    f"{proceso},{potencia},{horas},{iteraciones},"
                    f"{consumo:.2f},{huella:.4f}\n"
                )

            print("💾 Registro guardado correctamente.")

        except ValueError:
            print("⚠️ Error: introduce valores numéricos válidos.")

    elif opcion == 2:
        print("\n========== HISTORIAL DE AUDITORÍAS ==========")

        try:
            with open("auditoria.csv", mode="r", encoding="utf-8") as archivo:
                contenido = archivo.read()

                if contenido:
                    print(contenido)
                else:
                    print("ℹ️ El archivo está vacío.")

        except FileNotFoundError:
            print("ℹ️ Aún no existen registros. Realiza una auditoría primero.")

    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break

    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")





