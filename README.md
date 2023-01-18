# **Hangman-Game**

<img width="1308" alt="image" src="https://user-images.githubusercontent.com/112728772/212570491-f28b6c86-58c8-436b-8591-28cd1c616d88.png">

Hangman is a classic word guessing game in which players must correctly guess a word (that will be pick randomly in the list of words by the computer) before a certain number of incorrect guesses are made. Players can make guesses by suggesting letters that they think are in the word, and if the suggested letter is in the word, it is revealed in its correct position(s). If the suggested letter is not in the word, a part of the hangman drawing is added, and the player loses a "lives". The game is typically won by the player who correctly guesses the word before the hangman is fully drawn in the screen.

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
    * [Design](#design)
        * [Flowchart](#flowchart)

2. [Features](#features)

3. [Future Features](#future-features) 

4. [Data Model/ Classes](#data-model-classes)

5. [Testing](#testing)
    * [Validation Testing](#validation-testing)
    * [Manual Testing](#manual-testing)
    * [Defect Tracking](#defect-tracking)
    * [Outstanding Defects](#outstanding-defects)
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
- Have a easy and intuitive Hangman game for users to play.
- Ensuring that the game are working with no errors.
- Produce 100% valid python code.

## User Goal
- Want to easily navigate through the game with simple inputs.

## User Stories
- Be able to type my name.
- Show me the letter availables.
- Show me the wrong words.
- Show me the wrong letters.
- Show me the correct word at the end.
- Show me an optional message if I want to try again the game.

## Design

### Flowchart

<img width="911" alt="image" src="https://user-images.githubusercontent.com/112728772/212774770-06682e03-ea47-4c77-811b-b011ebb9676d.png">



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
### Welcome Screen

<img width="728" alt="image" src="https://user-images.githubusercontent.com/112728772/213234042-33111661-61cc-47a7-a01d-339d4a4304ca.png">

### Collect User Name

- Strips leading/trailing spaces so when name is outputted, it looks nicely spaced.
- Allows alpha-numeric and special characters so user has freedom to enter whatever they want.
- Recaps user name with color change.

<img width="731" alt="image" src="https://user-images.githubusercontent.com/112728772/212767436-713c4fc1-fec0-429b-b789-589083d4522e.png">

### Main Menu

- A main place so user can play many times, see rules or exit program.
- Input is stipped of leading/trailing spaces so user has high chances of successful input.
- Loops for input until valid option is collected with a nice error message and restatement of valid options.

 <img width="733" alt="image" src="https://user-images.githubusercontent.com/112728772/212765718-a1304f57-de48-4622-8501-fe2090433602.png">

### Playing Game
- If user chooses 1, Game Start.

 <img width="740" alt="image" src="https://user-images.githubusercontent.com/112728772/212763046-715ef651-2ef7-4654-b17e-603c41000469.png">

### Rules
- Only takes up 1 screen.
- Easy to read rules of the game.
- User can sit in rules as long as they want.
- Any key entry puts user back to main menu.

 <img width="730" alt="image" src="https://user-images.githubusercontent.com/112728772/213239347-832ed39f-19db-493f-9388-e658f46db500.png">


### GoodBye Message
- Provides user a good sense of game is over with matching font as welcome screen.

 <img width="735" alt="image" src="https://user-images.githubusercontent.com/112728772/212763461-a56ab092-540e-4d32-bb4c-5c91af369f78.png">

### Available Letters
- Recaps what letters the  user can guess.
- Gets updated as user makes guesses that just one letter.

 <img width="732" alt="image" src="https://user-images.githubusercontent.com/112728772/213234502-e03b84b4-704a-42be-8bf4-ac04e38459e9.png">


### Death Graphic
- Update as user makes invalid guess with water lever rising up.
- Starts with stick man in a box.
- Ends with just a box of water.

 <img width="726" alt="image" src="https://user-images.githubusercontent.com/112728772/213234777-9f0f4030-dbd9-467c-ac46-4a09d3c1e058.png">


### Collect Guess
- Strips leading and trailing spacings and compares without case sensitivity so user has better chance providing valid entries.
- If user enters non letters, user will be told invalid guess, and board will redraw after 2 seconds without losing a life.
- If user enters a word that is not the right length, user will be told invalid guess, and board will redraw after 2 seconds without losing a life.
- If user guesses a single letter that is in the word, user gets a positive message, and board will redraw after 2 seconds.
- If user guesses a single letter that is not in the word, user gets negative message, and the board will redraw after 2 seconds.
- If user guesses a word that is the right length, but not the correct word, user gets a negative message, and the board will redraw after 2 seconds.
- If user guesses the correct word, they get a positive message and win message that is in green. Then is taken to the main menu after 2 seconds.

### Word Display
- The word is displayed initially as plus signs with a space between so the user knows how long the word they are guessing is.
- correctly guessed letters fill in the plus signs as user makes guesses.

 <img width="730" alt="image" src="https://user-images.githubusercontent.com/112728772/213235921-5670298f-d0d5-412a-a4a2-eefb052abce5.png">

### Lives Left
- is red so it stands out to the user.
- reduces everytime a new invalid guess is made.

 <img width="730" alt="image" src="https://user-images.githubusercontent.com/112728772/213236149-bf23a53c-7efe-44c2-af1f-eb47680234be.png">

### Letters Guessed
- Is updated every time the user guesses a letter.

 <img width="726" alt="image" src="https://user-images.githubusercontent.com/112728772/213236885-4b3843d5-71d5-4875-9b2e-bea3c2b4a8db.png">

### Words Guessed
- gets updated each time the user makes an invalid word guess (spelling does not matter).

 <img width="730" alt="image" src="https://user-images.githubusercontent.com/112728772/213237281-4ed156bf-6cc2-4d1d-bfa7-691a6f459fb6.png">

### Guess Prompt
- If the user has lives left, the user is prompted for a new guess.
 <img width="731" alt="image" src="https://user-images.githubusercontent.com/112728772/213237469-7e120bbb-e399-4491-b10a-a0f2146d7510.png">

### Win Message 
- If user guesses by letters, or by word, the user sees a winning message.
 <img width="732" alt="image" src="https://user-images.githubusercontent.com/112728772/213240107-5eeb5e68-ed2e-4612-b200-e0dae97e375f.png">

### Loss message
- If the user makes 6 invalid guesses, they see a looser message
 <img width="731" alt="image" src="https://user-images.githubusercontent.com/112728772/213240708-a495626d-2af3-4df3-a914-d85ba81a8b01.png">

## Future Features

- User login.
- Use google sheets and recap of number of all games played and wins vs losses from main menu

## Data Model/ Classes

| Class: Hangman        |                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Methods:**          |                                                                                                                                                                                                                                                                                                                                                                                        |
| HangmanGame           | This is a class that represents the data model for a game of Hangman. It has several attributes such as the word to be guessed, the display of the word, whether the user has guessed the word,  the letters and words guessed, the available letters, and the number of lives remaining.  It also has several methods such as __init__, get_words_list, game_play and display_hangman |
| init (self)           | This is the constructor method for the HangmanGame class.  It initializes the properties of a new game such as the word to be guessed, the display of the word, whether the user has guessed the word,  the letters and words guessed, the available letters, and the number of lives remaining.                                                                                       |
| get_words_list(self)  | This method gets a random word from a list of words and converts it to uppercase.  It also creates an underline-based display of the word based on its length.                                                                                                                                                                                                                         |
| game_play(self)       | This method displays the available letters for the user, the current stage of the hangman game, the current display of the word for the user's guesses, the number of lives remaining for the user, the letters that the user has already guessed, and the words that the user has already guessed.                                                                                    |
| display_hangman(self) | This function will display the available letters for the user, the current stage of the hangman game, the current display of the word for the user's guesses, the number of lives remaining for the user, the letters that the user has already guessed, and the words that the user has already guessed.                                                                              |
| main()                | This function is the main entry point of the game. It starts by greeting the user and prompts them to start the game.  Then it calls the username() function to get the user's name and the start_game() function to start the game. Once the game is completed, the function will say a fancy good bye to the user.                                                                   |
| **Attributes:**       |                                                                                                                                                                                                                                                                                                                                                                                        |
| Word                  | A random word that the user will try to guess with 6 attempts                                                                                                                                                                                                                                                                                                                          |
| display_word          | The word to be displayed, with unguessed letters replaced by plus sign                                                                                                                                                                                                                                                                                                                 |
| user_guessed          | Whether the user has correctly guessed the word                                                                                                                                                                                                                                                                                                                                        |
| letter_guessed        | A list of letters that have been guessed                                                                                                                                                                                                                                                                                                                                               |
| words_guessed         | A list of words that have been guessed                                                                                                                                                                                                                                                                                                                                                 |
| available_letters     | A set of uppercase letters that can be guessed                                                                                                                                                                                                                                                                                                                                         |
| lives                 | The number of lives remaining in the game       

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
- If the word or letter was succesful should appear a message in Green.
- If the user guess a wrong letter or world, the message should appear in Red.
- Should have a print statement that tells the user how long the word is.

### Outstanding Defects
- The game was supposed to have words from A to Z, but my program stuck on words from A to E, and I couldn't fix it. Yes, it looks strange, but it does not affect the main functionality of the site, the game is working normally.

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
