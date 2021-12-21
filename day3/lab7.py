# print the fractional part of a integer
import math 
a =float(input("Enter a positive integer "))
y,x = math.modf(a)
print (x)
print(y)