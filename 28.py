a=int(input("enter the number you want square from 0 upto: "))
b=int(input("enter the number you wanna skip : "))
for char in range(a):
    if char != b:
        print(char**2)
