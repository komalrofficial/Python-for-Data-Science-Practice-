#print only odd number in a list
#num=int(input("enter a number from 1 to 100:"));
for i  in range(1,100):
    if i==50:
        break;
    print(i); 
#print number skip multipleof 3

for i in range(1,50):
    if i%3==0:
        continue;
    print(i); 
#skip vowels from string

str="electrical engineering";
for i in str:
    if i in 'aeiouAEIOU':
        continue;
    print(i);

#pass ststement

num=[85,34,76,20,90,45]
for i in range(len(num)):
    if num[i]>35:
       print("passed",num[i]);
    else:
        continue;



#stop when user enter zero value
# num=int(input("enter a number:",));
# while num!=0:
#     print("entered num:", num);
#     num=int(input("enter a number:",));
# print("you entered zero value, program stoped");


num=int(input("enter a number:",));
while num!=0:
    if num>0:
        square=num*num;
        print("square of the number is:",square);
    elif num==-1:
        print("Program End!");
        break;
    else: 
        print("Skipped!");
    num=int(input("enter a number:",));