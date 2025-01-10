import sys, os
import random
sys.path.append(os.path.dirname(__file__))

from Bookinghelper import BookingRequest

class IRCTCSystem:
    def __init__(self):
        pass

    def do_booking(self, bookingRequest : BookingRequest):
        booking_processor = BookingProcessor.getInstance()
        booking_processor.process_booking(bookingRequest)

    def onboard_train(self):
        trainMgr = TrainMgr.getInstance()
        seatCount = int(input("How many seats in compartment?"))
        compartmentCnt = int(input("How many compartment in train?"))
        trainName = input("what is the train Name?")
        trainMgr.do_onboard(trainName, compartmentCnt, seatCount)


class BookingProcessor:
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not BookingProcessor.__shared_instance:
            BookingProcessor()
        return BookingProcessor.__shared_instance
    
    def __init__(self):
        if BookingProcessor.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            BookingProcessor.__shared_instance = self
            self.seatSelectionStrategy : ISeatSelectionStrategy = slidingWindowSeatSelectionStrategy()

    def process_booking(self, bookingRequest : BookingRequest):
        seatId = self.seatSelectionStrategy.selectSeat()
        book = Booking(bookingRequest, seatId)
        bookingMgr = BookingMgr.getInstance()
        bookingMgr.streBooking(book.ticketId, book)
        print(book)
        return
    


class BookingMgr:
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not BookingMgr.__shared_instance:
            BookingMgr()
        return BookingMgr.__shared_instance
    
    def __init__(self):
        if BookingMgr.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            BookingMgr.__shared_instance = self
            self.__bookings = dict()
    
    def getBooking(self, bookingId):
        if bookingId in self.__bookings:
            return self.__bookings[bookingId]
        return "invalid Booking Id."
    
    def streBooking(self, bookingId, bookObj):
        self.__bookings[bookingId] = bookObj


class Booking:
    def __init__(self, bookingRequest : BookingRequest, seatId):
        self.src = bookingRequest.src
        self.dest = bookingRequest.dest
        self.time = bookingRequest.time
        self.ticketId = random.randint(1,1000)
        self.amount = bookingRequest.amount
        self.seatId = seatId
    def __str__(self):
        return f"Ticket booked from {self.src} to {self.dest}, timing: {self.time}, amount: {self.amount}"
    

class ISeatSelectionStrategy:
    @staticmethod
    def selectSeat():
        pass

class slidingWindowSeatSelectionStrategy(ISeatSelectionStrategy):
    def selectSeat(self):
        print("selecting seat using slidingWindowSeatSelectionStrategy.")
        return 123

class fixSizeWindowSeatSelectionStrategy(ISeatSelectionStrategy):
    def selectSeat(self):
        print("selecting seat using fixSizeWindowSeatSelectionStrategy.")
        return 456

class TrainMgr:
    __shared_instance = None

    @staticmethod
    def getInstance():
        if not TrainMgr.__shared_instance:
            TrainMgr()
        return TrainMgr.__shared_instance
    
    def __init__(self):
        if TrainMgr.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            TrainMgr.__shared_instance = self
            self.trains = dict()
            self.trainId = 0

    def do_onboard(self, trainName, compartmentCount, SeatCount):
        # create seats for comparements
        self.seats = dict()
        self.compartments = dict()
        for i in range(SeatCount):
            seatId = "seatId" + str(i)
            self.seats[seatId] = Seat(seatId)
        
        # create comparements for train
        for i in range(compartmentCount):
            compartmentId = "compartmentId" + str(i)
            self.compartments[compartmentId] = Compartment(compartmentId, self.seats)
        
        self.trainId += 1
        self.trains[self.trainId] =  Train(self.trainId, trainName, self.compartments)
        print("Successful onboarded new train.")
        
        return self.trains[self.trainId]

class Seat:
    def __init__(self, seatId):
        self.seatId = seatId
        
class Compartment:
    def __init__(self, compartmentId, seats):
        self.compartmentId = compartmentId
        self.seats = seats

    def setSeat(self, seatId, seat: Seat):
        self.seats[seatId] = seat
    
    def getSeat(self, seatId):
        return self.seats[seatId]

class Train:
    def __init__(self, trainId, name, compartments):
        self.trainId = trainId
        self.name = name
        self.compartments = compartments
    
    def setCompartment(self, compartmentId, compartment: Compartment):
        self.Compartments[compartmentId] = compartment
    
    def getCompartment(self, compartmentId):
        return self.Compartments[compartmentId]