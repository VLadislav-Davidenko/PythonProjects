from calendar import c
import random
from re import A, L
from timeit import repeat

used_letters = set()

def get_word():
    with open("words.txt") as file:
        lines = file.readlines()
        word_list = [line.rstrip() for line in lines]
        word = random.choice(word_list)
        return word

def info():
    print("Welcome dear gamer, here we will play handman")
    print("You will have 9 attempts to quess a word")
    print("To start enter yes, if you want to exit - enter exit\n")
    return input().lower() == "yes"

def check(letter):
    return len(letter) == 1

def repeat():
    answer = input("New game, enter repeat, else press enter: ")
    if answer.lower() == "repeat":
        used_letters.clear()
        main()
    else:
        quit()


def main():
    print("\nTotal attempts = 9")
    print("Let's go!\n")
    word = get_word()
    guessing = ("_ " * len(word)).rstrip()
    attempts = 0
    while attempts < 9:
        print(guessing)
        letter = (input("Your letter >> ")).lower()
        if not check(letter):
            print("Please do not cheat! ")
            attempts += 1
        if letter in used_letters:
            print("You have already used this letter, try another ")
        elif letter in word:
            for x, i in enumerate(word):
                if i == letter:
                    guessing = guessing.split()
                    guessing[x] = letter
                    guessing = " ".join(guessing)
            used_letters.add(letter)
            print(guessing)
            if "".join(guessing.split()) == word:
                if attempts == 0:
                    print("Are you a cheater ?")
                else:
                    print(f"{attempts} Attempts and you guess the word")
                repeat()
        else:
            attempts += 1
            used_letters.add(letter)
            print("\nYou are not lucky, try another")
            print(f"\nAttempts left {9 - attempts}")
        print("_"*70 + "\n")
    print("\nMaybe it is not your day\n")
    print(f"The word was {word}\n")
    repeat()

if __name__ == "__main__":
    main()
        
