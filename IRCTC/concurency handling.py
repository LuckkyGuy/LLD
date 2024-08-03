from threading import Thread, Lock
class Problem: 
    def __init__(self):
        self.seats = [0] * 10
        self.seats_lock = Lock()
    def bookSeat(self, seat_no, name):
        with self.seats_lock:
            if self.seats[seat_no] == 0:
                self.seats[seat_no] = seat_no + 1
                print(f"Seat is booked by {name}")
            else:
                print(f"Seat is already booked.")
problem = Problem()

t1 = Thread(target = problem.bookSeat, args=(2, "Keerti"))
t2 = Thread(target = problem.bookSeat, args=(2, "Yash"))
t3 = Thread(target = problem.bookSeat, args=(2, "Amit"))

t1.start()
t2.start()
t3.start()
            
t1.join()  
t2.join()  
t3.join()  
print(f"value of seat 2 is: {problem.seats[2]}")