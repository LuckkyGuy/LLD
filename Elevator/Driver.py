import sys, os
sys.path.append(os.path.dirname(__file__))

from ElevatorSystem import ElevatorSystem, Direction
from ElevatorController import OddEvenElevatorSelectionStrategy

def main():
    elevatorSystem = ElevatorSystem.getInstance()
    
    elevatorSystem.initializeElevatorSystem(4, 12)

    elevatorSystem.setEvelvatorSelectionAlgo(OddEvenElevatorSelectionStrategy())
    
    elevatorSystem.sendExternalRequest(1, Direction.UP)
    elevatorSystem.sendInternalRequest(3, 2)
    
if __name__ == '__main__':
    main()
    
