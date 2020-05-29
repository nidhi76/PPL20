from inht import Bird

class Young(Bird):
	def flight_range(self,rnge):
		self.rnge=rnge

	def ret_range(self):
		return self.rnge


y=Young();
y.setnm("Sanjeev")
y.flight_range(23)
print("The little bird can fly {} km ".format(y.ret_range()))
print(y.ret_nm())
