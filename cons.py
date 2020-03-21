class Calculator:
    def _init_(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
        
    def subtract(self):
        return self.a - self.b

def main():
    cal = Calculator(10,20)
    print(cal.add())
    print(cal.subtract())

main()