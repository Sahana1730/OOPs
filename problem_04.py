from random import randint

class Train:
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no {self.trainno} is running on time")

    def getfares(self, fro, to):
        fare = randint(300, 800)
        print(f"Ticket fare from {fro} to {to} in train no {self.trainno} is ₹{fare}")


# creating object (IMPORTANT: pass train number)
t = Train(17830)

t.book("Belgavi", "Bangalore")
t.getstatus()
t.getfares("Belgavi", "Bangalore")
