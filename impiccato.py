import random
import string

from words import words

def getValidWord(words):
    word = random.choice(words)
    while " " in word or "-" in word or "_" in word:
        word = random.choice(words)

    return str(word.upper())  # so every word is in uppercase

def hangman():
    word = getValidWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 10

    while len(wordLetters) > 0 and lives > 0:
        print("\n")
        print("Hai già usato queste lettere: ", " ".join(usedLetters))
        if lives > 1:
            print(f"Hai ancora {lives} vite rimaste.")
        else:
            print(f"Hai ancora {lives} vita rimasta.")

        # wordList = [letter if letter in usedLetters else "-" for letter in word]
        # Versione Lunga e Dettagliata (Equivalente)
        wordList = []
        for letter in word:
            if letter in usedLetters:
                wordList.append(letter)
            else:
                wordList.append("-")
        print("La parola: " , " ".join(wordList))

        userLetter = input("Indovina una lettera:").upper()
        if userLetter in (alphabet - usedLetters):
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print(f"Hai indovinato! '{userLetter}' fa parte della parola")
            else:
                print(f"'{userLetter}' non fa parte della parola.")
                lives -= 1  # lives = lives - 1

        elif userLetter in usedLetters:
            print("Hai già provato questa lettera. Prova qualcosa di diverso.")
        
        else:
            print("Carattere non valido. Prova qualcosa di diverso")

    # gets here when len(wordLetters) == 0 or lives == 0
    if len(wordLetters) == 0:
        if lives > 1:
            print(f"\nHai vinto con {lives} vite rimanenti!!! La parola era '{word}'!")
        else:
            print(f"\nHai vinto con una sola vita rimanente, per un pelo!!! La parola era '{word}'!")

    else:
        print(f"Hai finito le vite :( \n La parola era '{word}'. \nGAME OVER.")

hangman()