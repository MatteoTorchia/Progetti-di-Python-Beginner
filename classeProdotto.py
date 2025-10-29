class Prodotto:
    def __init__(self, id, nome, prezzo, quantita):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
    

def aggiungi_prodotto_a_inventario(inventario, prodotto):
    inventario.append(prodotto)
    return inventario

def descrivi_prodotto(prodotto):
    print("\nDescrizione del prodotto:")
    print(f"ID: {prodotto.id}, Nome: {prodotto.nome}, Prezzo: {prodotto.prezzo}, Quantità: {prodotto.quantita}")

def aggiorna_prezzo(prodotto, nuovo_prezzo):
    vecchio_prezzo = prodotto.prezzo
    prodotto.prezzo = nuovo_prezzo
    print(f"\nIl prezzo è stato aggiornato da {vecchio_prezzo} a {nuovo_prezzo} $")
    return prodotto.prezzo

def cerca_prodotto_per_id(inventario, id_cercato):
    for prodotto in inventario:
        if id_cercato == prodotto.id:
            return prodotto
    print(f"Non è stato trovato un prodotto con ID: {id_cercato}.")
    return None
    
# --- Flusso Principale ---
inventario = []

mela = Prodotto(1, "mela", 0.50, 100)
aggiungi_prodotto_a_inventario(inventario, mela)
descrivi_prodotto(mela)

aggiorna_prezzo(mela, 1)
descrivi_prodotto(mela)

cerca_prodotto_per_id(inventario, 1)
cerca_prodotto_per_id(inventario, 3)
