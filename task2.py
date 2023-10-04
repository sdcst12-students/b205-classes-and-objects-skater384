#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0
    
    def __init__(self,P=0,r=0,n=0):
        #more input parameters needed
        self.principal = P
        self.rate = r
        self.nPeriods = n
        
        return

    def interest(self,t,):
        
        return round((self.principal*(   (1+self.rate/100/self.nPeriods)**(self.nPeriods*t) ))-self.principal,2)
        
    def amount(self,t):
        return round((self.principal*(   (1+self.rate/100/self.nPeriods)**(self.nPeriods*t) )),2)

a = Calc(P=1000,r=4,n=2)
print(a.interest(3))
print(a.amount(5))
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

