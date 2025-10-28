class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self):
        print(self.marca, self.modello, self.anno)
    
    def aggiorna_anno(self, nuovo_anno):
        self.anno = nuovo_anno

class AutoElettrica(Veicolo):
    def __init__(self, marca, modello, anno, batteria_kwh):
        super().__init__(marca, modello, anno)
        self.batteria_kwh = batteria_kwh


v1 = Veicolo("Ford", "Model 3", 2023)

Veicolo.descrivi_veicolo(v1)
v1.aggiorna_anno(2024) 
v1.descrivi_veicolo()

e1 = AutoElettrica("Tesla", "Model Y", 2024, 75)
e1.descrivi_veicolo()

print(f"Batteria: {e1.batteria_kwh} kwh")