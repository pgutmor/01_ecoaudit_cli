
"""Módulo de cálculo de impacto energético y huella de carbono."""


def estimar_consumo_wh(potencia_w: float, horas_uso: float, iteraciones: int = 1) -> float:
    """Calcula el consumo energético total en Vatios-hora (Wh).

    Multiplica la potencia por las horas de uso y las iteraciones del proceso.
    """
    return potencia_w * horas_uso * iteraciones


def calcular_huella_co2(consumo_wh: float, factor_emision: float = 0.23) -> float:
    """Calcula la huella de carbono en kg de CO2.

    Convierte el consumo de Wh a kWh y lo multiplica por el factor de emisión.
    """
    consumo_kwh = consumo_wh / 1000.0
    huella_co2 = consumo_kwh * factor_emision
    return huella_co2
