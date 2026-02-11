catalog = {"apple": 0.5, "orange": 0.6, "bread": 1.0, }
cart = {}

def get_total_price(cart, price_dict):
    total = 0.00
    for item in cart:
        total += price_dict[item]
    return total       

# --- Main Flow ---
print("--- Welcome to bagio's shop! ---")
print("Those are the available products:")

for item in catalog:
    print(f"- {item}: {catalog[item]} €")

while True:
        request = input("\nWhat do you want to buy? (type 'stop' to end) ")

        if request == "stop":
            break
        if request in catalog:
            cart.append(request)
            print(f"Item '{request}' added to cart!")
        else:
            print(f"I'm sorry, there is no item such as '{request}'\nTry something different.")


print("---- Receipt ----")
for item in cart:
    print(f"- {item}: {catalog[item]} €")

total = get_total_price(cart, catalog)
print(f"\n-----Total: {total} €")

#---------------------------------------
#TODO:
# (Dizionari): Cambi la struttura del cart.
# Invece di essere una lista ['apple', 'apple'],
# diventa un dizionario {'apple': 2}.
# Questo richiede di riscrivere la funzione del totale.