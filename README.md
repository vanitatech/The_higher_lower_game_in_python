# Higher or Lower Game 

A simple **Higher or Lower** guessing game built with Python.

The player is shown two randomly selected people/accounts and has to guess which one has the higher number of followers. The game continues until the player makes an incorrect guess.

## How the Game Works

1. Two random accounts are selected from a dataset.
2. The details of both accounts are displayed.
3. The player chooses either **A** or **B**.
4. The program compares their follower counts.
5. If the answer is correct, the player's score increases.
6. If the answer is incorrect, the game ends and the final score is displayed.

##  Technologies Used

* Python
* `random` module
* Functions
* Loops
* Conditional statements
* Lists
* Dictionaries
* User input
* Python modules/imports

## Project Structure

```text
Higher_Lower_Game/
│
├── main.py
├── art.py
├── game_data.py
└── README.md
```

### `main.py`

Contains the main game logic, including:

* Selecting random accounts
* Displaying account information
* Getting user input
* Comparing follower counts
* Tracking the score
* Controlling the game loop

### `art.py`

Contains the ASCII art used by the game.

### `game_data.py`

Contains the account data used by the game.

## What I Learned

This project helped me practise:

* Creating and calling Python functions
* Passing arguments to functions
* Returning Boolean values from functions
* Working with lists of dictionaries
* Accessing dictionary values using keys
* Using `random.sample()` to select multiple random items
* Using `while` loops to control a game
* Using conditional logic with `if/else`
* Keeping track of a changing score
* Splitting a program across multiple Python files
* Importing functions, variables and data from other modules

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd Higher_Lower_Game
```

Run the game:

```bash
python main.py
```

## Example

```text
Compare A: Cristiano Ronaldo, Footballer, Portugal

VS

Against B: Lionel Messi, Footballer, Argentina

Who has more followers? Type 'A' or 'B': A

You're right! Current score 1
```

## Possible Future Improvements

Some features I could add in the future:

* Prevent the same account from appearing twice in a row
* Add difficulty levels
* Add a high-score system
* Improve the user interface
* Add input validation for invalid answers
* Add automated tests for the game logic
* Create a graphical or web-based version of the game

## Project Background

This project was created as part of my Python learning journey to practise programming fundamentals, problem-solving and working with structured data.
