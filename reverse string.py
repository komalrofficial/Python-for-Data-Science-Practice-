#reverse the given string
str="computer"
print(str[::-1])

#aproach 2 positive indexing

reversestring="";
for s in range(1,len(str)+1):
    reversestring+=str[len(str)-s]
print(reversestring)   
 
#aproach 3 negative indexing
reversestring="";
for s in range(1,len(str)+1):
   reversestring+=str[-s]
print(reversestring)

#reverse individual string

str="Hey! i am software developer"
print(str[::-1])

strarray=str.split();
print(strarray)
reverse="";
for st in range(len(strarray)):
    word=strarray[st];
    print(word[::-1])
    reverse+=word[::-1] +""
print(reverse)

#aproach 3 positive indexing

reverse="";
for st in range(len(strarray)):
    word=strarray[st];
    print(word)
    rev=""
    for s in range(1,len(word)+1):
        rev+=word[len(word)-s]
    reverse+=rev+" "
    print(reverse)

#negative indexing
reverse="";
for st in range(len(strarray)):
    word=strarray[st];
    print(word)
    rev=""
    for s in range(1,len(word)+1):
        rev+=word[-s]
    reverse+=rev+" "
    print(reverse)

#count the vovel number
str="computer"
count=0;
for s in range (len(str)):
    ch=str[s].lower();
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count+=1;
print("the number of vowels:", count);
# f string
print(f"the number of vowels:",count);

#approach 1
count=0;
for s in range(len(str)):
    ch=str[s].lower();
    if ch in "aeiou":
      count +=1;
print("the number of vowels:",count)

#palindrome aproach 1
num1=int(input("enter a first number"));
num2=int(input("enter a second number"))
if num1==num2:
    print("the number is palindrome");
else:
    print("the number is not palindrome");

#approach 2
str="c"
    
#remove space
str="software developer"
print(str.split())


