import turtle
skk=turtle.Turtle()
class square:
	def __init__(self):
		self.length=50
		self.breadth=90
		self.area=self.length*self.breadth
		self.peri=2*(self.length+self.breadth)
	def get_area_peri (self):
		print( "Area is : " +" "+ str(self.area))
		print("Perimeter is : " + " "+ str(self.peri))
		
	def set_area_peri(self):
		self.length=int(input("Enter length:"))
		self.breadth=int(input("Enter breadth:"))
		self.area=self.length*self.breadth
		self.peri=2*(self.length+self.breadth)
	
	def draw(self):
		for i in range(4): 
    			skk.forward(self.length) 
    			skk.right(self.breadth) 
      
		turtle.done() 

c=square()
c.draw()
c.get_area_peri()
c.set_area_peri()
c.get_area_peri()
		
