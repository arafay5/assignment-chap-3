def points(x1,y1,x2,y2):
    import math
    if x2-x1==0:
        distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        print('the slope is infinty and the distance is',distance)
    else:
        slope=(y2-y1)/(x2-x1)
        distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        print("the slope is ",slope,"and the distance is",distance)
