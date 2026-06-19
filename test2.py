num1=int(input("enter a number"));
def factorial(num1):
    fact=1
    for i in range(1,num1+1):
        fact=fact*i
    return fact

def strong(num1):
    sum=0
    for digit in str(num1):
        sum=sum+factorial(int(digit))
    if sum==num1:
        print("strong number");
    else:
        print("not an strong number");
strong(num1)