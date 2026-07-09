class Student:
    def __init__(self, name):
        self.name = name
        self.lap = self.Laptop("Hp", "4GB", "256GB")
    def show(self):
        print(self.name)

    class Laptop:
        def  __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        def show(self):
            print(self.brand)


s1 = Student("Rajinikar")
s1.show()
lap1 = s1.lap
print(lap1.brand)
print(lap1.show())


