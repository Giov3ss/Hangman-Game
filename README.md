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

2. [Features](#features)

3. [Future Features](#future-features) 

4. [Data Model/ Classes](#data-model-classes)

5. [Testing](#testing)
    * [Validation Testing](#validation-testing)
    * [Manual Testing](#manual-testing)
    * [Defect Tracking](#defect-tracking)
    * [Commenting Code](#commenting-code)

4. [Technology Used](#technology-used)  
    * [Language Used](#languages-used)
    * [Tools and Libraries](#tools-and-libraries)

5. [Testing](#testing)

6. [Deployment](#deployment)  
  
7. [Credits](#credits)
    * [Media](#media)  

- - -

# **Table of Contents**
## UX Development

### Project Goal 
- Ensuring that the game are working with no errors and perfectly.

## User Goal
- Want to easily navigate through the game with simple inputs.

## User Stories
- Be able to type my name.
- Show me the wrong words.
- Show me the correct word at the end.
- Show me an optional message if I want to try again the game.

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

## Future Features

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

## Future Features

## Testing

### Validation Testing

- run.py
<img width="1104" alt="image" src="https://user-images.githubusercontent.com/112728772/212193420-025a08a2-8044-4f93-97ac-05eb3243bdff.png">

- words.py
<img width="1102" alt="image" src="https://user-images.githubusercontent.com/112728772/212193643-66a6edd4-bc30-4c36-91c3-4ac16bda8804.png">

- stage.py
<img width="1144" alt="image" src="https://user-images.githubusercontent.com/112728772/212193823-f97440e1-ad57-4758-bf57-6c25e0d9593d.png">


## Technology Used

### Languages Used 

- Python

### Tools and libraries
- [coolors.co](https://coolors.co/623d2b-935836-6c6f70-ebebed-b88a68) - The color scheme that was used on the site.
- [Google Fonts](https://fonts.google.com/) - Both fonts were used by Google Fonts.
- [Balsamiq](https://balsamiq.com/) Used to build the wireframes.
- [Chrome Devtools](https://developer.chrome.com/docs/devtools/) - Used extensively to experiment with grid, flexbox and general responsiveness. 
- [Gitpod](https://www.gitpod.io/) - Used to create and host the website.
- [Github](https://github.com/) - Used to deploy the website.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used to creat an image displaying the homepage on multiple devices.
- [Favicon](https://favicon.io/) - Used to create the Icon for the website.
- [CSS Gradient](https://cssgradient.io/) To match the colours.
- [Browserstack](https://www.browserstack.com/) Provided browser compatibility with real desktop and mobile devices.
- [Table Generator](https://www.tablesgenerator.com/) Used to make a table of de devices and desktops tested.

### Testing

[testing.md](testing.md) 

### Deployment 

[https://giov3ss.github.io/Stuff4Trip/](https://giov3ss.github.io/Stuff4Trip/)

- The site was deployed to Github pages.

### Run Locally With GitPod

1. Go to the terminal
2. Type Git command: python3 -m http.server
3. A pop-up message will appear on the right-hand side, where Open Browser should be clicked
4. A new page opens where the site is available

* You can deploy this locally if you have the chrome gitpod extension installed
* Just click the green button in github when in chrome browser to start a gitpod instance

### Deploy to GitHub Pages

1. Navigate to the settings tab in the GitHub repository
    <img width="1395" alt="image" src="https://user-images.githubusercontent.com/112728772/204665064-f77f28cf-9fdb-4ed4-a6c9-0aad4b7f3853.png">

2. Once in settings, navigate to the pages tab on the left of the page
    <img width="327" alt="image" src="https://user-images.githubusercontent.com/112728772/204665128-ea0176da-4c5c-4c30-8291-093c810e975c.png">
 
3. Under source, select branch ‘main’ and then click ‘save’
    <img width="770" alt="image" src="https://user-images.githubusercontent.com/112728772/204665218-93e10ba7-633b-416b-9098-5a82a1d36c08.png">

4. Page will not automatically refresh and show a detailed ribbon display to indicate deployment
    <img width="831" alt="image" src="https://user-images.githubusercontent.com/112728772/204665292-5184480b-41cd-4375-9e72-c0e5f590eaab.png">


### To Fork the Repository 

To make a copy or ‘fork’ the repository:

1. Log into GitHub and locate repository
2. On the right hand side of the page select the ‘fork’ option to create and copy of the original

### To create a Local Clone 

1. under the repository name, click on the ‘code’ tab
2. in the clone box, HTTPS tab, click on the clipboard icon 
3. in your IED open GitBash
4. Changed the current working directory to the location you want the cloned directory to be made
5. Type ‘git clone’ and then paste the URL copied from GitHub
6. press enter and the local clone will be created 


### Credits
 - I would like to thank my mentor Malia for her help, tips and advise all the time.
 - Instructions on how to implement the HTML and CSS code using GitHub was taken from the HTML, CSS and Javascript course from Code Institute.
 - [Code Institute](https://codeinstitute.net/nl/) With the JavaScript Essentials.
 - [Freshman.tech](https://freshman.tech/todo-list/) Used to understand about the To-do-list project.
 - [Youtube](https://www.youtube.com/watch?v=MkESyVB4oUw&t=2010s) This video inspired me and helped me a lot to understanding more about JavaScript and how to start my project. 
 - [Stackoverflow](https://stackoverflow.com) When I was in doubt about something.
 - [CSS Gradient](https://cssgradient.io/) Helped me to match the background colors.
 - [CSS Tricks](https://css-tricks.com/perfect-full-page-background-image/) Helped me to keep the background image in the same spot, so the user can scroll down and the image does not break.
 - [JSON Local Storage](https://frontend.turing.edu/) Helped me to understand a bit about Local Storage using JSON.
 

### Media 
 - The Main-Image are from the free website: [Pexels](https://www.pexels.com/)
 - Icon for the website: [Favicon](https://favicon.io/)
