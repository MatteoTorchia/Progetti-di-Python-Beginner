def ottieni_membro(n):
    while True:
        try:
            a = float(input(f"Inserisci il {n}° membro dell'operazione: "))
            if a.is_integer():
                return int(a)
            else:
                return a
        except ValueError:
            print("Il valore inserito non è valido. Prova ad inserire un numero.")

def ottieni_operatore_ed_esegui(a, b):
    while True:
        op = input("Scegli un operatore matematico tra quelli disponibili: +, -, *, /, ** : ")
        if op == "+":
            return addizione(a, b)
        elif op == "-":
            return sottrazione(a, b)
        elif op == "*":
            return moltiplicazione(a, b)
        elif op == "/":
            return divisione(a, b)
        elif op == "**":
            return esponenziale(a, b)                
        else:
            print("Non hai scelto un operatore disponibile.")


def addizione(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: Non è possibile dividere per zero."
    else:
        return a / b

def esponenziale(a, b):
    if a == 0 and b == 0:
        return "0^0 è una forma indeterminata."
    return a ** b


# --- Flusso Principale ---
a = ottieni_membro(1)
b = ottieni_membro(2)

print(ottieni_operatore_ed_esegui(a, b))