#Filename:scores_management.py

SS={}
def Submit():
	global SS
	while(True):
		print('Please enter the name(0 to quit):'),
		name = input()
		if name == '0':
			break
		print('Please enter the score:'),
		score = int(input())
		SS[name] = score

def Request():
	global SS
	while(True):
		print('Please enter the name you want to ask about(0 to quit)'),
		name = input()
		if name == '0':
			break
		print(SS.get(name,'not exist'))
		
def Delete():
	global SS
	while(True):
		print('Please enter the name you want to delete(0 to quit)'),
		name = input()
		if SS.get(name,False) == False:
			print('not exist')
			break
		del SS[name]

def Sort():
	print('This is the sorter list')
	temp = sorted(SS.items(), key=lambda e:e[1], reverse=True)
	for item in temp:
		print (item)

import pickle as p
f = open('scores.data', 'rb')
SS = p.load(f)
while(True):
	print('What do you want to do?\n1 -> submit\n2 -> request\n3 -> delete\n4 -> sort\n')
	a = input()
	if a == '1':
		Submit()
	elif a == '2':
		Request()
	elif a == '3':
		Delete()
	elif a == '4':
		Sort()
	else:
		break
f = open('scores.data', 'wb')
p.dump(SS, f)
f.close