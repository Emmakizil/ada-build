import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    return random.choice(["rock", "paper", "scissors"])

def rps(player1, player2):
    if player1 == 'paper':
        if player2 == 'rock':
            print("Player 1 won!")
        elif player2 == "scissors":
            print("player 2 won!")
        else:
            print("It's a tie!")
    elif player1 == 'rock':
        if player2 == 'paper':
         print("Player 2 won!")
        elif player2 == "scissors":
            print("player 1 won!")
        else:
         print("It's a tie!")
    elif player1 == 'scissors':
        if player2 == 'rock':
             print("Player 2 won!")
        elif player2 == "paper":
         print("player 2 won!")
        else:
            print("It's a tie!")

def play_again():
    #return random.choice([True, False])
    user_input = input("Would you like to play again? Yes or No? ")
    if user_input.lower() == "yes":
        return True
    else:
        return False

def run_game():
    play = True
    while play:
        #assign rock, paper, scissors to players
        player1 = choose_rps()
        player2 = choose_rps()

        #each users output
        print(f'\nPlayer 1 chose {player1}')
        print(f"Player 2 chose {player2}\n")
        
        #output the winner
        rps(player1, player2)
        print('\n-----\n')
        
        play = play_again()
        
    print("\nThank You For Playing!")

#run_game()

def run_game_n_times(n):
    for i in range(n):
        print (f'Game number: {i + 1}')
       
        player1 = choose_rps()
        player2 = choose_rps()

        #each users output
        print(f'\nPlayer 1 chose {player1}')
        print(f"Player 2 chose {player2}\n")
        
        #output the winner
        rps(player1, player2)
        print('\n-----\n')
       
    print("\nThank You For Playing!")

run_game_n_times(3)