class Student:
   name="komal"        #ATTRIBUTES OR VARIABLES
   dept="IT"
   #METHOD
   def display_name(self):     #METHODS ,CLASS
        print("student name is",self.name);

#CREATE OBJECT
stu=Student();
stu.name="komal shende"
stu.display_name()                         
stu2=Student();
stu.name="pavani"
stu.display_name(); 
print(stu.name);
print(stu2.name);    



#CONSTRUCTOR METHOD
class Stuent1:
    # Constructor Method
    def __init__(self,name,dept):
        self.name=name;
        self.dept=dept;
    
    # Method
    def display_name(self):
        print("student Name is",self.name);


stu=Stuent1("abcd","ITI");
stu2=Stuent1("sdfg","IIT");
stu.display_name();
stu2.display_name();

#CREATE A CLASS STUDENT WITH ATTRIBUTES NAME AND AGE CREATE AN OBJECT AND DISPLAY THE DETAILS

class Student:
    name="minal"
    age="27"
    def display_name(self):
        print("student name is",self.name);
    def display_age(self):
        print("Her age is ", self.age)

stu=Student();
stu.name="minal"
stu.display_name()                         
stu2=Student();
stu.age="27"
stu.display_age(); 
print(stu.name);
print(stu2.age);

#2create a class employee with attributes id,name,and salary.

class employee:
    id="708965"
    name="AMIT"
    salary="50000"
    def display_id(self):
        print("employee id is",self.id);
    def display_name(self):
        print("His name is ", self.name)
    def display_salary(self):
        print("His salary is ", self.salary)


emp=employee();
emp.id="708965"
emp.display_id(); 
emp1=employee();
emp.name="amit"
emp.display_name()                         
emp2=employee();
emp.salary="50000"
emp.display_salary(); 
print(emp.id);
print(emp1.name);    
print(emp2.salary); 

#4  create a class book with atributes tittle and author.
class Book:
    tittle="electrical engineering"
    author="j.b.gupta"
    def display_tittle(self):
        print("book tittle is",self.tittle);
    def display_author(self):
        print("book author is ", self.author)
b=Book();
b.tittle="electrical engineering"
b.display_tittle();
b1=Book();
b.author="j.b.gupta"
b.display_author();

#6 create class person and store name and city

class person:
    storeName="aditya collection"
    city="nagpur"
    def display_storeName(self):
        print("person store Name is",self.storeName);
    def display_city(self):
        print("person from ", self.city)
per=person();
per.storeName="aditya collection"
per.display_storeName();
per1=person();
per.city="nagpur"
per.display_city();

#10 create a class bank with bank name and branch

class Bank:
    bankname="HDFC bank"
    branch="nagpur"
    def display_bankName(self):
        print("bankname is",self.bankname);
    def display_branch(self):
        print("branch name is", self.branch)
b=Bank();
b.bankname="HDFC bank"
b.display_bankName()
b.branch="nagpur"
b.display_branch();

# #17 create a calculator class with add ,subtract,multiply,and divide methods

# class Calculator:
#     def 


#create a car class with a method to start the car

class Car:
    def car_stsrted_method(self):
        print("car is started")

    