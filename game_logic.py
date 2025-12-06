import random
from ascii_art import STAGES

# List of secret words
WORDS = ["snowman", "meltdown", "santa", "elf", "snow", "tree", "gift",
    "star", "bell", "holly", "angel", "noel", "sock", "reindeer",
    "sleigh", "cookie", "stocking", "mistletoe", "fireplace",
    "gingerbread", "icicle", "candy cane", "ornament", "nutcracker",
    "garland", "snowflake", "caroling", "cranberries", "frostbite",
    "december", "chestnuts", "winter wonderland", "north pole",
    "peppermint", "tinsel", "bethlehem", "christmastide",
    "mulled wine", "evergreen", "snowdrift", "candlelight", "sleighbells"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_letter():
    while True:
        letter = input("Guess a letter: ")
        if letter.isalpha() and len(letter) == 1:
            return letter
        print("Wrong input. Please enter only one letter and no other characters.")
        continue


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while mistakes < len(STAGES) - 1 and len(guessed_letters) != len(secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_letter()
        print("You guessed:", guess)
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

    if mistakes == len(STAGES) - 1:
        print(f"Game Over! The word was: {secret_word}")
        print(STAGES[-1])
    elif len(guessed_letters) == len(secret_word):
        print("Congratulations, you saved the snowman!")