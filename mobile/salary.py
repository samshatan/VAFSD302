#write a program to calculate tye salary of an employe when a basic salary to be entered by the user as an input
#DA will be 45% of the basic salary 
#HRA will be the 10% if basic is less than 20000 and 15% if greater than and equal to 20000
#TA will be 5% if basic salary is less than and equal to 10000 and 10% if basic is greater than 10000 and less than and equal to 20000 and 20% ig greater than 20000
#TDS 10% if gross salary is less than equal to 20000 and 15% if gross salary is greater than 20000
b=int(input("Enter the basic salary"))
da=0.45*b
if(b<20000):
	hra=0.1*b
else:
	hra=0.15*b
if(b<=10000):
	ta=0.05*b
elif(b<=20000):
	ta=0.1*b
else:
	ta=0.2*b
gs=b+hra+ta+da
if(gs<=20000):
	tds=0.1*gs
else:
	tds=0.15*gs
sr=gs-tds
print(gs)
print(sr)