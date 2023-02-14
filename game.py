from random import choice
from hangman_graphic import HANGMAN
from wordlist import words
from replit import clear


# choosing a word to guess from wordlist randomly
guessing_word = choice(words)

display = []
guessing_length = len(guessing_word)
# setting up amout of lives
lives = 6

# hiding chosen word to guess
[display.append("_") for _ in range(guessing_length)]
print(f"word for you to guess: \n {''.join(display)}\n")

game_over = False

while not game_over:
    # user guesses a letter of guessing word
    guess = input('Guess a letter: ').lower()
    # clearing the console screen
    clear()

    if guess in display:
        print(f"You've already guessed '{guess}' letter")
    for index in range(guessing_length):
        letter = guessing_word[index]
        if letter == guess:
            display[index] = letter
    if guess not in display:
        print(f"You've guessed '{guess}' that is not in the word. You lose a life!")
        lives -= 1
        print(HANGMAN[lives])
        if lives == 0:
            game_over = True
            print("You lost!")

    print(f"{''.join(display)}")

    if "_" not in display:
        game_over = True
        print('You won! Your guessed word is: ', guessing_word)

