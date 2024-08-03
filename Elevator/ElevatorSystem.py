import sys, os
sys.path.append(os.path.dirname(__file__))
from enum import Enum
from ElevatorController import ElevatorManager, ExternalRequestProcessor, InternalRequestProcessor, ExternalRequest, InternalRequest

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"

class ElevatorSystem:
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not ElevatorSystem.__shared_instance:
            ElevatorSystem()
        return ElevatorSystem.__shared_instance
    
    def __init__(self):
        if ElevatorSystem.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            ElevatorSystem.__shared_instance = self
        
    def initializeElevatorSystem(self, noOfElevator, noOfFloor):
        self.noOfElevator = noOfElevator
        self.noOfFloor = noOfFloor

        print(f"Initializing elevator system with {self.noOfFloor} floors and {self.noOfElevator} elevators!");
        self.elevatorManager = ElevatorManager.getInstance()
        self.elevatorManager.initializeEelvator(self.noOfElevator)

        self.externalRequestProcessor = ExternalRequestProcessor()
        self.internalRequestProcessor = InternalRequestProcessor()
  
    def setEvelvatorSelectionAlgo(self, evelvatorSelectionStretagy):
        self.externalRequestProcessor.setEvelvatorSelectionStretagy(evelvatorSelectionStretagy)
    
    def sendExternalRequest(self, srcFloor, direction):
        externalRequest = ExternalRequest(srcFloor, direction)
        self.externalRequestProcessor.processRequest(externalRequest)

    def sendInternalRequest(self, destFloor, elevatorid):
        internalRequest = InternalRequest(destFloor, elevatorid)
        self.internalRequestProcessor.processRequest(internalRequest)

    
