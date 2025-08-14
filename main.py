from catalogo_monedas import CATALOGO_MONEDAS
from servicio_conversion import ServicioConversion

if __name__ == "__main__":

    # Crea el servicio de conversión con el catálogo.
    servicio = ServicioConversion(CATALOGO_MONEDAS)


# Ejemplo 1
cantidad = 100
resultado = servicio.convertir(cantidad, "USD", "ARS")
print(f"USD {cantidad} equivalen a: ARS {resultado:.2f}")

# Ejemplo 2
cantidad = 250.73
resultado = servicio.convertir(cantidad, "EUR", "USD")
print(f"EUR {cantidad} equivalen a: USD {resultado:.2f}")
