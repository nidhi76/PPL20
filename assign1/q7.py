def arm(a):
	arms="This is Armstrong number {}"
	b=a
	sum=0
	
	while a>0:
		dig=a%10
		sum+=pow(dig,3)
		a//=10
	if b==sum:
		print(arms.format(b))
if __name__ == "__main__": 
	for i in range(1,1000):
		arm(i)

		       
