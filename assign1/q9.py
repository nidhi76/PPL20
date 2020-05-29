import math
def fac(c) :
	
	oren="This is a ore number {}"
	oren1="This isnt a ore number {} "
	arr = []
	y=0
	den=0
	for i in range(1,c+1):
		if c%i==0:
			arr.insert(i-1,i)
			y+=1		
	for i in range(0,y):
		den+=c/arr[i]
	
	den=den/c
	hm=y/den
       
	if hm-int(hm)==0:
		print(oren.format(c))

	#else:
	#	print(oren1.format(c))
if __name__ == "__main__": 
	for g in range(1,6500):
		fac(g)
