def avg():
    a=eval(input("the marks of student splitted by comma(,): "))
    b=eval(input("the marks of student splitted by comma(,): "))
    c=eval(input("the marks of student splitted by comma(,): "))
    d=eval(input("the marks of student splitted by comma(,): "))
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    print(lst)
    for char in lst:
        s=0
        for marks in char:
            s =+ s+marks
        print(s/len(char))
            
