import random

# Runs one full game of Rock, Paper, Scissors.
def play_game():

    # Starting scores.
    player_score = 0
    computer_score = 0

    # Possible choices for the computer.
    options = ["rock", "paper", "scissors"]

    # Keep playing until someone reaches 4 points.
    while player_score < 4 and computer_score < 4:

        # Get the player's choice.
        player_choice = input("SHOOT! (Rock, Paper, Scissors): ").lower()

        # Randomly choose for the computer.
        computer_choice = random.choice(options)

        # Display both choices.
        result = f"You: {player_choice} AI Player: {computer_choice}"

        # -------- ROCK --------

        if player_choice == "rock" and computer_choice == "paper":
            print(result)
            print("Paper beats rock. You lose :(")
            computer_score += 1

        elif player_choice == "rock" and computer_choice == "scissors":
            print(result)
            print("Rock beats scissors! YOU WIN!")
            player_score += 1

        elif player_choice == "rock" and computer_choice == "rock":
            print(result)
            print("It's a tie.")

        # -------- PAPER --------

        elif player_choice == "paper" and computer_choice == "rock":
            print(result)
            print("Paper beats rock! YOU WIN!")
            player_score += 1

        elif player_choice == "paper" and computer_choice == "scissors":
            print(result)
            print("Scissors beat paper. You lose :(")
            computer_score += 1

        elif player_choice == "paper" and computer_choice == "paper":
            print(result)
            print("It's a tie.")

        # -------- SCISSORS --------

        elif player_choice == "scissors" and computer_choice == "rock":
            print(result)
            print("Rock beats scissors. You lose :(")
            computer_score += 1

        elif player_choice == "scissors" and computer_choice == "paper":
            print(result)
            print("Scissors beat paper. YOU WIN!")
            player_score += 1

        elif player_choice == "scissors" and computer_choice == "scissors":
            print(result)
            print("It's a tie.")

        # Player entered something invalid.
        else:
            print("Invalid choice")

        # Show the score after each round.
        print(f"Your Score: {player_score}")
        print(f"AI Score: {computer_score}")
        print()

    # Show who won the game.
    if player_score == 4:
        print("🎉 Congratulations! You won the game! TAKE THAT AI 🖕😛🖕")
    else:
        print("💻 The AI wins the game.")


# Main menu.
while True:

    print("1. Play Game")
    print("2. Quit")

    # Get the user's menu choice.
    choice = input("Choose an option: ")

    # Start the game.
    if choice == "1":
        play_game()

    # Exit the program.
    elif choice == "2":
        print("Goodbye!")
        break

    # Handle invalid menu choices.
    else:
        print("Invalid choice.")
