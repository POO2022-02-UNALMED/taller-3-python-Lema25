class Marca:
    def __init__ (self, nomb):
        self._nombre = nomb
    
    def setNombre(self, nomb):
        self._nombre = nomb

    def getNombre(self):
        return self._nombre