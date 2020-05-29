#Creating a file called myfile.txt
f=open('myfile.txt ','w')
str="This is a sample test text. Regarding python exceptions"

f.write(str)

#ask the user to input a file name
try:
	name=input("Enter filename")
	f=open(name,'r')

except IOError:
	print("File not found ")
else:
	strr=f.read()
	print(strr)	
f.close()
