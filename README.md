# **Hangman-Game**



## IMAGE GOES HERE 

## Live Site 

## link of Site after deployed 

## Repository

## repo 

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
- The user needs to type "Y" to start the game.
- The user enter his/her name.
- A random word is choose e the user can type a letter.
- After the user types a letter, the program will run and see if the letter is in the word, if so, it will appear in the console below, if not, a life and a frame will be taken from the Hangman.
- All typed letter will appear on the top of the Hangman frame with a message that the letter is not in the word.
- The user has 6 lives to find the correct word, if so, he will receive a congratulations message, and the correct word. If the user does not find the right word, a message will appear saying that the lives are over and the correct word will appear.
- The user has the option to play again and if yes, a new word is generated and he/she can start guessing the word.

## Features 
- A user input that he/she choose if want to start the game.
- A input where the user can write his name, and a "let's play" with the name of the user.
- Letter guessed will receive all the guessed letter that user guesses.
- Guess words will get all the words the user will try to guess.
- Available Letters are updated every time the user guesses the letter.
- The lives and Hangman stage will be updated every time the user makes an incorrect guess.
- An input at the end if the user wants to try again.

## Future Features

- User login.
- A dashboard where the user can see how many wins and losses he/she has.


## Data Model/ Classes

| Class: Hangman        |                                                                                                                                                                                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Methods:              |                                                                                                                                                                                                                                                                                    |
| Start Game()          | Creating an input if the user wants to play  and converting the answer to uppercase.                                                                                                                                                                                               |
| Username()            | Getting the username and print out into  the screen game.                                                                                                                                                                                                                          |
| __init__(self)        | This Initialize method will start the class off  as the user just start to play.                                                                                                                                                                                                   |
| get_words_list(self)  | Get a random word from the document "words.py" and converts the user input to uppercase, will also go display an underline *_* based on  the length of the words_list.                                                                                                             |
| game_play(self)       | Run the game till the user guesses the right word  or runs out of lives (6).                                                                                                                                                                                                       |
| display_hangman(self) | Display all the visual cues for the user to play the game,  so the user can see all the Available letters, Hangman Stage, display of word for user's guesses, how many lives are left for the user, Letters that the user already guessed and Words that the user already guessed. |
| main()                | Run the whole game and ask the user if he/she wants to try again                                                                                                                                                                                                                   |

## Testing

### Validation Testing

- run.py
<img width="1142" alt="image" src="https://user-images.githubusercontent.com/112728772/212495516-d172262b-7d1f-439c-a4e7-12c228f95f70.png">

- words.py
<img width="1102" alt="image" src="https://user-images.githubusercontent.com/112728772/212193643-66a6edd4-bc30-4c36-91c3-4ac16bda8804.png">

- stage.py
<img width="1144" alt="image" src="https://user-images.githubusercontent.com/112728772/212193823-f97440e1-ad57-4758-bf57-6c25e0d9593d.png">

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


### Defect of Note

### Outstanding Defects

### Commenting Code
<img width="806" alt="image" src="https://user-images.githubusercontent.com/112728772/212427820-67399cad-a915-4412-bd0d-a619b6d04536.png">

## Technology Used
### Languages Used 

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python") for the game code
- [Markdown](https://en.wikipedia.org/wiki/Markdown) for the content in my README file

### Tools and libraries
- [python random library](https://docs.python.org/3/library/random.html?#module-random ".py random") For selection a random word from the deck
- [Gitpod](https://www.gitpod.io/) - Used to build the gme.
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

 ### Gitpode

 ### Heroku


### Credits
 - I would like to thank my mentor Malia for her help, tips and advise all the time.
 - [Code Institute](https://codeinstitute.net/nl/) With the Python Essentials and template.
 - [Stackoverflow](https://stackoverflow.com) When I was in doubt about something.
 - [Invent with Python](https://inventwithpython.com/invent4thed/chapter8.html) Explained the whole game.
 - [Geeks for Geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) Provided explanation on how to import the colors in python text, also the custom fonts.
 

### Media 
 - [Fonts](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) Used to get custom fonts.

 ### Acknowledgements
 - This is a game for Project 3 for Full Stack Software Developer program with code Institute
