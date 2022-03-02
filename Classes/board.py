from tkinter import *
from tkinter import ttk
from player import player
from dice import rollDie
import random
class board:
    def __init__(self, boardArray, homeArray):
        self.players=[]
        self.window = Tk() 
        self.window.title('Agrivation')
        self.window.geometry("800x600") 
        self.canvas = Canvas(self.window, width = 800, height = 800)
        self.canvas.pack()
        self.allLoacations = boardArray
        self.homeLocations = homeArray
        self.occupiedSpots = [None] * 120
        self.create_board( boardArray)


    def create_circle(self,x, y, r): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1)
    def create_coloured_circle(self,x, y, r,colour): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1,fill=colour)

    def create_board(self,Array):
        for x in Array:
            i = 0
            xpos = 0
            for y in x:
                if i == 0:
                    xpos = y
                elif i == 1:
                    ypos = y
                    self.create_coloured_circle(xpos,y,10,"white")
                i = i+1
    def create_coloured_board(self,Array,Colour):
        for x in Array:
            i = 0
            xpos = 0
            for y in x:
                if i == 0:
                    xpos = y
                elif i == 1:
                    ypos = y
                    self.create_coloured_circle(xpos,y,10,Colour)
                i = i+1    
def popup_playercount(root,board):
    root.destroy()
    win = Toplevel()
    win.geometry("300x50")
    msg = Label(win, text="Number of Players: ")
    pcount = ttk.Combobox(win, values=[2,3,4,5,6 ]) 
    pcount.current(0)
    b = Button(win, text="Select", command = lambda: startGame(win,int(pcount.get()),board))


    msg.grid(row=1, column=0)
    pcount.grid(row=1, column=2)
    b.grid(row=1, column=3)
def startGame(root,pCount,board):
    root.destroy()
    x=0
    players = []
    while(x<pCount):
        board.players.append(player(x))
        x = x+1
    for players in board.players:
        board.create_coloured_circle(board.homeLocations[players.playerNumber][0],board.homeLocations[players.playerNumber][1],10,players.colour)
    firstTurn( board)

