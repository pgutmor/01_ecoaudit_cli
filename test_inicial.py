nombre_auditor = input("Introduce tu nombre: ").strip()
consumo_str = input("Introduce el consumo en Wh: ").strip()
consumo_wh = float(consumo_str)
print(f"--- INFORME PARA: {nombre_auditor.upper()} ---")
print(f"El consumo registrado es de {consumo_wh} Wh.")
consumototal = consumo_wh*24
print(f"Tu consumo total es de {consumototal} al dia")