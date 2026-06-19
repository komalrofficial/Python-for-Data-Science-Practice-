ch=str(input("enter the alphabet is vowel)"));
if(ch=='a' or ch=='A'):
    print("the A is vowel");
elif(ch=='e'):
    print("the E is vowel");
elif(ch=='i'):
    print("the I is vowel");
elif(ch=='o' ):
    print("the O is vowel");
elif(ch=='u' ):
    print("the U is vowel");
else:   
      print("the alphabet is consonant");





num1=int(input("enter the leap year:"));
if num1 %4 ==0  and num1  %100 !=0 or num1 %400 ==0:
    print ("leap year:", num1);
else:
    print("not leap year:", num1);