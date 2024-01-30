import random
from visuals import *

class HangmanGame:
    def __init__(self):
        """
        Initializes a new Hangman game instance.

        Attributes:
        - word (str): The target word to guess.
        - blanks (list): List representing the current state of the word with blanks.
        - already_guessed (list): List of letters that have been guessed.
        - lives (int): Number of lives remaining.
        - game_over (bool): Flag indicating whether the game is over.
        """
        # Load a word for the game
        self.word = self.choose_word()
        # Initialize blanks to represent the letters of the word
        self.blanks = ['_' if letter.isalpha() else '-' for letter in self.word]
        # Initialize the list of guessed letters
        self.already_guessed = []
        # Set the initial number of lives
        self.lives = 6
        # Flag indicating whether the game is over
        self.game_over = False

    def choose_word(self) -> str:
        """
        Chooses a random word from the 'words.txt' file and ensures it has a minimum length of 4 characters.

        Returns:
        str: The chosen word in lowercase.
        """
        try:
            # Open the file and read the lines
            with open('words.txt', 'r') as file:
                lines = file.readlines()

                # Choose a random word from the lines
                chosen_word: str = random.choice(lines).strip()
                # Ensure the word has a minimum length of 4 characters
                while len(chosen_word) < 4:
                    chosen_word = random.choice(lines).strip()

                return chosen_word.lower()
        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Error: 'words.txt' file not found.")
            return ""

    def display_word(self) -> str:
        """
        Generates a string representation of the word with blanks for unrevealed letters and hyphens for non-alphabetic characters.

        Returns:
        str: The word with blanks and hyphens based on guessed letters.
        """
        # Construct the display string with blanks and hyphens
        return ' '.join(letter if letter in self.already_guessed else '_' if letter.isalpha() else '-' for letter in self.word)

    def is_valid_guess(self, guess: str) -> bool:
        """
        Checks if a guess is valid, i.e., a single alphabetical character.

        Parameters:
        guess (str): The user's guess.

        Returns:
        bool: True if the guess is valid, False otherwise.
        """
        # Check if the guess is a single alphabetical character
        return guess.isalpha() and len(guess) == 1

    def take_guess(self, guess: str) -> None:
        """
        Processes the user's guess, updating the game state.

        Parameters:
        guess (str): The user's guess.

        Raises:
        ValueError: If the guessed letter has already been guessed.
        """
        # Check if the letter has already been guessed
        if guess in self.already_guessed:
            raise ValueError("You have already guessed that letter")

        # Add the guessed letter to the list
        self.already_guessed.append(guess)

        # Update blanks based on the guessed letter
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.blanks[i] = guess
        else:
            # Reduce lives if the guess is incorrect
            print("Wrong guess")
            self.lives -= 1

    def check_game_over(self) -> None:
        """
        Checks whether the game is over, either due to a win or loss.
        If the game is over, sets the game_over flag and prints the corresponding message.
        """
        # Check if the player has won
        if "_" not in self.blanks:
            self.game_over = True
            print(f"{self.display_word()}\nYou win!\n{logo}")
        # Check if the player has lost
        elif self.lives == 0:
            self.game_over = True
            print(f"{stages[self.lives]}\nYou lose!\nThe word was {self.word}\n{logo}")

    def play(self) -> None:
        """
        Main game loop. Takes user input for guesses and updates the game state until the game is over.
        """
        while not self.game_over:
            try:
                # Get the user's guess
                guess = input("Guess a letter: ").lower()

                # Check if the guess is valid
                if not self.is_valid_guess(guess):
                    raise ValueError("Invalid guess. Please enter a single alphabetical character.")

                # Process the guess
                self.take_guess(guess)
                # Display the current state of the game
                print(f"{stages[self.lives]}\n{self.display_word()}")
                # Check if the game is over
                self.check_game_over()

            except ValueError as ve:
                # Handle errors during the game
                print(f"Error: {ve}")

def main():
    """
    The main entry point for the Hangman game.
    Initializes a HangmanGame instance and starts the game.
    """
    # Create a HangmanGame instance
    hangman_game = HangmanGame()
    # Start the game
    hangman_game.play()

if __name__ == "__main__":
    # Run the game if the script is executed directly
    main()
