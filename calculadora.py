
"""Módulo de cálculo de impacto energético y huella de carbono."""


def estimar_consumo_wh(potencia_w: float, horas_uso: float, iteraciones: int = 1) -> float:
    """Calcula el consumo energético total en Vatios-hora (Wh).

    Multiplica la potencia por las horas de uso y las iteraciones del proceso.
    """
    return potencia_w * horas_uso * iteraciones


def calcular_huella_co2(consumo_wh: float, factor_emision: float = 0.23) -> float:
    """Calcula la huella de carbono a partir del consumo energético.

    Convierte el consumo de Wh a kWh y multiplica por el factor de emisión.
    """
    kwh = consumo_wh / 1000.0
    emisiones = kwh * factor_emision
    return emisiones


