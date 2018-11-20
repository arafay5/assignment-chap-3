def hit(x1,y1,r,x2,y2):
    d=((x2-x1)**2)+((y2-y1)**2)
    if d <= r**2:
        print('true')
    else:
        print('false')
