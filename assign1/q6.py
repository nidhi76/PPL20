

def sum(x): 
	sum = 1
	for i in range(2, x): 
		if x % i == 0: 
			sum += i
	return sum 
	

 
def ami(a,b):  
	if sum(a) == b and sum(b) == a: 
		print(a,b)
	



if __name__ == "__main__": 
	arr=[220, 17296, 18416, 63020, 76084,66928, 66992, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595] 
	
	
	for k in range(0, len(arr)): 
		for j in range(0, len(arr)): 
			ami(arr[k], arr[j])





