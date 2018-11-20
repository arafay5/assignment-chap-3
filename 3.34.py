def pay(hourlywage,hours):
    if hours <= 40:
        sum=hourlywage*hours
    else:
        sum=40*hourlywage
        sum += (hours-40)*(hourlywage*1.5)
    return sum






































    
