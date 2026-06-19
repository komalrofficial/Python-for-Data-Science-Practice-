#find the ADDITION of two numbers
def add(a,b):
    return a+b
ans=add(2,3);
print("addition is",ans);

#find the GREATEST of two numbers
 
def greatest(a,b):
    if a>b:
        return a
    else:
        return b
ans=greatest(5,10)
print("greatest is",ans)

#even or odd number
def even_odd(num):
    if num%2==0:
      return "Even"
    else:
      return "Odd"
ans=even_odd(8)
print("number is",ans)

#number positive or negative
def pos_neg(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
ans=pos_neg(8)
ans2=pos_neg(-5)
ans3=pos_neg(0)
print("number is",ans)
print("number is",ans2)
print("number is",ans3)

#check person eligibl to vote
# num=int(input("Enter the age of person: "))
def eligible_to_vote(age):
    if age>=18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
ans=eligible_to_vote(45)
print("person is",ans)
 #leap year or not

def leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return "Leap year"
    else:
        return "Not a leap year"
ans=leap_year(2020)
ans2=leap_year(1900)
print("year is",ans)
print("year is",ans2)

#check character is vowel or consonant
def vowel_consonant(char):
    if char in 'AEIOUaeiou':
        return "Vowel"
    else:
        return "Consonant"
ans=vowel_consonant('A')
ans2=vowel_consonant('b')
print("character a is",ans)
print("character b is",ans2)

#eligible for driving liscense
def eligible_for_driving_license(age):
    if age>=20:
        return "Eligible for driving license"
    else:
        return "Not eligible for driving license"
ans=eligible_for_driving_license(56)
print("person is",ans)

#find the greatest of 3 numbers
a=18
b=98
c=56



# def greatest_of_three(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# ans=greatest_of_three(a,b,c)
# print("greatest is",ans)

# #find the smallest of 3 numbers
# def smallest_of_three(a,b,c):
#     if a<b or a<c:
#         return a
#     elif b<a or b<c:
#         return b 
#     else:
#         return c
# ans=smallest_of_three(56,98,76)
# print("smallest_of_three:",ans)

# #check wether a number is divisible by 5 and 11

# num=int(input("enter a number",));
# def devisible(num):
#     if num %5==0 and num %11==0:
#         return "divisible"
#     else:
#         return "not divisible"
# ans=devisible(num)
# print("divisible",ans)


# #check number is multiple of 3 or 7
# num=int(input("enter a number"));
# def multiply_of(num):
#     if num%3==0 or num%7==0:
#         return"multiple"
#     else:
#         return"not multiple"
# ans=multiply_of(num)
# print("multiple or not multiple:",ans);

#check wether a number is zero ,positive or negative
  
num=int(input("enter a number"));
def zero_positive_negative(num):
    if num==0:
        return "zero number"
    elif num>0:
        return"positive number"
    else :
        return "negative number"
ans=zero_positive_negative(num);
print("zero_positive_negative:",ans);


#check wether a number is divisible by both 2 and 3

num=int(input("enter a number divisible by both 2 and 3:"));
def devisible(num):
    if num %2==0 and num %3==0:
        return "divisible"
    else:
        return "not divisible"
ans=devisible(num)
print("divisible by  both 2 and 3:",ans)
