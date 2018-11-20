def rev_int(x):
    a=x//100
    b=(x-(a*100))//10
    c=(x-(a*100)-(b*10))
    return (c*100)+(b*10)+a
