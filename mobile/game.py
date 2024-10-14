import random
def player(g):
	a=int(input("Guess a number:- "))
	b=int(input('Guess another number:-'))
	c=int(input('Guess third number:-'))
	if(a==g):
		print('Player one guess is right')
	elif(b==g):
		print('Player second guess is right')
	elif(c==g):
		print('Player third guess is right')
	else:
		print('Guess again')
		print('Compiler number is',g)
s=int(input('For starting the game press 1'))
z=int(input("Enter the number of time u want to play this game"))
for i in range(z):
	if(s==1):
		g=random.randint(0,9)
		player(g)