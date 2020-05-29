import math
class Geometry(): 
 
    def __init__(self, x = 0.0, y = 0.0): 
        self.x = x 
        self.y = y 
 
    def computeArea(self): 
        pass
 
    def computePerimeter(self): 
        pass
 
    def move(self, deltaX, deltaY): 
        self.x += deltaX 
        self.y += deltaY 
 
    def __str__(self): 
        return 'Abstract class Geometry should not be instantiated and derived classes should override this method!'

class Circle(Geometry): 
 
    def __init__(self, x = 0.0, y = 0.0, radius = 1.0): 
        super(Circle,self).__init__(x,y) 
        self.radius = radius 
 
    def computeArea(self): 
        return math.pi * self.radius ** 2
 
    def computePerimeter (self): 
        return 2 * math.pi * self.radius 
 
    def __str__(self): 
        return 'Circle with coordinates {0}, {1} and radius {2}'.format(self.x, self.y, self.radius) 

class Rectangle(Geometry): 
 
    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0): 
        super(Rectangle, self).__init__(x,y) 
        self.width = width 
        self.height = height 
 
    def computeArea(self): 
        return self.width * self.height 
 
    def computePerimeter (self): 
        return 2 * (self.width + self.height) 
 
    def __str__(self): 
        return 'Rectangle with coordinates {0}, {1}, width {2} and height {3}'.format(self.x, self.y, self.width, self.height ) 
 
rectangle1 = Rectangle(15,20,4,5) 
print(rectangle1.computeArea()) 
print(rectangle1.computePerimeter()) 
rectangle1.move(2,2) 
print(rectangle1)
 
circle1 = Circle(10, 10, 10) 
print(circle1.computeArea()) 
print(circle1.computePerimeter()) 
circle1.move(2,2) 
print(circle1)
