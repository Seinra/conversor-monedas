class Moneda:
    """
    Clase que representa una moneda con sus propiedades básicas para un conversor de divisas.
    Almacena el nombre, símbolo y tasa de cambio respecto al Peso Argentino (ARS).
    """

    def __init__(self, nombre, simbolo, tasa_cambio):
        # Inicializa una moneda con sus atributos.
        self.nombre = nombre
        self.simbolo = simbolo
        self.tasa_cambio = float(tasa_cambio)

    def __str__(self):
        return f"{self.nombre} {self.simbolo} - Tasa {self.tasa_cambio}"
