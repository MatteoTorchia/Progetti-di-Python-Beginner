catalog = {"apple": 0.5, "orange": 0.6, "bread": 1.0, }
cart = []


# --- Main Flow ---
print("--- Welcome to the shop! ---")

for i in catalog:
    print(i, catalog[i])

while True:
        request = input("What do you want to buy? (type 'stop' to end) ")

        if request == "stop":
            break
        if request in catalog:
            cart.append(request)
            print(f"Item '{request}' added to cart!")
        else:
            print(f"There is no item such as '{request}'\nTry something different.")

