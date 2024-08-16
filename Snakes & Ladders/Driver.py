from abc import ABC, abstractmethod
import os, sys
sys.path.append(os.path.dirname(__file__))

from Game import GameSystem


def main():
    gameSystem = GameSystem().getInstance()
    gameSystem.initializeGame(3)
    gameSystem.playGame()

    
if __name__ == '__main__':
    main()