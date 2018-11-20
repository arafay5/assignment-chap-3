print('Practice Problem 3.40')
def partition(names):
    return[firstname for firstname in names
           if firstname[0].lower() in 'abcdefghijklm']

x = partition(['Ron','Harry','Zack','Max','Abdullah'])
x.sort()
print(*x,sep = '\n')
