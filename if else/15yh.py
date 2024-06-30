x=int(input("enter first number:"))
y=int(input("enter second number: "))
z=int(input("enter third number: "))
if x>y:
    if x>z:
        print("x is greatest")
elif y>x:
    if y>z:
        print("y is greatest")
elif z>x:
    if z>y:
        print("z is greatest")