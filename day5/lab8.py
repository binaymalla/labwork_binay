# Write a Python program to get the Fibonacci series between 0 to 50.Note : 
# The Fibonacci Sequence is the series of numbers :0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it

n1, n2 = 0, 1
terms = 0
print("Fibonacci sequence:")
while terms<10:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    terms+=1