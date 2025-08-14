from moneda import Moneda
from conversor import Conversor


class ServicioConversion:
    # Maneja la lógica de negocio para buscar monedas y realizar conversiones.
    def __init__(self, catalogo: dict):
        # Args: catalogo: Diccionario que mapea códigos de monedas a objetos Moneda.
        self.catalogo = catalogo
        self.conversor = Conversor()

    def obtener_moneda(self, codigo_moneda: str) -> Moneda:
        # Busca una moneda por su código.
        return self.catalogo[codigo_moneda]

    def convertir(self, cantidad: float, codigo_origen: str, codigo_destino: str) -> float:
        # Convierte una cantidad de una moneda a otra usando sus códigos.
        moneda_origen = self.obtener_moneda(codigo_origen)
        moneda_destino = self.obtener_moneda(codigo_destino)
        return self.conversor.convertir(cantidad, moneda_origen, moneda_destino)
