import random
target_num,guess_num=random.randint(1,10),0
while target_num!=guess_num:
    if target_num>guess_num:
        guess_num =int(input("Higher:"))
    else:
        guess_num = int(input("Lower:"))
print ("well guessed")