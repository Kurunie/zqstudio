#Filename:scores_management.py
#超低配版成绩管理系统
SS={}
def isname(name):
    for i in name:
        if not (ord(i) >= 65 and ord(i) <= 90 or ord(i) >=97 and ord(i) <=122 or ord(i) == 32):
            return False
    return True
    
def isscore(score):
    for i in score:
        if not ord(i) >=48 and ord(i) <= 57:
            return False
    return True
    
def Submit():
    global SS
    while(True):
        name = input('Please enter the name(Enter to exit):\n')
        if len(name) == 0:
            break
        if not isname(name):
            print('Wrong Input')
            continue
        print('Please enter the score:'),
        score = input()
        if not isscore(score):
            print('Wrong Input')
            continue
        SS[name] = int(score)

def Request():
    global SS
    while(True):
        name = input('Please enter the name you want to ask about(Enter to exit):\n')
        if len(name) == 0:
            break
        if not isname(name):
            print('Wrong Input')
            continue
        print('%s\'s score is %s' % (name, SS.get(name,'not existing')))
        
def Delete():
    global SS
    while(True):
        name = input('Please enter the name you want to delete(Enter to exit):\n')
        if len(name) == 0:
            break
        if SS.get(name,False) == False:
            print('not exist')
            break
        del SS[name]

def Sort():
    sw = input('ordending -> 1\ndescending ->2\n')
    print('This is the sorted list')
    if sw == '1':
        temp = sorted(SS.items(), key=lambda e:e[1], reverse=False) #返回list
    elif sw == '2':
        temp = sorted(SS.items(), key=lambda e:e[1], reverse=True)
    else:
        print('Wrong Input')
    for item in temp:
        print (item)

import pickle as p
import os, sys
filename = os.path.dirname(os.path.abspath(sys.argv[0]))
filename = filename + '\scores.data'
#print (filename)
if not os.path.exists(filename):
    f = open(filename, 'wb')
    f = open(filename, 'rb')
else:
    f = open(filename, 'rb')
    try:                  #处理EOFError异常：文件为空时无法读入
        SS = p.load(f)
    except EOFError:
        pass  #不管

while(True):
	a = input('What do you want to do?\n1 -> submit\n2 -> request\n3 -> delete\n4 -> sort\n')
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
f = open(filename, 'wb')
p.dump(SS, f)
f.close()