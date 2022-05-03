#Step 3
from dis import dis
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
incorrect_guesses = []
guess_count = 0

#Create blanks
display = []
for _ in range(word_length):
	display.append('_')

while '_' in display:
    print(f'{display}')
    
    guess = input("Guess a letter: ").lower()
    guess_count += 1

    for letter_pos in range(len(chosen_word)):
        if guess == chosen_word[letter_pos]:
            display[letter_pos] = guess
        
    if guess not in display:
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
        else:
            print(f'{guess} has been previously tried')


if '_' not in display:
    print(f'{display}')
    print(f'Game over! You found the word: {chosen_word} in {guess_count} guesses.')
    print(f'Incorrect guesses: {incorrect_guesses}')