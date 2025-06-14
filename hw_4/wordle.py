import random

def choose_random_word(words):
    try:
        return random.choice(words)
    except IndexError:
        print("Error: Word list is empty.")
        return "error"

def user_guess(word_length):
    while True:
        try:
            guess = input(f"Enter your guess ({word_length} letters): ").lower()
            if len(guess) != word_length:
                raise ValueError(f"Expected {word_length} letters.")
            if guess not in word_list:
                print("This word is not in the dictionary.")
                continue
            if not guess.isalpha():
                raise ValueError("Only alphabetic characters allowed.")
            return guess
        except ValueError as e:
            print("Input Error:", e)

def check_guess(secret_word, guess):
    result = []
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            result.append('correct')
        elif letter in secret_word:
            result.append('present')
        else:
            result.append('absent')
    return result

def format_feedback(guess, result):
    display = []
    for i in range(len(guess)):
        letter = guess[i]
        status = result[i]
        if status == 'correct':
            display.append(f"[{letter.upper()}]")
        elif status == 'present':
            display.append(f"({letter})")
        else:
            display.append(f" {letter} ")
    return ' '.join(display)

def play_game(word_list, max_tries):
    secret_word = choose_random_word(word_list)
    if secret_word == "error":
        return
    word_length = len(secret_word)
    tries_left = max_tries

    print("Welcome to Wordle!")
    print(f"Guess the {len(secret_word)}-letter word. You have {max_tries} tries.")

    while tries_left>0:
        print(f"Attempt {max_tries - tries_left + 1}/{max_tries}")
        guess = user_guess(word_length)

        if guess == secret_word:
            print("You win!!! Congratulations!")
            return
        result = check_guess(secret_word, guess)
        feedback = format_feedback(guess, result)
        print("Result:", feedback)
        tries_left -= 1
    print(f"You lose! The word was: {secret_word}")

def start_again():
    while True:
        again = input("Play again? (yes/no): ").strip().lower()
        if again == 'yes':
            return True
        elif again == 'no':
            return False
        else:
            print("Please, enter 'yes' or 'no'")


word_list = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
max_tries = 6

while True:
    play_game(word_list, max_tries)
    if not start_again():
        print("Thank you for the game! Goodbye!")
        break