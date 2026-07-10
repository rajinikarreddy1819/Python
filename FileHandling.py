"""

Open, read and Close File


# f = open("File_name", "Mode -> read, write, append")
# "r" --> open for reading(Def)
# "w" ---> open for writing, truncating the file fisrt
# "x"  --> create a new file and open it for writing
# "a" ---> open for writing, appending to the end of file if it exists
# "b" ----> binary mode
# "t" -----> text mode
# "+" -----> open a disk for updating (reading and writing)

"""
class FileHandling:
    def open_file(self, file):
        f = open(file, "r")
        data =  f.read()
        f.close()
        return data
    
    def reading_file(self,file):
        f = open(file, "r")
        line1 = f.readline() # reads one line at a time
        print(line1)

        line2= f.readline()
        print(line2)  
        f.close()

    def write_file(self, file):
        f = open(file, "w")
        f.write("I Want to learn Java")
        f.close()

    def appending_file(self,file):
        f = open(file, "a")
        f.write(" And also AI") 

     

f1 = FileHandling()
print(f1.open_file("File.txt") ) 
f1.reading_file("File.txt")
f1.write_file("File.txt")
print(f1.reading_file("File.txt") ) 
f1.appending_file("File.txt")
f1.reading_file("File.txt")

f2 = FileHandling()
f2.write_file("Sample.txt")

print("============================ WITH METHOD =====================")

with open("Sample.txt", "r") as f:
    data = f.read()
    print("With method "+ data)   



    



