from televisores.control import Control
from televisores.marca import Marca

class TV:
    numTV=0
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    def setMarca(self, marca):
        if isinstance(marca, Marca):
            self.marca = marca
    def getMarca(self):
        return self.marca

    def setControl(self, control):
        if isinstance(control, Control):
            self.control = control
    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen):
        if((volumen>=0 and volumen<=7) and self.estado==True):
                self.volumen = volumen
    def getVolumen(self):
        return self.volumen

    def setCanal(self, canal):
        if((canal>=1 and canal<=120) and self._estado==True):
                self.canal = canal
    def getCanal(self):
        return self.canal

    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if(self.estado==True and self.canal<120):
            self.canal = self.canal +1
    def canalDown(self):
        if(self.estado==True and self.canal>1):
            self.canal = self.canal -1

    def volumenUp(self):
        if(self.estado==True and self.volumen<7):
            self.volumen = self.volumen +1
    def volumenDown(self):
        if(self._estado==True and self.volumen>0):
            self.volumen = self.volumen -1

    def getEstado(self):
        return self.estado

    @classmethod
    def getNumTV(self):
        return self.numTV
    @classmethod
    def setNumTV(self, numTV):
        self.numTV = numTV
