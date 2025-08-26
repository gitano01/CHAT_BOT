import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Catalogos:
    def __init__(self):
        self.catalogos = {
            "productos": ["camiseta", "pantalon", "zapatos"],
            "servicios": ["asesoria", "soporte", "instalacion"]
        }

    def get_catalogo(self, tipo):
        return self.catalogos.get(tipo, [])

    def add_item(self, tipo, item):
        if tipo in self.catalogos:
            self.catalogos[tipo].append(item)
            return True
        return False

    def remove_item(self, tipo, item):
        if tipo in self.catalogos and item in self.catalogos[tipo]:
            self.catalogos[tipo].remove(item)
            return True
        return False
