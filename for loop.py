

#reverse a number using for loop
num1=int(input("enter a number: "));
num=num1;
reverse="";
for a in range((len(str(num1)))):
    rem=num1%10;
    reverse+=str(rem);
    num1=num1//10;
print("the reverse of the numbr:",reverse);


