def linear(a,t):
	for i in range(len(a)):
		if a[i] == t:
			return i
	return -1
a=[5,8,12,20,35]
t=12
r=linear(a,t)
if(r!=-1):
	print("found the target at ",r)
else:
	print("not found")