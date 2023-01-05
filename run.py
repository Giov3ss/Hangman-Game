import random
from words import words 

def start_game():
    print("""
             _  _  __  __  _  __ __ __  __  __  _  
            | || |/  \|  \| |/ _]  V  |/  \|  \| | 
            | >< | /\ | | ' | [/\ \_/ | /\ | | ' | 
            |_||_|_||_|_|\__|\__/_| |_|_||_|_|\__|       
    """)

    if input('Would you like to play Hangman? (Y)').upper() == "Y":
        username()

    else:
        print('Please try again.')
        start_game()



        




# function to get random words from the list 
def get_words_list():
    """
    Get random words from words.py
    """
    word = random.choice(words)
    return word.upper()

# Creating a function for the game play 
def game_play(word):
    """
    Track the correctly word the user input
    """
    completion_words = "_" * len(word)
    user_guessed = False 
    letter_guessed = []
    words_guessed = []
    lives = 6

    print(display_hangman(lives))
    print(completion_words)
    print('\n')

    # Getting the user input 
    while not user_guessed and lives > 0:
        guess = input('Please guess a letter or word: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in letter_guessed:
                print(f'You already guessed the letter, {guess}')
            elif guess not in word:
                print(f'{guess}, is not in the word.')
                lives -= 1
                letter_guessed.append(guess)
            else:
                print(f'Congrats! {guess} is in the word.')
                letter_guessed.append(guess)
                word_as_list = list(completion_words)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                completion_words = "".join(word_as_list)
                if "_" not in completion_words:
                    user_guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print(f'You already guessed the word, {guess}')
            elif guess != word:
                print(f'{guess}, is not the word.')
                lives -= 1
                letter_guessed.append(guess)
            else:
                user_guessed = True
                completion_words = word
        else:
            print("Is not a valid guess.")

        print(display_hangman(lives))
        print(completion_words)
        print("\n")
    if user_guessed:
        print('Congrats, you guessed the exactly word, YOU ROCK!')
    else:
        print(f'Sorry, you have no live! the word was {word}, try again!')

def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]


def main():
    word = get_words_list()
    game_play(word)
    while input('Do you want try again? (Y/N ').upper() == "Y":
        word = get_words_list()
        game_play(word)
    
if __name__ == "__main__":
    main()