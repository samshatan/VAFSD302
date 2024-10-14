a=int(input("Enter first subject:- "))
b=int(input("Enter second subject:- "))
c=int(input("Enter third subject:- "))
d=int(input("Enter fourth subject:- "))
e=int(input("Enter fifth subject:- "))
av=(a+b+c+d+e)/5
if(av>=90):
	print("A")
elif(av>=80):
	print("B")
elif(av>=70):
	print("C")
elif(av>=60):
	print("D")
else:
	print("Fail")