class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self, clutch, ace):
        self.clutch = clutch
        self.acc = ace
        if clutch and ace:
            print('Car Started .......') 
        else:
            print("Car Not Started .... Turn on the Clutch and Acce")  

c1 = Car()
c1.start(clutch=True,ace=True)  

c2 = Car()
c2.start(False, True)

