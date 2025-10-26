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
        print("You already used these letters: ", " ".join(usedLetters))
        if lives > 1:
            print(f"You have {lives} lives remaining.")
        else:
            print(f"You have {lives} life remaining.")

        # wordList = [letter if letter in usedLetters else "-" for letter in word]
        # Versione Lunga e Dettagliata (Equivalente)
        wordList = []
        for letter in word:
            if letter in usedLetters:
                wordList.append(letter)
            else:
                wordList.append("-")
        print("Current word: " , " ".join(wordList))

        userLetter = input("Guess a letter:").upper()
        if userLetter in (alphabet - usedLetters):
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print(f"You guessed! '{userLetter}' is in the word")
            else:
                print(f"'{userLetter}'is not in the word.")
                lives -= 1  # lives = lives - 1

        elif userLetter in usedLetters:
            print("You have already tried this character. Please give a different input")
        
        else:
            print("Invalid character. Please give a different input")

    # gets here when len(wordLetters) == 0 or lives == 0
    if len(wordLetters) == 0:
        print(f"\nYou won!!! The word was '{word}'!")
    else:
        print(f"You've run out of lives :( \n The word was '{word}'. \nGAME OVER.")

hangman()