number=eval(input('your number:'))
if number==987654:
    print('congrats')
if number!=98765:
    print('sorry')

n=98
if not n%2:
    print(n,'是偶数')
    
x=input('enter a string:')
if x:
    print('x是一个非空字符串')

number=eval(input('enter your number:'))
if number==987654:
    print('congrats')
else:
    print('oh no')
    
score=eval(input('enter your score:'))
if score<0 or score>100:
    print('your numner is wrong')
elif 0<=score<50:
    print('D') 
elif 50<=score<60:
    print('Pass') 
elif 60<=score<70:
    print('B') 
else:
    print('A')
    