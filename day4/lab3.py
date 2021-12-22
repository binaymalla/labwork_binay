a =int(input("enter your age\t"))
g=input ("enter your gender(M/F)\t")
if g == "F"or (g=="M" and (a>40 and a<60)):
    print("You can work only in urban areas")
elif g == "M" and (a > 20 and a<40):
    print("You can work anywhere")
elif g !="M" or g!="F":
    print("Please enter only M or F")
else:
    print ("Error")