import random
import csv

def check_guess(secret_word, guess):
    feedback = ''
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback += '+'
        elif guess[i] in secret_word:
            feedback += '*'
        else:
            feedback += '-'
    return feedback

def read_words_from_csv(file_path):
    words = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            words.append(row[0])
    return words

def fetch_random_word(words):
    return random.choice(words)

def show_rules():
    print("=== Wordle Rules ===")
    print("1. The secret word is a five-letter word.")
    print("2. You have 6 attempts to guess the word.")
    print("3. After each guess, the feedback will be provided.")
    print("   '+' indicates a correct letter in the correct position.")
    print("   '*' indicates a correct letter in the wrong position.")
    print("   '-' indicates an incorrect letter.")
    print("4. Your goal is to guess the word within the given attempts.")

def play_wordle():
    print("Welcome to Wordle!")
    show_rules()

    while True:
        start_game = input("Type 'start' after reading the rules to begin the game: ").lower()
        if start_game != 'start':
            print("Please type 'start' to begin the game.")
            continue
        else:
            break

    play_alone = input("Do you want to play alone? (Y/N): ").lower()
    if play_alone == 'y':
        play_alone_game()
    else:
        play_with_computer_game()

def play_alone_game():
    attempts = 6

    print("=== Play Alone ===")
    print("Guess the secret five-letter word.")

    valid_solutions = read_words_from_csv('valid_solutions.csv')  # Replace with your valid solutions CSV file path

    secret_word = fetch_random_word(valid_solutions)

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        guess = input("Enter your guess: ").lower()

        if len(guess) != 5:
            print("Please enter a five-letter word.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed the correct word.")
            break

        feedback = check_guess(secret_word, guess)
        print(f"Feedback: {feedback}")

        reveal = input("Would you like to reveal the solution? (Y/N): ").lower()
        if reveal == 'y':
            print(f"The solution is: {secret_word}")
            break

        attempts -= 1

    if attempts == 0:
        print("Game over. You ran out of attempts.")
        print(f"The secret word was: {secret_word}")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == 'y':
        play_wordle()
    else:
        print("Thank you for playing Wordle!")

def play_with_computer_game():
    attempts = 6

    print("=== Play with Computer ===")
    print("You and the computer will take turns guessing the secret word.")
    print("Guess the secret five-letter word.")

    valid_solutions = read_words_from_csv('valid_solutions.csv')  # Replace with your valid solutions CSV file path

    secret_word = fetch_random_word(valid_solutions)

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        user_guess = input("Enter your guess: ").lower()

        if len(user_guess) != 5:
            print("Please enter a five-letter word.")
            continue

        if user_guess == secret_word:
            print("Congratulations! You guessed the correct word.")
            break

        user_feedback = check_guess(secret_word, user_guess)
        print(f"Your feedback: {user_feedback}")

        reveal = input("Would you like to reveal the solution? (Y/N): ").lower()
        if reveal == 'y':
            print(f"The solution is: {secret_word}")
            break

        print("\nComputer's turn to guess...")
        computer_guess = fetch_random_word(valid_solutions)
        computer_feedback = check_guess(secret_word, computer_guess)

        print(f"Computer's guess: {computer_guess}")
        print(f"Computer's feedback: {computer_feedback}")


        attempts -= 1

    if attempts == 0:
        print("Game over. You and the computer ran out of attempts.")
        print(f"The secret word was: {secret_word}")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == 'y':
        play_wordle()
    else:
        print("Thank you for playing Wordle!")


play_wordle()
