from Classes.player import player
from Classes.dice import rollDie
from Classes.bc import board
from Classes.marble import marble
from Classes.board import *
playerCount = 0
players = []
while(1>=playerCount or playerCount>6):
    playerCount = int(input("How many Players(1-6): "))
newGame = board()
x= 0
# creates a game with the selected number of players between 1 and 6
while(x<playerCount):
    players.append(player(x))
    x = x+1
    print(x)
# for each player creates 4 pieces and placers them in the assigned starting positions
isThereAWinner = False
winner = ""
# A flag for checking if a player has won
currentRoll = 0
rolledASix = False
currentPositions = []
availableMoves = []

while(isThereAWinner==False):
    for player in players:
        currentRoll = rollDie()
        print("You Rolled: ", currentRoll)

        currentPositions = player.getAllPositions()
        if(currentRoll==6):
            rolledASix = True
        if(currentRoll!= 1) and (currentRoll!= 6):
            for position in currentPositions:
                if position.getPosition() != player.startPosition:
                    availableMoves.append(position)
        else:
            for position in currentPositions:
                availableMoves.append(position)
        if not availableMoves:
            print("No available moves")
        else:            
            print("Choose a piece to move: ")
            i = 0
            for position in availableMoves: 
                i=i+1
                print(i,": ", position.getPosition())
            selectedPiece = 0
            while(selectedPiece >= 5 or selectedPiece <= 0): 
                selectedPiece= int(input("Select object to move: "))
            availableMoves[selectedPiece-1]=availableMoves[selectedPiece-1]+currentRoll
            if availableMoves[selectedPiece-1]>80:
                availableMoves[selectedPiece-1]=availableMoves[selectedPiece-1]-80
                print(availableMoves[selectedPiece-1])
                player.setNewPosition(availableMoves[selectedPiece-1], selectedPiece)
                for position in player.Position:
                    if position.getPosition() >= 80:
                        isThereAWinner = True
                        winner = player.playerNumber
        availableMoves = []
        rolledASix = False
        
    
print("The winner is player number ")
print( winner)

