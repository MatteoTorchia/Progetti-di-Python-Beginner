
mela = {
    "id": 1,
    "nome" : "mela",
    "prezzo" : 0.53,
    "quantita" : 50
    }

quaderno = {
    "id": 2,
    "nome" : "quaderno",
    "prezzo" : 1.20,
    "quantita" : 100
    }

biro = {
    "id": 3,
    "nome" : "biro",
    "prezzo" : 0.25,
    "quantita" : 200
    }

inventario = [mela, quaderno, biro]

def aggiungi_prodotto(inventarioid, nome, prezzo, quantita):
    nuovo_podotto = {
        "id": id,
        "nome" : nome,
        "prezzo" : prezzo,
        "quantita" : quantita
        }
    inventario.append(nuovo_podotto)
    return inventario

def cerca_prodotto_per_id(inventario, id_cercato):
    for prodotto in inventario:
        if id_cercato == prodotto["id"]:
         return prodotto

    print(f"Prodotto con ID {id_cercato} non trovato.")
    return None

def aggiorna_quantita(inventario, id_prodotto, nuova_quantita):
   prodotto = cerca_prodotto_per_id(inventario, id_prodotto)
   if prodotto == None:
      return False
   else:
      quantita_non_aggiornata = prodotto["quantita"]
      prodotto["quantita"] = nuova_quantita
      print(f"La quantità del prodotto è stata aggiornata da {quantita_non_aggiornata} a {nuova_quantita}.")
      return True

# --- Flusso Principale ---

aggiorna_quantita(inventario, 9, 777)