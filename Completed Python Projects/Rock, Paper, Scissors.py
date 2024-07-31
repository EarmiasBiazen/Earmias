import random

def get_comp_choice():
    list_1 = ['rock', 'paper', 'scissors']
    return random.choice(list_1)

def determine_winner(user, comp_choice):
    if user == "rock" and comp_choice == 'paper':
        return 'You lose!'
    elif user == "scissors" and comp_choice == 'rock':
        return 'You lose!'
    elif user == "paper" and comp_choice == 'scissors':
        return 'You lose!'
    elif user == "rock" and comp_choice == 'scissors':
        return 'You win!'
    elif user == "scissors" and comp_choice == 'paper':
        return 'You win!'
    elif user == "paper" and comp_choice == 'rock':
        return 'You win!'
    elif user == comp_choice:
        return "It's a draw!"
    else:
        return 'Invalid input! Please choose rock, paper, or scissors.'

def main():
    while True:
        print('Rock, Paper, Scissors... (type "quit" to end the game)\n')
        user = input("You're choice: ").lower()
        if user == 'quit':
            print('Thanks for playing!')
            break
        
        comp_choice = get_comp_choice()
        print(f"Computer chose: {comp_choice}")
        
        result = determine_winner(user, comp_choice)
        print(result)

if __name__ == "__main__":
    main()

