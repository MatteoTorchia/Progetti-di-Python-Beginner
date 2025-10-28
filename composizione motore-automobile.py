class Motore:
    def accendi(self):
        return "Il motore è acceso."

class Automobile:
    def __init__(self):
        self.motore = Motore()
    
    def avvia(self):
        return self.motore.accendi()


# --- Flusso Principale ---
car = Automobile()
print(car.avvia())