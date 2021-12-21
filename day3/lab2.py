# Marks of 4 subjects and their total marks percentage and grade
M = int (input ("Enter your marks in maths"))
S = int (input ("Enter your marks in Science"))
C = int (input ("Enter your marks in computer"))
H = int (input ("Enter your marks in Health"))
total =M+S+C+H
p = (total/400)*100
if p >= 70 :
    print ("congrats you have secured distinction")
elif p>=60 and p<=70:
    print ("congrats you have secured first division")   
elif p>=40:
    print ("congrats you have passed") 
elif p<=40:
    print ("oops you have failed your exam ")