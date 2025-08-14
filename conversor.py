class Conversor:
    # Clase que realizas conversiones de monedas usando tasas de cambio respecto a ARS.
    def convertir(self, cantidad: float, moneda_origen, moneda_destino) -> float:
        cantidad_en_ars = cantidad / moneda_origen.tasa_cambio
        cantidad_convertida = cantidad_en_ars * moneda_destino.tasa_cambio
        return cantidad_convertida
