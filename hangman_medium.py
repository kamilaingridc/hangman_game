import random
import time


def archive_words():
    with open('palavrasedicas.txt', 'r') as file:
        lines = file.read().splitlines()
        random_line = random.choice(lines)
        word, tip = random_line.split(";")
        return word, tip


def show_word(word, letters_discovered):
    for letter in word:
        if letter in letters_discovered:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


chances = 6
wrong_letters = []
word, tip = archive_words()
letters_discovered = set()
print(f"Welcome to our hangman game! You have {chances} chances. Good luck! ")

# Loop principal do jogo
while chances > 0:
    print(f"Tip: {tip}")
    show_word(word, letters_discovered)

    letter = input("Choose a letter or guess the word: ").upper()

    if letter == word:
        print("Congratulations, you got the word right!")
        break

    if letter in word:
        print("Correct letter!")
        letters_discovered.add(letter)
        if letters_discovered == set(word):
            print(f"You got the word right! The word was: {word}")
            break
    else:
        print("Wrong letter.")
        wrong_letters.append(letter)
        chances -= 1

    time.sleep(1)
    print(f"Remaining attempts: {chances}")
    print(f"Wrong letters: {', '.join(wrong_letters)}")

if chances == 0:
    print(f"You lost! The word was: {word}")
