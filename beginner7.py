i=0
while i<3:
    user_name=input('your user name:')
    pwd=input('your password:')
    
    if user_name=='xyj' and pwd=='888888':
        print('正在登录')
        i=8
    else:
        if i < 2:
            print('用户名或密码不正确, 您还有',2-i,'次机会')
        i+=1
if i==3:
    print('三次均错误')
    
for i in range(1,4):
    for j in range (1,5):
        print('*',end = '')
    print()
    
for i in range (1,6):
    for j in range (1, i+1):
        print('*',end='')
    print()
    
for i in range (1,6):
    for j in range (1,7-i):
        print('*',end='')
    print()
    
for i in range(1,6):
    for j in range (6-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()