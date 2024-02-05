for i in 'hello':
    print('i')
for i in 'hello':
    print(i)
    
for i in range(1,11):
    print(i)
    
s=0
for i in range(1,11):
    s+=i
print(s)

for i in range(100,1000):
    sd=i%10
    tens=i//10%10
    hundred=i//100
    if sd**3+tens**3+hundred**3==i:
        print(i)
        
s=0
for i in range(1,11):
    s+=i
else:
    print('1-10的累加为',s)
    
answer=input('今天要上课吗?y/n')
while answer == 'y':
    print('好好学习，天天向上')

s=0
i=1
while i<=100:
    s+=i
    i+=1
print('和为',s)

