answer=input('请问喝酒了吗')
if answer=='yes':
    proof = eval(input('请输入酒精含量：'))
    if proof<20:
        print('不构成酒驾，一路平安')
    elif proof< 80:
        print ('已构成酒驾,不要开车')
    else:
        print('以达到醉驾标准，请不要开车')
else:
    print('可以离开')   
    

user_name=input('your user name:')
pwd=input('your password:')
if user_name=='xyj'  and pwd=='123456':
    print('correct')
else:
    print('not correct')
    
    
score=eval(input('your score:'))
if score<0 or score>100:
    print('invalid')
else:
    print('your score is',score)
    
    
score=input('your grade:')
match score:
    case 'A':
        print('distinction') 
    case 'B' :
        print('good')
    case 'C' :
        print('pass')