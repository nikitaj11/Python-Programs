class calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def division(self,a,b):
        return a/b 
    def multiplication(self,a,b):
        return a*b 

def main():
    cal = calculator()
    print(cal.add(10,20))
    print(cal.subtract(20,10))
    print(cal.division(20,4))
    print(cal.multiplication(2,5))

