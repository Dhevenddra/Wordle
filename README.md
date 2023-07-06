# Wordle Game
Wordle is a simple word-guessing game where players attempt to guess a five-letter word within a limited number of attempts. This program allows you to play Wordle on your computer using a command-line interface.

## New Features and Changes
* Added the option to play alone or with the computer.
* Included basic rules of the game.
* Required the user to confirm that they have read the rules before starting the game.
* Enabled the user and the computer to have 6 chances each to guess the word.
* Displayed feedback after each guess.

## Requirements
* Python 3.x
* CSV file containing valid solution words - https://www.kaggle.com/datasets/bcruise/wordle-valid-words

## Usage
1. Open a terminal or command prompt and navigate to the directory where the program is located.

2. Run the program by executing the following command:
```python wordle_game.py```

4. Read the basic rules displayed at the start of the program.

5. Type 'start' to confirm that you have read the rules and begin the game.

6. Choose to play alone or with the computer by responding to the prompts.

7. Guess the secret five-letter word within 6 attempts.

8. After each guess, feedback will be provided to help you refine your subsequent guesses.

9. If you or the computer guesses the correct word within the given attempts, you win the game. Otherwise, the game ends, and the secret word is revealed.

10. You will be prompted to play again. Enter 'Y' or 'y' to play another round with a new random word, or any other key to exit the program.

## Acknowledgments
* The Wordle game concept was adapted for this program.
* CSV reading functionality is based on the csv module in Python's standard library.

## Contact
If you have any questions or inquiries, feel free to reach out.
