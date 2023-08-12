# Hangman guessing game.
# Description: 6 Chances to guess the word, otherwise you lose. Entering
# the same letter that is revealed doesn't count as a mistake.
# By: Kaushal Bhingaradia
# Date: August/11/2023
# IMPORTANT: install random-word using 'pip install random-word' (without
# quotation marks).
from random_word import RandomWords

# the hangman body aka the sprites. Top to bottom!
head = f"(x_x)\n"
left_arm = f"/`"
torso = f"|"
right_arm = f"`\ \n"
left_leg = f" /"
right_leg = f"`\ \n"

# Gets the magic random word for the game.
# You can mod it to put your own list of random words instead of using the
# random-word lib.

# Generate the random word for guessing
r = RandomWords()
random_word = r.get_random_word()
# print(random_word)

print("Welcome to Hangman. Let's play!")
print("-------------------------------")
# determine the difficulty of the random word based on its length.
length = int(len(random_word))
print(f"\nThis is {length} letter word!")
if length <= 6:
    print(f'Difficulty: Easy\n')
elif 6 < length <= 9:
    print(f'Difficulty: Medium\n')
else:
    print(f'Difficulty: Hard\n')

# blur some of the letters for guessing. Every odd  letter is blurred
# with a "_".
# store random word with blurs as a list named blurred_word
blurred_word = []
# use string_word as a variable to convert blurred_word list back to string.
string_word = ' '
for count, word in enumerate(random_word):
    blurred_word.append(word)

    # python counts from 0 instead of 1 so %2 will only blur odd index.
    if count % 2 == 0:
        # blurs the random word
        blurred_word[count] = '_'
# convert the list of the blurred_word into a clean readable string.
print(f"\n{string_word.join(blurred_word)}\n")


# Using this function to find the indexes in the random word to help
# update the indexes on the blurred word to reveal the correct letter once the
# guess word matches a letter in the random word.
def find_indexes(r_word, letter):
    list_indexes = []
    for r_index, char in enumerate(r_word):
        if char == letter:
            list_indexes.append(r_index)
    return list_indexes


# global mistake counter
mistake = 0

# This is the core code of hangman guessing game !
game_running = True
while game_running:
    try:
        # count number of mistakes. If 6 then game over!
        # Ask for user input
        guess = str(input('\nGuess a letter:\n')).lower()

        # if the guessed letter is correct then replace the blur with the
        # correct letter
        if guess[0] in random_word:
            indexes = find_indexes(random_word, guess[0])
            for i in indexes:
                blurred_word[i] = guess[0]
            print(f"\n{string_word.join(blurred_word)}\n")

        # if you guess wrong, it counts as a mistake. The mistake counter adds
        # up and will eventually create a full hangman, which is game over!
        if guess[0] not in random_word:
            mistake += 1
            print(f"Oops the letter '{guess[0]}' is not it! mistake: {mistake}")
            print(f"{string_word.join(blurred_word)}\n")

        if mistake == 1:
            print(head)

        if mistake == 2:
            print(head + left_arm)

        if mistake == 3:
            print(head + left_arm + torso)

        if mistake == 4:
            print(head + left_arm + torso + right_arm)

        if mistake == 5:
            print(head + left_arm + torso + right_arm + left_leg)

        # game over if the mistake counter adds up to 6. Break out of while
        # loop and tells player they lost!
        if mistake == 6:
            print(head + left_arm + torso + right_arm + left_leg + right_leg)
            game_running = False
            print('GAME OVER: YOU LOST! '
                  f'THE CORRECT WORD WAS --> {random_word}')

        # Checks if there is any more blurs left. If the word is complete it
        # breaks out of while loop and tells player they won!
        if '_' not in blurred_word:
            game_running = False
            print(f'GAME OVER: YOU WON! '
                  f'YOU CORRECTLY GUESSED THE WORD --> {random_word}')
    except Exception as e:
        print(e)
        continue
