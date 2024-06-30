u1g=(input("Enter your fav game:"))
u1gr=float(input("enter your rating for that game:"))
u2g=(input("enter your fave game"))
u2gr=float(input("enter your rating for that game"))
if(u1g==u2g):
    if(u1gr==u2gr):
        print("Both have same taste")
    elif(u1gr!=u2gr):
        print("Both are choosen different game but same ratings")
elif(u1g!=u2g):
    if(u1gr!=u2gr):
        print("Both are choosen different game and different ratings")
