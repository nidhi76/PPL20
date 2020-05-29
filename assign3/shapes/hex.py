import turtle
polygon=turtle.Turtle()



class Hex:
	
	def __init__(self):
		self.num_sides = 6
		self.side_length = 70
		self.angle = 360.0 / self.num_sides

	def get_side(self):

		side_length=int(input("Enter new side"))
		return side_length 
				
			
		
		
		  
	
	def draw(self):
		for i in range(self.num_sides): 
			polygon.forward(self.side_length) 
			polygon.right(self.angle) 
		

h=Hex()
h.draw()
h.get_side()

