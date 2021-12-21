#Find the sum of digits of a num.
num = int(input("Enter a number"))
sumofdigits = 0
for digit in str(num):
    sumofdigits += int(digit)
print(sumofdigits)