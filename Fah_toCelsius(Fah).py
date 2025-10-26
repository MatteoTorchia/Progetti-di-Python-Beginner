def Fah_toCelsius(Fah):
    if Fah >= -459.67:
        return(Fah - 32) * 5/9
    else:
        return print("Hai inserito un valore inferiore allo zero assoluto!")

inputFah = float(input("Inserisci la temperatura espressa in fahrenheit"))
print(Fah_toCelsius(inputFah))
