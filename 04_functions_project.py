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

game = rps('rock', 'rock')