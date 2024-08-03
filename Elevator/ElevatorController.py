from abc import abstractmethod

class ExternalRequest:
    def __init__(self, srcFloor, direction):
        self.__srcFloor = srcFloor
        self.__directionToGo = direction
    
    def getSrcFloor(self):
        return self.__srcFloor
    
    def getDirection(self):
        return self.__directionToGo
    
    def setSrcFloor(self, floor):
        self.__srcFloor = floor
    
    def setDirection(self, direction):
        self.__directionToGo = direction
    
    
class InternalRequest:
    def __init__(self, destFloor, srcElevatorId):
        self.__destFloor = destFloor
        self.__srcElevatorId = srcElevatorId

    def getSrcElevatorId(self):
        return self.__srcElevatorId
    
    def getDestFloor(self):
        return self.__destFloor
    
    def setSrcElevatorId(self, floor):
        self.__srcElevatorId = floor
    
    def setDestFloor(self, destFloor):
        self.__destFloor = destFloor
        
class ExternalRequestProcessor:
    
    def __init__(self):
        self.elevatorSelectionStrategy = OddEvenElevatorSelectionStrategy()
    
    def setEvelvatorSelectionStretagy(self, elevatorSelectionStrategy):
        self.elevatorSelectionStrategy = elevatorSelectionStrategy

    def processRequest(self, extReq: ExternalRequest):
        elevatorId = self.elevatorSelectionStrategy.selectElevator(extReq)
        elevatorManager = ElevatorManager.getInstance()
        elevator = elevatorManager.getElevator(elevatorId)
        elevator.moveToFloor(extReq.getSrcFloor())
        
class InternalRequestProcessor:

    def processRequest(self, intReq: InternalRequest):
        elevatorManager = ElevatorManager.getInstance()
        elevator = elevatorManager.getElevator(intReq.getSrcElevatorId())
        elevator.moveToFloor(intReq.getDestFloor())
        

class ElevatorManager:
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not ElevatorManager.__shared_instance:
            ElevatorManager()
        return ElevatorManager.__shared_instance
    
    def __init__(self):
        if ElevatorManager.__shared_instance:
            raise Exception("This class is a Singleton class !")
        ElevatorManager.__shared_instance = self
        self.__elevatorMap = dict()
    
    def initializeEelvator(self, noOfElevator):
        for i in range(noOfElevator):
            self.__elevatorMap[i] = Elevator(i)
    
    def getElevator(self, evelatorId):
        return self.__elevatorMap[evelatorId]
    

class Elevator:
    def __init__(self, elevatorId):
        self.elevatorController = ElevatorController()
        self.__elevatorId = elevatorId

    def getElevatorId(self):
        return self.__elevatorId
    
    def moveToFloor(self, destFloor):
        self.elevatorController.moveElevatorToFloor(destFloor)


class ElevatorController:
    def __init__(self):
        self.elevatorMovementStrategy = SSTFElevatorControlStrategy()
        self.state = ElevatorCurrState()

    def moveElevatorToFloor(self, dstFloor):
        self.elevatorMovementStrategy.findNextStop(dstFloor)
        


class ElevatorCurrState:
    def __init__(self):
        self.direction = Direction.UP
        self.state = ElevatorStatus.IDLE
        self.currFloor = 0


class Direction:
    UP = "UP"
    DOWN = "DOWN"

class ElevatorStatus:
    IDLE = "IDLE"
    MOVING = "MOVING"
    STOPPED = "STOPPED"

class IElevatorControlStrategy:
    def findNextStop(dstFloor):
        pass

class FCFSElevatorControlStrategy(IElevatorControlStrategy):
    def findNextStop(self, floorNum):
        print(f"Applying First Come First Serve Algorithm and Moving elevator to floor {floorNum}")
        # returning 1 for demo purposes, should be determining next stop and returning that
        return 1
        
class SSTFElevatorControlStrategy(IElevatorControlStrategy):
    def findNextStop(self, floorNum):
        print(f"Applying Shortest Seek Algorithm and Moving elevator to floor {floorNum}")
        # returning 1 for demo purposes, should be determining next stop and returning that
        return 1
    

class IElevatorSelectionStrategy:
    @abstractmethod
    def selectElevator(extReq: ExternalRequest):
        pass

class OddEvenElevatorSelectionStrategy:
    def selectElevator(self, extReq: ExternalRequest):
        print("Selecting elevator according to odd-even strategy and returning elevator id: ")
        if extReq.getSrcFloor()&1: 
            return 1
        return 2
    
class ZoneElevatorSelectionStrategy:
    def selectElevator(self, extReq: ExternalRequest):
        # For demo purposes, always returning elevator id 3
        print("Selecting elevator according to zone strategy and returning elevator id 3")
        return 3