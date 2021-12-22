a = int(input ("Enter total num of class held\t"))
b = int(input ("enter total num of classes attended\t"))
per = (b/a)*100
print (per)
if per < 75:
    print ("you are not allowed to attend the exam")
else:
    print ("You are allowed to sit in exam")