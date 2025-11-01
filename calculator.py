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
        op = input("Scegli un operatore matematico tra quelli disponibili: +, -, *, /. ")
        try:
            if op == "+":
                return addizione(a, b)
            elif op == "-":
                return sottrazione(a, b)
            elif op == "*":
                return moltiplicazione(a, b)
            elif op == "/":
                return divisione(a, b)                
        except ValueError:
            print("Non hai scelto un operatore disponibile.")


def addizione(a, b):
    c = a + b
    return c

def sottrazione(a, b):
    c = a - b
    return c

def moltiplicazione(a, b):
    c = a * b
    return c

def divisione(a, b):
    if b == 0:
        c = print("Non è possibile dividere per zero.")
        return c
    else:
        c = a / b
        return c


# --- Flusso Principale ---
a = ottieni_membro(1)
b = ottieni_membro(2)

print(ottieni_operatore_ed_esegui(a, b))