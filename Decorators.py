class Decorators:
    @staticmethod
    def greatest_first(func):# 1. It will take sub , divide function as parameter Func. Func is # Decorator is used eliminate the duplicate of code 
        def wrap(a,b): 
            if a < b:
                a,b = b,a
            return func(a,b) # 3. Returns the same Function (Either divide or Sub Function)
        return wrap   # 2. Calls the wrap function by returning 

    @staticmethod
    @greatest_first
    def divide(a,b):
       # if a < b: # To divide greatest number with small value
         #   a,b = b,a
        return a/b
    @staticmethod
    @greatest_first
    def sub(a,b):
        #if a < b: # To Eliminate the Negative value
         #   a,b = b,a        
        return a - b;
""" METHOD 1 :"""
c = Decorators()
print(c.divide(3,4))
print(c.sub(3,4))

""" METHOD 2 : """
print("============================Method 2 =============================")
class Decorator:
    @staticmethod
    def greatest_first(func):# 1. It will take sub , divide function as parameter Func. Func is # Decorator is used eliminate the duplicate of code 
        def wrap(a,b): 
            if a < b:
                a,b = b,a
            return func(a,b) # 3. Returns the same Function (Either divide or Sub Function)
        return wrap   # 2. Calls the wrap function by returning 

    @staticmethod
    # @greatest_first
    def divide(a,b):
       # if a < b: # To divide greatest number with small value
         #   a,b = b,a
        return a/b
    @staticmethod
   # @greatest_first
    def sub(a,b):
        #if a < b: # To Eliminate the Negative value
         #   a,b = b,a        
        return a - b;

c = Decorator()
sub = c.greatest_first(c.sub)
result1 = sub(3,4)
print(result1)

divide = c.greatest_first(c.divide)
result2 = divide(3,4)
print(result2)



      
    