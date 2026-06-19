#base and exponent
x=int(input("enter the base value"));
y=int(input("enter the power value"));
pow=1;
for a in range(1,y):
    pow=pow*x
    print("the power of given exponent:",pow);
