# grade calculator using marks a,b,c,d,fail
a=int(input("enter a grade marks"));

def grade_calculator(a):
   if a >60:
      print ("a grade");
   elif a<=60 and a>50:
      print ("b grade");
   elif a<=50 and a>40:
      print ("c grade");
   elif a<=40 and a>35:
      print ("d grade");
   else:
      print("fail")
   
grade_calculator(a)










