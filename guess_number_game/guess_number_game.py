import random
def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Your number of attempts will depend on the selected difficulty level.")

def select_difficulty():
    print("Select difficulty level:")
    print("1: Easy - 10 chances")
    print("2: Medium - 5 chances")
    print("3: Hard - 3 chances")
    while True:
        choice = input("Enter your choice '1, 2 or 3': ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        elif choice == '3':
            return 3
        else:
            print("Incorrect choice. Please select '1, 2 or 3'")

def get_number_to_guess():
    return random.randint(1, 100)

def play_game():
    chances = select_difficulty()
    number_to_guess = get_number_to_guess()
    attempts = 0
    print(f"Great! You have selected the difficulty level with {chances} chances.")
    print("Let's start a game!") 
    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        attempts += 1
        
        if guess < number_to_guess:
            print(f"Incorrect! The number is greater than {guess}.")
        elif guess > number_to_guess:
            print(f"Incorrect! The number is less than {guess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return attempts
    print(f"Sorry, you've run out of chances. The correct number was {number_to_guess}.")
    return attempts

def main():
    while True:
        welcome_message()
        attempts = play_game()
        play_again = input("\nDo you want to play again? (yes or no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
