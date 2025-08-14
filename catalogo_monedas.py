from moneda import Moneda

# Diccionario que mapea códigos de monedas a instancias de Moneda
CATALOGO_MONEDAS = {
    "ARS": Moneda("Peso", "ARS", 1.0),
    "USD": Moneda("Dólar", "USD", 0.00076),
    "EUR": Moneda("Euro", "EUR", 0.00065)
}
