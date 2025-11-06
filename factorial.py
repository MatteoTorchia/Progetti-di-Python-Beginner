def get_int():
    while True:
        try:
            n = int(input("Use this calculator to calculate the factorial n! -- Insert n: "))
            return n
        except ValueError:
            print("Error: Invalid character.")

def factorial_function(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        product = 1
        for i in range(2, n + 1):
            product = product * i
        return product


# --- Main Flow ---
print(factorial_function(get_int()))


# print(factorial_function(0))
# print(factorial_function(1))
# print(factorial_function(-3))
# print(factorial_function(2))
# print(factorial_function(6))