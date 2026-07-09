class Student:
   # name = "Rajinikar"
    College_name = "GCET" # Class Attribute (Same for All Instance/Objects)
    def __init__(self, fullname, marks): #Constructor
        print("In Constructor")
        self.name = fullname # Instance Attribute (Different for different Instance / Objects)
        self.marks = marks
   # def __init__(self, first, last):
   #     self.fullname = first + last

    def welcome(self):
        print("Welcome", self.name)

    def  getmarks(self):
        return self.marks



s1 = Student("Rajinikar", 96)
print(s1.name)
print(s1.College_name)
s1.welcome()
print(s1.getmarks())



s2 = Student("Rajini", 99)
print(s2.name)
print(s2.College_name)
s3 = s2
print(s2.name)


#s4 = Student("Rajinikar", "Reddy")
#print(s4.fullname)
print(s3)
print(type(s3))
print(s3.name)
#print(s1.name)    
#print(type(s1))
#print(s1)


