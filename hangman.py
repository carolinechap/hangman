import random
import emoji

from colorama import Fore, Back, Style
from words import spell_list
from stages import display_hangman

def get_word():
    spell = []
    if len(spell_list) != 0:
        spell = random.choice(spell_list)
        return spell.upper()
    else:
        print('The invisibility spell has been used. There is no word, sorry about that. \U0001fa84')
        exit()

def play(spell):
    word_completion = "_" * len(spell)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n")
    print(Style.BRIGHT + Fore.YELLOW + "Let's play Hangman! Guess the Harry potter's spell...", emoji.emojize
    (':high_voltage:'))
    print(Fore.RED + display_hangman(tries))
    print(Style.RESET_ALL)
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        input_word = input("Please guess a letter or a word: ").upper()
        if len(input_word) == 1 and input_word.isalpha():
            if input_word in guessed_letters:
                print("You already guess the letter ", input_word)
            elif input_word not in spell:
                print(input_word, "is not in the word.")
                tries -= 1
                guessed_letters.append(input_word)
            else:
                print("Great job", input_word, "is in the spell")
                guessed_letters.append(input_word)
                spell_list = list(word_completion)
                indices = [i for i, letter in enumerate(spell) if letter == input_word]
                for index in indices:
                    spell_list[index] = input_word
                word_completion = "".join(spell_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(spell) and input_word.isalpha():
            if input_word in guessed_words:
                print("You already guess the spell ", input_word)
            if input_word != spell:
                print(input_word, "is not the word")
                tries -= 1
                guessed_words.append(input_word)
            else:
                guessed = True
                word_completion = word
        else:
            print(guess, " is not a value guess.")

        print(Fore.RED + display_hangman(tries))
        print(Style.RESET_ALL)
        print(word_completion)
        print("\n")

    if guessed:
        print(Fore.GREEN + "You made it, the spell was", spell)
    else:
        print(Fore.RED + "Sorry, you ran out of tries. The spell was", spell)

    print(Style.RESET_ALL)


def main():
    spell = get_word()
    play(spell)

    while input("Do you want to play again ? (Y/N)").upper() == "Y":
        spell = get_word()
        play(spell)

if __name__ == "__main__":
    main()
