listold=eval(raw_input("enter the list"))
listnew=[]
i=0
val=0
#loop for the total numbers 
for i in range(1,26):
       val=0
#loop for each element
       for j in listold:
                  if(i==j):
                       val=1
                       break
       if(val==0):
                  listnew.append(i)
       i=i+1
print(listnew)
print("are missing page numbers") 
