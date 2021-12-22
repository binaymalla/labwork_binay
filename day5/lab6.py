# Write a Python program to count the number of even and odd numbers from a series of numbers.
series = (1, 2, 3, 4, 5, 6, 7, 8,11,32,46,56,89,777,545,52,36,63,21, 9)
count_odd = 0
count_even = 0
for x in series:
        if  x % 2==0:
    	        count_even+=1
        else:
                count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)