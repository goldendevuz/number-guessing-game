## Number Guessing Game - CLI Project

### Overview

The Number Guessing Game is a command-line interface (CLI) based game where the player attempts to guess a randomly
generated number between 1 and 100. The game provides three difficulty levels: Easy, Medium, and Hard, each affecting
the number of attempts allowed. The game gives feedback on each incorrect guess, indicating whether the correct number
is higher or lower than the user's guess.

### How to Play

1. **Start the Game**: Run the game from the command line. Upon starting, a welcome message and the rules of the game
   will be displayed.

2. **Select Difficulty Level**: Choose the difficulty level:
    - **Easy**: 10 chances to guess the number.
    - **Medium**: 5 chances to guess the number.
    - **Hard**: 3 chances to guess the number.

3. **Enter Your Guess**: Input your guess for the number. The game will provide feedback:
    - If your guess is **correct**, a congratulatory message will display along with the number of attempts it took to
      guess correctly.
    - If your guess is **incorrect**, the game will inform you whether the correct number is greater or less than your
      guess.

4. **End of Game**: The game ends when you either guess the correct number or run out of chances. At the end of each
   round, you will be given an option to play again or exit.

### Example Gameplay

\`\`\`
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:

1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts.
\`\`\`

### Additional Features

To make the game more engaging, consider implementing the following features:

1. **Multiple Rounds**: Allow users to play multiple rounds of the game without restarting the program. After each
   round, ask the user if they want to play again.

2. **Timer**: Add a timer to track how long it takes the user to guess the correct number.

3. **Hint System**: Provide clues if the user is struggling to guess the number. This could be in the form of a range or
   a "hot/cold" indicator.

4. **High Score Tracking**: Keep track of the user's best score, which is the fewest number of attempts taken to guess
   the correct number on each difficulty level.

### Getting Started

1. Clone the repository to your local machine.
2. Run the game from the command line using Python:
   \`\`\`bash
   python number_guessing_game.py
   \`\`\`

## Idea Source

The idea for the Expense Tracker CLI project was inspired
by [roadmap.sh's Number Guessing Game project](https://roadmap.sh/projects/number-guessing-game). Visit the link to see
more details and learn about similar project ideas.

### Contribution

Contributions are welcome! If you have any ideas or improvements for the game, feel free to fork the repository and
submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [goldendevuz@gmail.com].

---

Enjoy the game, and happy guessing!
