from moneda import Moneda


class Conversor:
    # Clase que realizas conversiones de monedas usando tasas de cambio respecto a ARS.
    def convertir(self, cantidad, moneda_origen, moneda_destino):
        cantidad_en_ars = cantidad / moneda_origen.tasa_cambio
        cantidad_convertida = cantidad_en_ars * moneda_destino.tasa_cambio
        return cantidad_convertida


if __name__ == "__main__":
    # Crear instancias de Moneda con tasas de ejemplo (respecto al Peso)
    ars = Moneda("Peso", "ARS", 1.0)
    usd = Moneda("Dólar", "USD", 0.00076)
    eur = Moneda("Euro", "EUR", 0.00065)

conversor = Conversor()
# Creamos el conversor de monedas (hardcodeado)

# Ejemplo 1
cantidad = 100
resultado = Conversor.convertir(cantidad, usd, ars)
print(f"{usd.simbolo}{cantidad} equivalen a: {ars.simbolo}{resultado:.2f}")

# Ejemplo 2
cantidad = 250.73
resultado = Conversor.convertir(cantidad, eur, usd)
print(f"{eur.simbolo}{cantidad} equivalen a: {usd.simbolo}{resultado:.2f}")
