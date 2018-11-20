lst=[]
a=input('enter first word of list: ')
lst.append(a)
b=input('the second word of list; ')
lst.append(b)
c=input('the third word of list: ')
lst.append(c)
d=input('the fourth word of list: ')
lst.append(d)
e=input('the fifth word of list: ')
lst.append(e)

print('this is the list: ',lst)
for x in lst:
    if x != 'secret':
        print(x)
        
             
             
