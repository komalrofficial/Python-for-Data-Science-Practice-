num = int(input("Enter a number: "));
reverse = "";
while num!=0:
    rem = num % 10;
    if rem % 2 != 0:
        rem = rem * 2;
    
    reverse += str(rem); 
    num = num // 10;
# print(reverse);
finalreverse="";
num = int(reverse);
while num!=0:
    rem = num % 10;
    if rem % 2 != 0:
        rem = rem * 2;
    
    finalreverse += str(rem); 
    num = num // 10;

print(finalreverse);


 
f1=1
f2=2
num1=int(input("enter fibonacci number: "));
print(f1,f2);
for i in range(num1):
    f3=f1+f2;
    swap=f1;
    f1=f2;
    f2=f3;
    print(f3);