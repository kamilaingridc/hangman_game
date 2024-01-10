import random


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

def remove_word(word_to_remove):
    with open('palavrasedicas.txt', 'r') as file:
        lines = file.readlines()
    with open('palavrasedicas.txt', 'w') as file:
        for line in lines:
            if not line.startswith(word_to_remove):
                file.write(line)

def add_new_word(word, tip):
    with open('palavrasedicas.txt', 'a') as file:
        file.write(f"\n{word};{tip}\n")

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

    print(f"Remaining attempts: {chances}")
    print(f"Wrong letters: {', '.join(wrong_letters)}")

if chances == 0:
    print(f"You lost! The word was: {word}")

choice = input("\nDo you want to add or remove words? [1]Add / [2]Remove / [3]No: ").upper()
if choice == '1':
    new_word = input("Enter a new word: ").upper()
    new_tip = input("Enter a tip for the word: ")
    add_new_word(new_word, new_tip)
    print(f"Added {new_word} with tip: {new_tip} to the list.")
elif choice == '2':
    word_to_remove = input("Enter the word you want to remove: ").upper()
    remove_word(word_to_remove)
    print(f"Removed {word_to_remove} from the list.")
else:
    print("Thank you for playing!")
