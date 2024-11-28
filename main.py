"""Welcome to the Number Guessing Game!
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
Congratulations! You guessed the correct number in 4 attempts."""
import random


def main() -> None:
    choice_input: str = input("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: """)
    choice: int = int(choice_input) if choice_input in ("1", "2", "3") else 0
    level: str = "Easy" if choice == 1 else "Medium" if choice == 2 else "Hard"
    if choice:
        guess_input: str = input(f"""
Great! You have selected the {level} difficulty level.
Let's start the game!

Enter your guess: """)
        answer: int = random.randint(1, 100)
        max_attempts: int = 10 if choice == 1 else 5 if choice == 2 else 3
        left_attempts: int = max_attempts - 1
        while left_attempts > 0:
            left_attempts -= 1
            guess: int = int(guess_input) if guess_input in map(str, range(1, 100)) else 0
            if guess:
                if guess > answer:
                    print("Incorrect! The number is less than", guess)
                elif guess < answer:
                    print("Incorrect! The number is greater than", guess)
                elif guess == answer:
                    print("Congratulations! You guessed the correct number in", max_attempts - left_attempts,
                          "attempts.")
                    break
                guess_input = input("\nEnter your guess: ")
        if not left_attempts:
            print("You lose")

if __name__ == "__main__":
    main()
