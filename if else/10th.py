x=int(input("Enter first number: "))
y=int(input("Enter Second number: "))
z=(input("Enter a arithmetic operations +,-,*,/ : "))
if z=="+":
    print("Addtion of two numbers is:",x+y)
elif z=="-":
    print("Subtraction of two number:",x-y)
elif z=="/":
    print("Division of two number is:",x/y)
else:
    print("Multiplication of two number is ",x*y)