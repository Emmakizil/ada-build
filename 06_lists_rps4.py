import random

def choose_rps():
  r = random.randint(0,2)
  
  if r == 0:
      return "rock"
  elif r == 1:
      return "scissors"
  else:
      return "paper"

def rps_function(player1, player2):
  if player1 == player2:
    print("It's a tie!")
  elif player1 == "scissors":
    if player2 == "rock":
      print ("Player 2 won!")
    else:
      print("Player 1 won!")
  elif player1 == "rock":
    if player2 == "scissors":
      print ("Player 1 won!")
    else:
      print("Player 2 won!")
  else:
    if player2 == "scissors":
      print ("Player 2 won!")
    else:
      print("Player 1 won!")
       

def play_again():
  r = random.randint(0,1)
  if r == 0:
    return True
  else:
    return False

play = True

print("Welcome to Rock, Paper, Scissors!\n")
while play == True:
  player1 = choose_rps()
  player2 = choose_rps()

  print("Player 1 chose", player1,".")
  print("Player 2 chose", player2,".")

  rps_function(player1, player2)

  print(" ")

  play = play_again()

print("Thank you for playing!")