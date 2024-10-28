import random

player_score = 0
cpu_score = 0
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

while True:
    cpu_choice = random.choice(choices)
    player_choice = input("Enter your choice: ").lower().strip()
    if player_choice not in choices:
        print("Invalid choice")
        continue
    else:
        print("Rock...Paper...Scissors...Lizard...Spock...Shoot!")
        print("Your opponent played ", cpu_choice)
        if player_choice == cpu_choice:
            print("It's a tie!")
        elif player_choice == 'rock':
            if cpu_choice == 'scissors':
                print("Your Rock crushes the Scissors. You win!")
                player_score += 1
            elif cpu_choice == 'lizard':
                print("Your Rock crushes the Lizard. You win!")
                player_score += 1
            elif cpu_choice == 'paper':
                print("Your Opponent's Paper covers your Rock. You lose!")
                cpu_score += 1
            elif cpu_choice == 'spock':
                print("Your Opponent's Spock vaporizes your Rock. You lose!")
                cpu_score += 1
        elif player_choice == 'paper':
            if cpu_choice == 'rock':
                print("Your Paper covers the Rock. You win!")
                player_score += 1
            elif cpu_choice == 'spock':
                print("Your Paper disproves Spock. You win!")
                player_score += 1
            elif cpu_choice == 'scissors':
                print("Your Opponent's Scissors cuts your Paper. You lose!")
                cpu_score += 1
            elif cpu_choice == 'lizard':
                print("Your Opponent's Lizard eats your Paper. You lose!")
                cpu_score += 1
        elif player_choice == 'scissors':
            if cpu_choice == 'paper':
                print("Your Scissors cuts the Paper. You win!")
                player_score += 1
            elif cpu_choice == 'lizard':
                print("Your Scissors decapitates the Lizard. You win!")
                player_score += 1
            elif cpu_choice == 'rock':
                print("Your Opponent's Rock crushes your Scissors. You lose!")
                cpu_score += 1
            elif cpu_choice == 'spock':
                print("Your Opponent's Spock smashes your Scissors. You lose!")
                cpu_score += 1
        elif player_choice == 'lizard':
            if cpu_choice == 'spock':
                print("Your Lizard poisons Spock. You win!")
                player_score += 1
            elif cpu_choice == 'paper':
                print("Your Lizard eats the Paper. You win!")
                player_score += 1
            elif cpu_choice == 'rock':
                print("Your Opponent's Rock crushes your Lizard. You lose!")
                cpu_score += 1
            elif cpu_choice == 'scissors':
                print("Your Opponent's Scissors decapitates your Lizard. You lose!")
                cpu_score += 1
        elif player_choice == 'spock':
            if cpu_choice == 'scissors':
                print("Your Spock smashes the Scissors. You win!")
                player_score += 1
            elif cpu_choice == 'rock':
                print("Your Spock vaporizes the Rock. You win!")
                player_score += 1
            elif cpu_choice == 'paper':
                print("Your Opponent's Paper disproves your Spock. You lose!")
                cpu_score += 1
            elif cpu_choice == 'lizard':
                print("Your Opponent's Lizard poisons your Spock. You lose!")
                cpu_score += 1
        print("Player: ", player_score, " - CPU: ", cpu_score)