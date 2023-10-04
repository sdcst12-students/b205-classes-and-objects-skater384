"""
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.
"""

class rectPrism:
    length = 0
    width = 0
    height = 0
    def __init__(self,h,l,w):
        # note you will need to specify more input parameters
        self.height = h
        self.length = l
        self.width = w

        pass

    def volume(self):
        
        return self.height*self.length*self.width
    
    def surfaceArea(self):
        return ((self.length*self.height)+(self.length*self.width)+(self.width*self.height))*2

# class instances and assertions below:

a = rectPrism(l=10,w=2,h=5)
a.height
assert a.volume() == 100
assert a.surfaceArea() == 160

b = rectPrism(l=1,w=1,h=1)
b.height
assert b.volume() == 1
assert b.surfaceArea == 6

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None