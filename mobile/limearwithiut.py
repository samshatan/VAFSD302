a=[10,48,73,47,56,25]
t=int(input("Enter the number u want to search:-"))
f= False
for i in range(len(a)):
	if a[i]==t:
		print("Target",t," found at ",i+1)
		f=True
		break
if f==False:
	print("value not find")
print(type(a))