import random

words = ["BLUE", "RED", "GREEN", "YELLOW", "PINK", "PURPLE", "BROWN", "ORANGE", "GRAY", "WHITE", "BLACK"]
tips = ["The color of the sky on a clear day",
        "The color of an apple",
        "The color of grass",
        "The color of the sun",
        "The color of Barbie",
        "The color of grapes",
        "The color of chocolate",
        "It's a fruit and a color",
        "The color of black + white",
        "The color of peace",
        "The color of darkness"]

def choose_random_word_and_tip():
    randoms = random.randint(0, len(words) - 1)
    return words[randoms], tips[randoms]

def show_word(word, letters_discovered):
    for letter in word:
        if letter in letters_discovered:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


chances = 6
wrong_letters = []
word, tip = choose_random_word_and_tip()
letters_discovered = set()

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

    print(f"Remaining attempts: {chances}")
    print(f"Wrong letters: {', '.join(wrong_letters)}")

if chances == 0:
    print(f"You lost! The word was: {word}")
