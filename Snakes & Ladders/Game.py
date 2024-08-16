from abc import abstractmethod
from itertools import cycle
import random
import time

class GameSystem:
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not GameSystem.__shared_instance:
            GameSystem()
        return GameSystem.__shared_instance
    
    def __init__(self):
        if GameSystem.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            GameSystem.__shared_instance = self
            self.players = []
            
    def initializeGame(self, numberOfPlayer: int):
        self.baordObj = Board()
        self.baordObj.initialize()
        self.baordObj.add_snakes([[0,1,2,3], [2,2,3,6]])
        self.baordObj.add_ladders([[2,3, 5,6], [2,5, 7,8]])
        for i in range(numberOfPlayer):
            name = input(f"Player{i+1} Name: ")
            self.players.append(Player(name, i+1, self.baordObj.board[0][0]))
    
    def playGame(self):
        for player in cycle(self.players):
            print(f"Player:{player.name} turn")
            while True:
                diceNumber = random.randint(1,6)
                spot = player.getSpot()
                i, j = spot.row, spot.col
                newNumber = i*10 + j + diceNumber
                if newNumber > 99:
                    continue
                elif newNumber == 99:
                    print(f"Player:{player.name} Won the Game !")
                    return
                i, j = newNumber//10, newNumber%10
                newSpot = self.baordObj.board[i][j]
                player.setSpot(newSpot)
                if newSpot.obstacle:
                    newSpot.move(player)
                print(f"Player: {player.name} is moved to position: {player.spot.row}, {player.spot.col}")
                time.sleep(3)
                break

class Board:
    def __init__(self):
        self.board = []
        
    def initialize(self):
        for i in range(10):
            row = []
            for j in range(10):
                row.append(Spot(i, j))
            self.board.append(row)

    def add_snakes(self, snakes):
        for si,sj,ei,ej in snakes:
            startSpot = self.board[si][sj]
            endSpot = self.board[ei][ej]
            spot = self.board[si][sj]
            spot.obstacle = Snake(startSpot, endSpot)

    def add_ladders(self, ladders):
        for si,sj,ei,ej in ladders:
            startSpot = self.board[si][sj]
            endSpot = self.board[ei][ej]
            spot = self.board[si][sj]
            spot.obstacle = Ladder(startSpot, endSpot)

class Player:
    def __init__(self, name, playerid, spot):
        
        self.name = name
        self.playerid = playerid
        self.spot = spot

    def getSpot(self):
        return self.spot
    
    def setSpot(self, spot):
        self.spot = spot

class Spot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.obstacle = None

    def move(self, player: Player):
        self.obstacle.move(player)
        
    
class Obstacle:
    @abstractmethod
    def move():
        pass

class Snake(Obstacle):
    def __init__(self, startSpot: Spot, endSpot: Spot):
        self.startSpot = startSpot
        self.endSpot = endSpot
    
    def move(self, player: Player):
        player.setSpot(self.endSpot) 
        print("Player encountered snake.")


class Ladder(Obstacle):
    def __init__(self, startSpot: Spot, endSpot: Spot):
        self.startSpot = startSpot
        self.endSpot = endSpot

    def move(self, player: Player):
        player.setSpot(self.endSpot) 
        print("Player encountered snake.")
