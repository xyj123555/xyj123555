lst=[]
for i in range(1,5):
    goods=input('enter the number and goods:')
    lst.append(goods)
for item in lst:
    print(item)
    
cart=[]
while True:
    flag=False
    num=input('enter the number you want to buy:')
    for item in lst:
        if num==item[0:4]:
            flag=True
            cart.append(item)
            print('have added to the cart')
            break
    if not flag and num!='q':
        print('not exist')
    if num== 'q':
        break
print('-'*50)
print('your chosen goods are:')
cart.reverse()
for item in cart:
    print(item)
    
            