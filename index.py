import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
draws = 0

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        if user_choice in choices or user_choice == 'q':
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score, draws

    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print("--------------------------------")
    print(f"Your score: {user_score}\nComputer score: {computer_score}\nDraws: {draws}\n")

while True:
    user_choice = get_user_choice()

    if user_choice == 'q':
        break

    print(f"\nYour choice: {user_choice} | Computer's choice: {get_computer_choice()}")
    print("********************************")
    determine_winner(user_choice, get_computer_choice())
