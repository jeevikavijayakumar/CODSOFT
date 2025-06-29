import random

# Initialize scores
user_score = 0
computer_score = 0


options = ["rock", "paper", "scissors"]

print("Welcome to the Rock, Paper, Scissors Game!")

while True:
    print("\nChoose one: rock / paper / scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(options)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")


    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("You lose this round.")
        computer_score += 1


    print(f"\nScores:\nYou: {user_score} | Computer: {computer_score}")

    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break
