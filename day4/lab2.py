# To sum three given integers if two or more values then 0
a = int(input ("enter 1st integer\t"))
b = int(input ("enter 2nd integer\t"))
c = int(input ("enter 3rd integer\t"))
if a!=b!=c:
    d = a+b+c
    print("the sum of the numbers are",d)
else:
    print("please Enter 3 different numbers")