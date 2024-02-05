d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)

lst1=[10,20,30,40]
lst2=['cat','dog','pet,','zoo']
zipobj=zip(lst1,lst2)
print(zipobj)
d=dict(zipobj)
print(d)

d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t:10})

print('max:',max(d))

del d 


d={'hello':10,'world':20,'python':30}
print(d['hello'])
print(d.get('hello'))

for item in d.items():
    print(item)
    

for key,value in d.items():
    print(key,value)
    
d={100:'x',200:'y',300:'z'}
print(d)

d[400]='a'
print(d)

keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)

lst=list(d.items())
print(lst)

print(d.pop(100))

d.clear()
print(d)

import random
d={item:random.randint(1,100) for item in range (4)}
print(d)

lst=[100,200,300]
lst2=['x','y','z']
d={key:value for key,value in zip(lst,lst2)}
print(d)