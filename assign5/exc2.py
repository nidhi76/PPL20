f=open('sample.txt','w')

try:
	print("Enter a which is less than 100 and b should be less 50")
	a=int(input("Enter first number:"))
	b=int(input("Enter second number:"))
	assert a<100 and b<50
	div=a/b
	f.write(div)

except ZeroDivisionError:
	print("Division is not possible")
except TypeError:
	print("Decimal answer aren't displayed")
except ValueError:
        print("Numbers with symbol like ^,! dont work")
except SyntaxError:
	print("Numbers with symbol like ^,! dont work")
except AssertionError:
	print("Follow the number range!!")
else:	
	print(div)
	
finally:	
	f.close()
