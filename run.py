import random
from words import words 

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
    print("Let's play: ")

    print("""
             _  _  __  __  _  __ __ __  __  __  _  
            | || |/  \|  \| |/ _]  V  |/  \|  \| | 
            | >< | /\ | | ' | [/\ \_/ | /\ | | ' | 
            |_||_|_||_|_|\__|\__/_| |_|_||_|_|\__|       
    """)


def display_hangman(tries):
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
    return stages[tries]