# #Write a Python program that accepts a string and calculate the number of digits and letter
# a = input ("enter a mixture of num and letters:\t")
# count_letter=0
# count_num = 0
# for let in str(a):
#         if  let=="a"or let=="b" or let =="c" or let =="d"or let =="e"or let=="f"or let =="g"or let =="h" or let=="i" or let=="j" or let=="k" or let=="l" or let =="m" or let=="n" or let=="o" or let=="p" or let=="q" or let=="r" or let=="s"  or let=="t" or let=="u" or let=="v" or let=="w" or let=="x"or let=="y"  or let=="z":
#     	    count_letter+=1
#         else:
#     	    count_num+=1
# print("Number of letter :",count_letter)
# print("Number of num :",count_num)



a=input("Input a string: ")
i=0
j=0
for k in a:
    if k.isdigit():
        i=i+1
    elif k.isalpha():
        j=j+1
    else:
        pass
print("Letters", j)
print("Digits", i)