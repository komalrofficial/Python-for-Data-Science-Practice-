# Take number from user and reverse it
num1=int(input("Enter a number to reverse:"))
num=num1;
# Perform loop to reverse the number
reverse = "";
while num1 != 0:
    rem = num1%10; # it will return remainder 
    reverse += str(rem);
    num1 = num1//10; # it will return quotient 
print("The reverse of the number is: ", reverse);

if int(reverse) == int(num):
    print("The number is a palindrome.");
else:
    print("The number is not a palindrome.");