import random
import string
from time import sleep
import os
from colorama import Fore
from words import WORDS_LIST
from stage import STAGES
import pyfiglet


def start_game():
    """
    Starts a new Hangman game.

    Will prompt the user with options to start the game, view the rules or
    quit the game.
    Based on the user's answer, the game will start, display the rules or
    exit the program.
    """

    print(Fore.LIGHTWHITE_EX + "What do you want to do?")
    print("1 = Play Game")
    print("2 = View rules")
    print("3 = Quit")
    answer = input("Enter your answer here \n").strip()
    while answer not in ["1", "2", "3", 1, 2, 3]:
        print("Invalid answer, try again!")
        sleep(2)
        start_game()

    if answer == "1":
        game = HangmanGame()
        game.get_words_list()
        game.game_play()
        start_game()
    elif answer == "2":
        display_rules()
        input(Fore.YELLOW + "Press any key to go back to the main menu.\n")
        start_game()


def display_rules():
    """
    Display the rules of the Hangman game.
    The function will print the main objective, gameplay and the number of tries the user has to correctly guess the word.  # noqa
    """
    print("""The main objective of Hangman is to guess a word within 6 tries 
    by entering letters or a word of the same length as the one you are trying to solve.  # noqa

    When you play Hangman, you are presented a screen with available letters.
    A pixelated hanman gallows that is empty to start with.

    A series of + symbols indicated the length of the word, the number of lives left,  # noqa
    a recap of the letters you have guessed, and a recap of words guessed.

    As you make guesses that are correct the proper placement of letters are filled in.  # noqa
    If you make an incorrect guess a body part is added to the hangman graphic 
    and your number of tries left goes down.

    You have 6 guesses to start with.

    Good Luck and May The Odds Always Be in Your Favor.""")


def username():
    """
    Prompts the player to enter their name and greets them.

    Asks the player to enter their name and stores it in the variable 'name'.
    Prints a greeting message including the player's name.
    """

    name = input(Fore.LIGHTWHITE_EX + 'Enter your name: \n')
    print(Fore.YELLOW + f"Hey, {name}! Let's see how good you are.")
    sleep(1)


