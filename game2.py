import random

print("welcome to rock paper scissors")


# User Inputs
user_choice = input("Please make a selection 'rock', 'paper', 'scissors'): ")
#You Chose: rock
print("You chose:", user_choice) 

user_choice = user_choice.lower()

# Validate User Inputs

if user_choice not in valid_options:
    print("oops invalid try again")
exit() # quit()

# Computer Choice

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("computer_choice:", computer_choice)

# Determine The Winner

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