#find the salary amount
b=int(input("enter the basic salary:"));
def salary_amount(b):
    totalsalary=(b+5000+3000)-(b*0.1)
    print("total salary:",totalsalary);

salary_amount(b)
