n=eval(input('enter an integer: '))
a=(n//1000)
print(a)
b=((n-1000)//100)
print(b)
c=(n-((b*100)+1000))//10
print(c)
d= (n-((b*100)+(c*10)+1000))
print(d)
