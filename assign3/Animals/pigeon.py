class Pigeon:
	def __init__(self,name):
		self.name=name
		self.db=self.cuckoo()


	class cuckoo:
		def __init__(self):
			self.dd="03"
			self.mm="09"
			self.yy="1989"
			

		def display(self):
			print('{}/{}/{} is your DOB'.format(self.dd,self.mm,self.yy))



pige=Pigeon("Arthur")
x=pige.db
x.display()
