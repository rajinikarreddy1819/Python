class ExceptionHandling:
    def div(self, a, b):
        try:
            return a/b
        except  Exception as e:
            print(e)
        else:
            print("Good to Go") 

        finally:
            print("I WILL EXECUTE IF EXCEPTION IS OCCURED OR NOT, I USED FOR RESOURCE CLOSING")       
e1 = ExceptionHandling()
print(e1.div(2,4))
print(e1.div(4,0))            


 