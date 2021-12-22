# to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
a = int(input ("Enter a num betweeen 1500 and 2700:\t"))
if a>= 1500 and a<= 2700:
    if a%7==0 and a%5==0:
        print ("divisible by 5 and 7")
    else:
        print ("not")
else:
    print ("please enter num between 1500 and 2700:\t")