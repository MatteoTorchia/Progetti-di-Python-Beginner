catalog = {"apple": 0.5, "orange": 0.6, "bread": 1.0, }
cart = ()
flag=0

# --- Main Flow ---
print("--- Welcome to the shop! ---")
for i in catalog:
    print(i, catalog[i])
while flag==0:
    request = input("What do you want to buy? ")
    for i in catalog:
        if request == i:
            n = input(f"How many {i} do you want? ")
            flag = 1
            break
        if i == len(catalog)-1:
            print(f"There is no item such as '{request}'\nTry something different.")