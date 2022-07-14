import random

print("welcome to rock paper scissors")


# User Inputs
user_choice = input("Please make a selection 'rock', 'paper', 'scissors'): ")
#You Chose: rock
print("You chose:", user_choice) 

user_choice = user_choice.lower()

# Validate User Inputs



# Computer Choice

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("computer_choice:", computer_choice)

# Determine The Winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")
# Display Results


# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!