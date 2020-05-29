def gm(a,r,n) :
	for i in range(0,n):
		print (a*pow(r,i))
if __name__ == "__main__": 
	a=int(input("Enter value for a:"))
	r=int(input("Enter value for r:"))
	n=10
	gm(a,r,n)