def firstTurn( board):
            firstPlayer = random.randint(1,len(board.players))
            print(len(board.players))
            player = board.players[firstPlayer-1]
            roll = rollDie()
            playerMSG = Label(board.window, text="Player number " + player.getPlayerNumber() + " choose a piece to move: ", fg=player.colour)   
            rollMSG = Label(board.window, text="You Rolled a  " + str(roll))
            playerMSG.place(x=550, y = 200)
            rollMSG.place(x=550, y = 220)
   
            buttons=[]
            i = 0
            k = 0
            for marble in player.marbles:
                if marble.getPosition() == player.startPosition:
                    if roll == 1 or roll == 6:
                        if k == 0:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(0,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1

                        elif k == 1:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(1,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1

                        elif k == 2:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(2,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1

                        elif k == 3:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(3,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1

                    else:
                        k=k+1
                else:
                    if k == 0:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(0,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1
                    
                    elif k == 1:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(1,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1

                    elif k == 2:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(2,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1

                    elif k == 3:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(3,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1

            if buttons == []:
                buttons.append( Button(board.window, text="You have no moves!", command = lambda: noMoves(player,board,buttons)))
                buttons[i].place(x=550, y= 250)
def newTurn( board, player):
            whoPlays = player.playerNumber+1
            if len(board.players) <= whoPlays:
                whoPlays = 0

            player = board.players[whoPlays]
            roll = rollDie()
            playerMSG = Label(board.window, text="Player number " + player.getPlayerNumber() + " choose a piece to move: ", fg=player.colour)   
            rollMSG = Label(board.window, text="You Rolled a  " + str(roll))
            playerMSG.place(x=550, y = 200)
            rollMSG.place(x=550, y = 220)
   
            buttons=[]
            i = 0
            #number of buttons created
            k = 0
            #used for functions of the buttons
            #to ensure that the fuctions of the buttons are not updating what marble to target it is using k as a pointer to the marble number
            #this needed to be seperate from i as i is used for index and location of the buttons that are created

            for marble in player.marbles:
                if marble.getPosition() == player.startPosition:
                    if roll == 1 or roll == 6:
                        if k == 0:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(0,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1
                        elif k == 1:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(1,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1

                        elif k == 2:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(2,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                            k=k+1

                        elif k == 3:
                            buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromHome(3,player,board,buttons)))
                            ypos = 250 + i * 30
                            buttons[i].place(x=550, y= ypos)
                            i=i+1
                    else:
                        k=k+1
                else:
                    if k == 0:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(0,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1
                    elif k == 1:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(1,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1
                    elif k == 2:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(2,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1
                    elif k == 3:
                        buttons.append( Button(board.window, text="Move marble "+ str(marble.marbleNumber)+" "+str(marble.position), command = lambda: moveFromSpot(3,player,board,buttons,roll)))
                        ypos = 250 + i * 30
                        buttons[i].place(x=550, y= ypos)
                        i=i+1
                        k=k+1
            if buttons == []:
                buttons.append( Button(board.window, text="You have no moves!", command = lambda: noMoves(player,board,buttons)))
                buttons[i].place(x=550, y= 250)

def moveFromHome(mNum,player,board,buttons):
    for button in buttons:
        button.destroy()
    print("move from home")
    player.marbles[mNum].position=player.moveFromHome()

    player.marblesAtHome = player.marblesAtHome - 1
    if player.marblesAtHome == 0:
        board.create_coloured_circle(board.homeLocations[player.playerNumber][0],board.homeLocations[player.playerNumber][1],10,"white")
    board.create_coloured_circle(board.allLoacations[player.marbles[mNum].position][0],board.allLoacations[player.marbles[mNum].position][1],10,player.colour)
    if not board.occupiedSpots[player.moveFromHome()]:
        board.occupiedSpots[player.moveFromHome()]=player.playerNumber
    elif board.occupiedSpots[player.moveFromHome()]:
        board.players[board.occupiedSpots[player.moveFromHome()]].marblesAtHome = board.players[board.occupiedSpots[player.moveFromHome()]].marblesAtHome + 1
        for marbles in board.players[board.occupiedSpots[player.moveFromHome()]].marbles:
            if marbles.position == player.moveFromHome():
                marbles.position = board.players[board.occupiedSpots[player.moveFromHome()]].startPosition
                break      
        board.occupiedSpots[player.moveFromHome()]=player.playerNumber
        print(board.occupiedSpots[player.moveFromHome()])
    newTurn(board,player)
def moveFromSpot(mNum,player,board,buttons,roll):
    for button in buttons:
        button.destroy()
    board.occupiedSpots[player.marbles[mNum].position]=None
    print("moving spot")
    board.create_coloured_circle(board.allLoacations[player.marbles[mNum].position][0],board.allLoacations[player.marbles[mNum].position][1],10,"white")
    player.marbles[mNum].position=player.marbles[mNum].position+roll
    if player.marbles[mNum].position >= 84:
        player.marbles[mNum].position = player.marbles[mNum].position - 83
    if player.marbles[mNum].position >= player.victoryLocation:
        if player.marbles[mNum].position-roll <= player.victoryLocation:
            player.marblesToWin = player.marblesToWin - 1
            player.marbles.pop(mNum)
            if player.marblesToWin == 0:
                Winner(board,player)
            newTurn(board,player)
    board.create_coloured_circle(board.allLoacations[player.marbles[mNum].position][0],board.allLoacations[player.marbles[mNum].position][1],10,player.colour)
    if not board.occupiedSpots[player.marbles[mNum].position]:
        board.occupiedSpots[player.marbles[mNum].position]=player.playerNumber
    elif board.occupiedSpots[player.marbles[mNum].position]:

        board.players[board.occupiedSpots[player.marbles[mNum].position]].marblesAtHome = board.players[board.occupiedSpots[player.marbles[mNum].position]].marblesAtHome + 1
        for marbles in board.players[board.occupiedSpots[player.marbles[mNum].position]].marbles:
           ### board.create_coloured_circle(board.homeLocations[players.playerNumber][0],board.homeLocations[players.playerNumber][1],10,players.colour)
            if marbles.position == player.marbles[mNum].position:
                marbles.position = board.players[board.occupiedSpots[player.marbles[mNum].position]].startPosition
                break
        board.occupiedSpots[player.marbles[mNum].position]=player.playerNumber
    newTurn(board,player)
def noMoves(player,board,buttons):
    for button in buttons:
        button.destroy()
    print("cant move")
    newTurn(board,player)
def Winner(board, player):
    print("The winner is player " + str(player.playerNumber+1))
    msg = Label(board.window, text="Player "+str(player.playerNumber+1)+" Wins",font=("Courier", 15))
    board.canvas.destroy()
    msg.place(x=150, y = 200)

boardArray = [[340,280],[300,100],[320,100],[340,100],[360,100],[380,100],[380,120],[380,140],[380,160],
[380,180],[380,200],[400,190],[420,180],[440,170],[460,160],[480,150],[490,170],[500,190],[510,210],[520,230],
[500,240],[480,250],[460,260],[440,270],[420,280],[440,290],[460,300],[480,310],[500,320],[520,330],[510,350],
[500,370],[490,390],[480,410],[460,400],[440,390],[420,380],[400,370],[380,360],[380,380],[380,400],[380,420],
[380,440],[380,460],[360,460],[340,460],[320,460],[300,460],[300,440],[300,420],[300,400],[300,380],[300,360],
[280,370],[260,380],[240,390],[220,400],[200,410],[190,390],[180,370],[170,350],[160,330],[180,320],[200,310],
[220,300],[240,290],[260,280],[240,270],[220,260],[200,250],[180,240],[160,230],[170,210],[180,190],[190,170],
[200,150],[220,160],[240,170],[260,180],[280,190],[300,200],[300,180],[300,160],[300,140],[300,120]] 
#home Locations

homeArray = [[410,100],[270,460],[535,255],[145,305],[460, 450],[215,120]]

theBoard = board(boardArray, homeArray)




# create x, horizontal y, vertical
stGameBut = Button(theBoard.window, text="Start Game", command = lambda:popup_playercount(stGameBut,theBoard))
stGameBut.place(x=600, y= 200)
exitGameButton = Button(theBoard.window, text="Exit", command = theBoard.window.destroy)
exitGameButton.place(x=700, y = 500)

theBoard.window.mainloop()
i=0
