#username and password.
usern=input("enter your username")
passw=input("enter your password")
for i in range(3):
    u_name=input("Please enter correct user name")
    pwd=input("Please enter correct password")
    if u_name== usern and pwd == passw:
        print("You are Logged in sucessfully")
        break
else:
    print("Attempts exceeded")