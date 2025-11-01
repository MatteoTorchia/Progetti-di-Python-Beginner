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
        print("Non è possibile dividere per zero.")
    else:
        c = a / b
        return c


# --- Flusso Principale ---


a = ottieni_membro(1)
b = ottieni_membro(2)

op = input("Scegli l'operatore matematico. +, -, *, /")

if op == "+":
    print(addizione(a, b))
elif op == "-":
    print(sottrazione(a, b))
elif op == "*":
    print(moltiplicazione(a, b))
elif op == "/":
    print(divisione(a, b))
else:
    print("Non hai scelto un operatore disponibile.")