#实例1
class Person():
    def __init__(self,weight):
        self.weight=weight;
    def eat(self,food):
        self.weight+=food;
    def exercise(self):
        self.weight-=0.5
lilei=Person(80)
print(lilei.weight)
lilei.eat(1)
print(lilei.weight)
lilei.exercise()
print(lilei.weight)
#实例2
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        area=3.1415926*(self.radius**2)
        return area
    def get_circumference(self):
        circumference=2*3.1415926*self.radius
        return circumference
c1=Circle(5)
print(c1.radius)
print(c1.get_area())
print(c1.get_circumference())
c2=Circle(10)
total_area=c1.get_area()+c2.get_area()
print(total_area)
#实例3
class BankAccount():
    def __init__(self):
        self.balance=0
    def deposit(self,money):
        self.balance+=money
    def withdraw(self,money):
        if money<=self.balance:
            self.balance-=money
        return self.balance
lilei_bank_account=BankAccount()
print(lilei_bank_account.balance)
lilei_bank_account.deposit(100)
print(lilei_bank_account.balance)
print(lilei_bank_account.withdraw(101))

