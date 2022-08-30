class Control:
    def __init__(self):
        self.tv = None

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, can):
        self.tv.setCanal(can)
    
    def enlazar(self, t):
        self.tv = t
        self.tv.setControl(self)

    def setTv(self, t):
        self.tv = t

    def getTv(self):
        return self.tv
    