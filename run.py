import random
import string
from colorama import Fore
from words import words_list
from stage import STAGES
import pyfiglet


def start_game():
    """
    The variable result will display the title of the "Hangman Game"
    Creating an input if the user wants to play hangman game
    """
    result = pyfiglet.figlet_format("Hagman", font="banner3-D")
    print(result)

    if input(Fore.GREEN + 'Would you like to play Hangman? (Y)').upper() == "Y": # noqa
        username()

    else:
        print('Please try again.')
        start_game()


def username():
    """
    Creating an input for the user to write his name 
    Printing a greeting on the screen
    """
    name = input(Fore.LIGHTWHITE_EX + 'Enter your name: \n')
    print(Fore.GREEN + f"Hey, {name}! Let's Play.")


class HangmanGame:
    """
    Data Model

    ***

    Atributtes:

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

    """

    def __init__(self):
        """
        This Initialize method will start the class off 
        as the user just start to play
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
        self.word = random.choice(words_list).upper()
        self.display_word = "_ " * len(self.word)

    def game_play(self):
        """
        The loop will run until the user guesses the right word or runs out of lives # noqa
        """ 
        # Getting the user input
        while not self.user_guessed and self.lives > 0:
            self.display_hangman()
            guess = input('Please guess a letter or word: ').upper()

            if len(guess) == 1 and guess.isalpha():
                self.available_letters -= {guess}
                if guess in self.letter_guessed:
                    print(f'You already guessed the letter, {guess}')

                elif guess not in self.word:
                    print(f'{guess}, is not in the word.')
                    self.lives -= 1
                    self.letter_guessed.append(guess)
                else:
                    print(f'Congrats! {guess} is in the word.')
                    self.letter_guessed.append(guess)
                    word_as_list = [x for x in self.display_word if x != ' ']
                    indices = [
                        i for i, letter in enumerate(self.word)
                        if letter == guess
                        ]
                    for index in indices:
                        word_as_list[index] = guess
                    self.display_word = " ".join(word_as_list)
                    if "_" not in self.display_word:
                        self.user_guessed = True

            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in self.words_guessed:
                    print(f'You already guessed the word, {guess}')
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
            print(Fore.GREEN + f'Congrats, you guessed the exactly word "{self.word}", YOU ROCK!') # noqa
        else:
            print(Fore.LIGHTRED_EX + f'Sorry, you have no more lives! the word was {self.word} you can try again :)') # noqa
                    
    def display_hangman(self):
        """
        Creating a function that will display:
        Available letters for the user
        The Hangman Stages/ lives
        The display of word for user's guesses
        How many lives are left for the user
        Letters that the user already guessed
        Words that the user already guessed
        """
        print(Fore.LIGHTWHITE_EX + f"Available Letters: {' '.join(sorted(self.available_letters))}") # noqa
        print(Fore.LIGHTWHITE_EX + STAGES[self.lives])
        print(Fore.LIGHTWHITE_EX + self.display_word)
        print(Fore.LIGHTRED_EX + f"Lives left: {self.lives}")
        print(Fore.LIGHTWHITE_EX + f'Letters guessed: {" ".join(self.letter_guessed)}') # noqa
        print(Fore.LIGHTWHITE_EX + f'Words guessed: {" ".join(self.words_guessed)}') # noqa
        print("\n")


def main():
    """
    Main function, will run the whole game and ask the user if he/she wants to try again # noqa
    """
    start_game()
    game = HangmanGame()
    game.get_words_list()
    game.game_play()

    while input(Fore.LIGHTWHITE_EX + 'Do you want try again? (Y/N ').upper() == "Y": # noqa
        game = HangmanGame()
        game.get_words_list()
        game.game_play()
    good_bye = pyfiglet.figlet_format("Good Bye!", font="banner3-D")
    print(good_bye)


if __name__ == "__main__":
    main()