class HangmanGame:
    """
    Data Model

    ***

    ATRIBUTTES:

    word: str
        A random word that the user will try to guess with 6 attempts

    display_word: str
        display of word for user's guesses

    user_guessed: Boolean
        Will track if the user has guessed current word or not

    letter_guessed: Array of str
        will track the letters that the user has guessed

    words_guessed: Array of str
        will track the words that the user has guessed

    lives: int number
        will count the lives or chances until user looses game

    METHODS:

    __init__: Initialize the properties of a Hangman game

    get_words_list:
        Getting a random words from words.py
        Coverts the user input to uppercase
        Will also go display an underline *_* based on
        the length of the words_list

    game_play(self): Handles the gameplay of a Hangman game

    display_hangman(self):
        This function will display the available letters for the user,
     the current stage of the hangman game, the current display of the word for the user's guesses,
        the number of lives remaining for the user, the letters that the user has already guessed,
        and the words that the user has already guessed.

    main():
    This function is the main entry point of the game, it will run the whole hangman game. # noqa
    The function starts by greeting the user, with a fancy text,
     then it will call the username() function to get the user's name and the start_game() function to start the game.  # noqa
    Once the game is completed, the function will say a fancy good bye to the user.  # noqa

    """

    def __init__(self):
        """
        Initialize the properties of a Hangman game.

        Attributes:
        word (str): The word to be guessed.
        display_word (str): The word to be displayed, with unguessed letters replaced by underscores.
        user_guessed (bool): Whether the user has correctly guessed the word.
        letter_guessed (list): A list of letters that have been guessed.
        words_guessed (list): A list of words that have been guessed.
        available_letters (set): A set of uppercase letters that can be guessed. # noqa
        lives (int): The number of lives remaining in the game.
        """
        self.word = ""
        self.display_word = ""
        self.user_guessed = False
        self.letter_guessed = []
        self.words_guessed = []
        self.available_letters = set(string.ascii_uppercase)
        self.lives = 6

    def get_words_list(self):
        """
        Getting a random words from words.py
        Coverts the user input to uppercase
        Will also go display an underline *_* based on
        the length of the words_list
        """
        self.word = random.choice(WORDS_LIST).upper()
        self.display_word = "+ " * len(self.word)

    def game_play(self):
        """
        Handles the gameplay of a Hangman game.
        This function repeatedly prompts the player to guess a letter or word, and checks if the guess is valid.  # noqa
        If the guess is a single letter and has not been guessed before, it checks if the letter is in the word.  # noqa
        If it is, it updates the display_word to show the correctly guessed letter, otherwise it reduces the number of lives by 1.  # noqa
        If the guess is the word and has not been guessed before, it checks if the word is the correct word.  #noqa
        If it is, the user_guessed is set to True, otherwise the number of lives is reduced by 1.  # noqa
        Attributes:
        self.user_guessed(bool): Whether the user has correctly guessed the word.  # noqa
        self.lives (int): The number of lives remaining in the game.
        self.display_word (str): The word to be displayed, with unguessed letters replaced by underscores.  # noqa
        self.letter_guessed (list): A list of letters that have been guessed.
        self.words_guessed (list): A list of words that have been guessed.
        self.available_letters (set): A set of uppercase letters that can be guessed.  # noqa
        self.word (str): The word to be guessed.

        """

        # THE BEGIN OF THE LOGIC WAS TAKEN FROM https://youtu.be/m4nEnsavl6w
        while not self.user_guessed and self.lives > 0:
            self.display_hangman()
            guess = input('Please guess a letter or word: \n').upper().strip()

            if len(guess) == 1 and guess.isalpha():
                self.available_letters -= {guess}
                if guess in self.letter_guessed:
                    print(f'You already guessed the letter, {guess}')  # noqa

                elif guess not in self.word:
                    print(f'{guess}, is not in the word.')
                    self.lives -= 1
                    self.letter_guessed.append(guess)
                else:
                    print(f'Congrats! {guess} is in the word.')  # noqa
                    self.letter_guessed.append(guess)
                    word_as_list = [x for x in self.display_word if x != ' ']
                    indices = [
                        i for i, letter in enumerate(self.word)
                        if letter == guess
                    ]
                    for index in indices:
                        word_as_list[index] = guess
                    self.display_word = " ".join(word_as_list)
                    if "+" not in self.display_word:
                        self.user_guessed = True

            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in self.words_guessed:
                    print(f'You already guessed the word, {guess}')  # noqa
                elif guess != self.word:
                    print(f'{guess}, is not the word.')
                    self.lives -= 1
                    self.words_guessed.append(guess)
                else:
                    self.user_guessed = True
                    self.display_word = self.word
            else:
                print("Is not a valid guess.")

        if self.user_guessed:
            sleep(1)
            print(Fore.GREEN + f'Congrats, you guessed the exactly word "{self.word}", YOU ROCK!')  # noqa
        else:
            sleep(1)
            print(
                Fore.LIGHTRED_EX + f'Sorry, you have no more lives! the word was {self.word} you can try again :)')  # noqa
        # END HERE

    def display_hangman(self):
        """
        This function will display the available letters for the user, 
        the current stage of the hangman game, the current display of the word for the user's guesses,  # noqa
        the number of lives remaining for the user, the letters that the user has already guessed,  # noqa
        and the words that the user has already guessed.
        """
        sleep(1)
        os.system('clear')
        print(Fore.LIGHTWHITE_EX + f"Available Letters: {' '.join(sorted(self.available_letters))}")  # noqa
        print(Fore.LIGHTWHITE_EX + STAGES[self.lives])
        print(Fore.LIGHTWHITE_EX + self.display_word)
        print(Fore.LIGHTRED_EX + f"Lives left: {self.lives}")
        print(Fore.LIGHTWHITE_EX + f'Letters guessed: {" ".join(self.letter_guessed)}')  # noqa
        print(Fore.LIGHTWHITE_EX + f'Words guessed: {" ".join(self.words_guessed)}')  # noqa
        print("\n")


def main():
    """
    This function is the main entry point of the game, it will run the whole hangman game. # noqa
    The function starts by greeting the user, with a fancy text, 
    then it will call the username() function to get the user's name and the start_game() function to start the game.  # noqa
    Once the game is completed, the function will say a fancy good bye to the user.  # noqa
    """
    # Greeting the user
    result = pyfiglet.figlet_format("Hangman", font="banner3-D")
    print(result)
    print(Fore.YELLOW + "Welcome player! It's time to see if you can save the Hangman or not! \n")  # noqa
    sleep(2)
    # welcome user
    username()
    start_game()
    # fancy good bye
    good_bye = pyfiglet.figlet_format("Good Bye!", font="banner3-D")
    print(good_bye)


if __name__ == "__main__":
    main()
