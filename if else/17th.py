x="admin"
y="1234"
print("the username is",x,"\nand the password",y)
name=input("enter username: ")
pas=input("enter password: ")
if x==name:
    if y==pas:
        print("Your successfully logged in")
else:
    print("your username or the password is incorrect")