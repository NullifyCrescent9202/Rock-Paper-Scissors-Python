import random
choices = ["rock", "paper", "scissors"]
player1 = input("Enter choice: ")
player2 = random.choice(choices)
Tie = 0

def game(p1, p2):
    
    if  p1 == p2:
        return("Tie")
     
    elif p1 == "rock" and p2 == "paper":
        return("player2 wins")
    
    elif p1 == "paper" and p2 == "rock":
        return("player1 wins")
    
    elif p1 == "scissors" and p2 == "rock":
        return("player2 wins")
    
    elif p1 == "rock" and p2 == "scissors":
        return("player1 wins")
    
    elif p1 == "paper" and p2 == "scissors":
        return("player2 wins")
    
    elif p1 == "scissors" and p2 == "paper":
        return("player1 wins")
    
print(game(player1, player2))