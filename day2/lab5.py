# A school decided to replace the desks in three classrooms.
# Each desk sits two students.Given the number of students in each class,
# print the smallest possible number of desks that can be purchased.
# The program should read three integers:
# the number of students in each of the threeclasses, a, b and c respectively.
# Suppose In the first test there are three groups.
# The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks are also enough for the third group of 22 students.
# So, we need 32 desks in total.

firstclass=int(input("Enter the number of students in first class: "))
secclass=int(input("Enter the number of students in second class: "))
thirdclass=int(input("Enter the number of students in third class: "))
if firstclass%2==0:
    bench1=firstclass/2
else:
    bench1=(firstclass+1)/2
if secclass%2==0:
    bench2=secclass/2
else:
    bench2=(secclass+1)/2
if thirdclass%2==0:
    bench3=thirdclass/2
else:
    bench3=(thirdclass+1)/2
totalbench=bench1+bench2+bench3
print(f"Number of bench in first class:\t",bench1)
print(f"Number of bench in second class:\t",bench2)
print(f"Number of bench in third class:\t",bench3)
print(f"Total no. of bench needed:\t",totalbench)