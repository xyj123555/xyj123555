lst=[88,89,90,98,00,99]
print(lst)
for index in range(len(lst)):
    if str(lst[index])!='0':
        lst[index]='19'+str(lst[index])
    else:
        lst[index]='200'+str(lst[index])
print(lst)

lst=[88,89,90,98,00,99]
for index,value in enumerate(lst):
    if str(value)!='0':
        lst[index]='19'+str(value)
    else:
        lst[index]='200'+str(value)
print(lst)