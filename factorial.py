num1=145
num=num1
s_num=0
while num1!=0:
    rem=num1%10
    num1=num1//10;
    fact=1
    for n in range(1,rem+1):
        fact=fact*n;
    s_num+=fact
if num==s_num:
    print("strong number");
else:
    print("not strong number");
