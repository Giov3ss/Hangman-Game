# **Hangman-Game**

<img width="1308" alt="image" src="https://user-images.githubusercontent.com/112728772/212570491-f28b6c86-58c8-436b-8591-28cd1c616d88.png">

- Hangman is a classic word guessing game in which players must correctly guess a word (that will be pick randomly in the list of words by the computer) before a certain number of incorrect guesses are made. Players can make guesses by suggesting letters that they think are in the word, and if the suggested letter is in the word, it is revealed in its correct position(s). If the suggested letter is not in the word, a part of the hangman drawing is added, and the player loses a "lives". The game is typically won by the player who correctly guesses the word before the hangman is fully drawn in the screen.

## Live Site 
[https://hangman-gameplay.herokuapp.com/](https://hangman-gameplay.herokuapp.com/)

## Repository
[https://github.com/Giov3ss/Hangman-Game/blob/main/README.md](https://github.com/Giov3ss/Hangman-Game/blob/main/README.md)

## Author

Giovani Fonseca

## **Table of Contents**

1. [UX Development](#ux-development)
    * [Project Goal](#project-goal)
    * [User Goals](#user-goal)
    * [User Stories](#user-stories)
    * [How to Play](#how-to-play)  
    * [Desing](#desing)
        * [Flowchart](#flowchart)

2. [Features](#features)

3. [Future Features](#future-features) 

4. [Data Model/ Classes](#data-model-classes)

5. [Testing](#testing)
    * [Validation Testing](#validation-testing)
    * [Manual Testing](#manual-testing)
    * [Defect Tracking](#defect-tracking)
    * [Commenting Code](#commenting-code)

6. [Technology Used](#technology-used)  
    * [Language Used](#languages-used)
    * [Tools and Libraries](#tools-and-libraries)

7. [Deployment](#deployment)
    * [Fork the repository](fork-the-repository)
    * [Heroku](#heroku)
  
8. [Credits](#credits)
    * [Media](#media)  

9. [Acknowledgements](#acknowledgements)

- - -

# **Table of Contents**
## UX Development

### Project Goal 
- Ensuring that the game are working with no errors and perfectly.

## User Goal
- Want to easily navigate through the game with simple inputs.

## User Stories
- Be able to type my name.
- Show me the letter availables.
- Show me the wrong words.
- Show me the wrong letters.
- Show me the correct word at the end.
- Show me an optional message if I want to try again the game.

## Flowchart
<img width="723" alt="image" src="https://user-images.githubusercontent.com/112728772/212423963-3c23c17a-1325-49ec-817a-8fe0d080bdd7.png">


## How to Play
- The user needs to type "1" to start the game or "2" to quit.
- The user enter his/her name.
- A random word is choose e the user can type a letter.
- After the user types a letter, the program will run and see if the letter is in the word, if so, it will appear in the console below, if not, a life and a frame will be taken from the Hangman.
- All typed letter will appear on the top of the Hangman frame with a message that the letter is not in the word.
- The user has 6 lives to find the correct word, if so, he will receive a congratulations message, and the correct word. If the user does not find the right word, a message will appear saying that the lives are over and the correct word will appear.
- The user has the option to play again and if yes, a new word is generated and he/she can start guessing the word.
  
How to play video:

https://user-images.githubusercontent.com/112728772/212769897-fb339cc9-cf31-4209-b606-22c7e9222c0f.mp4


## Features 

A input where the user can write his name, and a message with the user's name will appear on the screen:

 <img width="731" alt="image" src="https://user-images.githubusercontent.com/112728772/212767436-713c4fc1-fec0-429b-b789-589083d4522e.png">


A user input that the user chooses whether to Start the Game, View the rules, or Quit:

 <img width="733" alt="image" src="https://user-images.githubusercontent.com/112728772/212765718-a1304f57-de48-4622-8501-fe2090433602.png">


If user chooses 1, Game Start:

 <img width="740" alt="image" src="https://user-images.githubusercontent.com/112728772/212763046-715ef651-2ef7-4654-b17e-603c41000469.png">

If the user chooses 2, the Rules will appear on the screen (the user can press any key to return to the menu options):

 <img width="735" alt="image" src="https://user-images.githubusercontent.com/112728772/212763194-ff81ab41-ebf4-4025-9fc7-6e41bd57f778.png">

If the user chooses 3, the Game is over and a fancy "Goodbye" is displayed on the screen:

  <img width="735" alt="image" src="https://user-images.githubusercontent.com/112728772/212763461-a56ab092-540e-4d32-bb4c-5c91af369f78.png">

Win by Letter:

 <img width="737" alt="image" src="https://user-images.githubusercontent.com/112728772/212762527-a09b165b-a695-4826-bf8d-59d2b8f2e0ab.png">

Win by Word:

 <img width="729" alt="image" src="https://user-images.githubusercontent.com/112728772/212764290-c9bc9737-bbd0-4f4b-993f-0d383c9016a2.png">

If the user runs out of lives, a message appears with the correct word, and the user can choose, Play Game, see the Rules or Quit:

 <img width="728" alt="image" src="https://user-images.githubusercontent.com/112728772/212763920-dbeab556-e960-4513-a731-879c37f5e1d0.png">

## Future Features

- User login.
- A dashboard where the user can see how many wins and losses he/she has.


## Data Model/ Classes

| Class: Hangman       |                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Methods:             |                                                                                                                                                                                                                                                                                                                                                                                        |
| Start Game()         | This function starts a new game of Hangman, it welcomes the player and prompts them to start the game or quit.  If the player chooses to start the game, it calls the username() function and creates a new instance of the  HangmanGame class, which starts the game.                                                                                                                 |
| Username()           | This function prompts the player to enter their name and greets them by printing a message including their name.                                                                                                                                                                                                                                                                       |
| HangmanGame()        | This is a class that represents the data model for a game of Hangman. It has several attributes such as the word to be guessed, the display of the word, whether the user has guessed the word,  the letters and words guessed, the available letters, and the number of lives remaining.  It also has several methods such as __init__, get_words_list, game_play and display_hangman |
| init (self)          | This is the constructor method for the HangmanGame class.  It initializes the properties of a new game such as the word to be guessed, the display of the word, whether the user has guessed the word,  the letters and words guessed, the available letters, and the number of lives remaining.                                                                                       |
| get_words_list(self) | This method gets a random word from a list of words and converts it to uppercase.  It also creates an underline-based display of the word based on its length.                                                                                                                                                                                                                         |
| game_play(self)      | This method displays the available letters for the user, the current stage of the hangman game, the current display of the word for the user's guesses, the number of lives remaining for the user, the letters that the user has already guessed, and the words that the user has already guessed.                                                                                    |
| main()               | This function is the main entry point of the game. It starts by greeting the user and prompts them to start the game.  Then it calls the username() function to get the user's name and the start_game() function to start the game. Once the game is completed, the function will say a fancy good bye to the user.                                                                   |

## Testing

### Validation Testing

- run.py
<img width="1163" alt="image" src="https://user-images.githubusercontent.com/112728772/212565966-a76c2e91-6eda-475a-a684-9b5d54ac415f.png">

- words.py
<img width="1117" alt="image" src="https://user-images.githubusercontent.com/112728772/212566110-e16f32f7-0232-4ca2-9c0e-49767c5037f2.png">

- stage.py
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/112728772/212566005-590d2ec4-68cb-45f6-8c10-86ca0851d04b.png">

### Manual Testing
- [x] Input asking if the user wants to play is working.
- [x] Input asking the user name is working.
- [x] Input where the user can type a letter or guess a word is working.
- [x] Number of lives decreases every time the user tries to guess and it's a wrong letter/word.
- [x] Hangman stage loses a frame every time the user tries to guess and it's a wrong letter/word.
- [x] Available letters appearing correctly.
- [x] Word/Letter guesses working corretly.
- [x] A message display when the user ran out lives.
- [x] An alert message appear when the user type an invalid input if is not a letter/word.
- [x] Input asking if the user wants to try again working corretly.
- [x] Good bye message at the end working. 

### Defect Tracking

- Do you want to play input, there should be an if statement, so if the user doesn't want to play, the game just ends.


### Commenting Code
<img width="806" alt="image" src="https://user-images.githubusercontent.com/112728772/212427820-67399cad-a915-4412-bd0d-a619b6d04536.png">

## Technology Used
### Languages Used 

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python") for the game code
- [Markdown](https://en.wikipedia.org/wiki/Markdown) for the content in my README file

### Tools and libraries
- [python random library](https://docs.python.org/3/library/random.html?#module-random ".py random") For selection a random word from the deck
- [Gitpod](https://www.gitpod.io/) - Used to build the gme.
- [Colorama](https://pypi.org/project/colorama/) - Used to put some color in the text.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used to creat an image displaying the homepage on multiple devices.
- [Table Generator](https://www.tablesgenerator.com/) Used to make a table explaining the model/methods of the class.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) For Python validation.


### Deployment 

#### link of the site here 

 The site was deployed by Heroku pages. The steps are:
 - Log in Heroku website;
 - Click "New" and select > "Create new app";
 - Choose the name of the app, region and click on > "Create App";
 - In the menu section only the "Deploy" and "Settings" are relevant.
 Settings firts:
 - Buildpacks need to be added. First Python and second is node.js in this follow sequence. Save this section.
 Deploy:
 - The "Deploy" section needs to be selected from the menu and connect it to Github;
 - Firts enter the name of your repository that you want to connect, the click > "connect";
 - A choice will appear, you can Deploy either automatic or manual deployment, which deploys the current state of the branch;
 - Then you can click on Heroku app > "Deploy Branch".

 ### Fork the repository

[https://github.com/Giov3ss/Hangman-Game/blob/main/README.md](https://github.com/Giov3ss/Hangman-Game/blob/main/README.md)
 
 <img width="1420" alt="image" src="https://user-images.githubusercontent.com/112728772/212497044-81beae62-bd04-4a8e-ae07-29a037f86fbc.png">

 ### Heroku
 - Log in Heroku website;
 - Click "New" and select > "Create new app";

  <img width="1431" alt="image" src="https://user-images.githubusercontent.com/112728772/212567101-57efd8fe-86c0-4cc8-b721-7f87641f213f.png">
 
- Choose the name of the app, region and click on > "Create App";

 <img width="1434" alt="image" src="https://user-images.githubusercontent.com/112728772/212567121-0e842119-f6e0-47e8-b358-dc26e5f308d2.png">

- Buildpacks need to be added. First Python and second is node.js in this follow sequence. Save this section.
 Deploy:

 <img width="1253" alt="image" src="https://user-images.githubusercontent.com/112728772/212567270-255618bf-c64b-441b-a075-48a33409cfa7.png">

- The "Deploy" section needs to be selected from the menu and connect it to Github;
- Firts enter the name of your repository that you want to connect, the click > "connect";

 <img width="1432" alt="image" src="https://user-images.githubusercontent.com/112728772/212567657-344b7937-332c-4f0c-9d5b-1f67c8f620c7.png">

- A choice will appear, you can Deploy either automatic or manual deployment, which deploys the current state of the branch;
- Then you can click on Heroku app > "Deploy Branch".

 <img width="1288" alt="image" src="https://user-images.githubusercontent.com/112728772/212567722-37180822-1fd8-409c-9626-e90fe91e1c5d.png">


### Credits
 - I would like to thank my mentor Malia for her help, tips and advise all the time.
 - [Code Institute](https://codeinstitute.net/nl/) With the Python Essentials and template.
 - [Stackoverflow](https://stackoverflow.com) When I was in doubt about something.
 - [Invent with Python](https://inventwithpython.com/invent4thed/chapter8.html) Explained the whole game.
 - [Youtube](https://youtu.be/m4nEnsavl6w) This video helped me understand the logic of the game.
 - [Geeks for Geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) Provided explanation on how to import the colors in python text, also the custom fonts.
 

### Media 
 - [Fonts](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) Used to get custom fonts.

 ### Acknowledgements
 - This is a game for Project 3 for Full Stack Software Developer program with code Institute
