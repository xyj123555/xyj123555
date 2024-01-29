s='3.14+3'
print(s,type(s))
x=eval(s)
print(x,type(x))

age=eval(input('your age:'))
print(age,type(age))

print(1+1)
print(1-1)
print(1*1)
print(10/2)
print(10//3)
print(2**4)

x=20
y=10
x=x+y
print(x)
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)

a,b=10,20
print(a,b)
a,b=b,a
print(a,b)

print(19<10)
print(19>10)
print(19==10)
print(19!=10)

print(8>7 and 6>5)
print(8>7 and 6<5)
print( not (8>7))