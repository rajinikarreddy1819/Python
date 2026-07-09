class Student:
    college = "GCET"
    def __init__(self, first, last):
        self.fullname = first + last
    @staticmethod    
    def get_Details(marks):
        sum=0
        for i in marks:
            sum += i
        if sum >= 60:
            return "PASS"
        else:
            return "Fail"
s1 = Student("Rajinikar", "Reddy")
print(s1.fullname + " : " + s1.get_Details([30,30,40]))        