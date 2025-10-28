class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self):
        return f"Veicolo: {self.marca} {self.modello}, Anno: {self.anno}"
    
    def aggiorna_anno(self, nuovo_anno):
        self.anno = nuovo_anno

class AutoElettrica(Veicolo):
    def __init__(self, marca, modello, anno, batteria_kwh):
        super().__init__(marca, modello, anno)
        self.batteria_kwh = batteria_kwh
    
    def descrivi_veicolo(self):
        descrizione_base = super().descrivi_veicolo()
        return f"{descrizione_base} | Batteria: {self.batteria_kwh} kWh"


# --- Flusso Principale ---
v1 = Veicolo("Ford", "Model 3", 2023)

Veicolo.descrivi_veicolo(v1)
v1.aggiorna_anno(2024) 
print(v1.descrivi_veicolo())

e1 = AutoElettrica("Tesla", "Model Y", 2024, 75)
e1.descrivi_veicolo()

print(f"Batteria: {e1.batteria_kwh} kWh")
print(e1.descrivi_veicolo())