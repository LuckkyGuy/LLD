import sys, os
sys.path.append(os.path.dirname(__file__))

from IRCTCSystem import IRCTCSystem, Train, Compartment, Seat
from Bookinghelper import BookingRequest

def main():
    system = IRCTCSystem()
    bookingRequest = BookingRequest("Delhi", "BLR", "3PM", "5 Aug 2024", "1000")
    system.do_booking(bookingRequest)

    # admin
    print("----------------------")
    
    system.onboard_train()


    
if __name__ == '__main__':
    main()
    