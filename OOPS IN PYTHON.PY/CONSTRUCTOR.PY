#def__init__(self,variable list):

class Student:
    def __init__(self,name,age,dept,fees,course):
        self.name= name;
        self.age= age;
        self.dept= dept;
        self.fees= fees;
        self.course=course;
    def displaydetails(self):
        print(f"new student name is {self.name} {self.age} years old taken admission in {self.course} in {self.dept} and offered fees is rs.{self.fees}")
stu=Student("komal shnde","31","IT","60000","DATA SCIENCE");
stu2=Student("minal rawde","27","computer science","50000","marn") 
stu.displaydetails();
stu2.displaydetails();

#9 CREATE A COURSE CLASS WITH COURSE NAME AND duration 
class Course:
    def __init__(self,name,duration):
        self.name= name;
        self.duration=duration;
    def displaycourse(self):
        print(f"course name is{self.name} his duration is{self.duration}")
stu=Course("electrical engineering","4years");
stu.displaycourse();

#10 create a school class wth school details
class School:
    def __init__(self,name,establish_yaer,board,principal,no_of_student):
        self.name=name;
        self.establish_yaer=establish_yaer;
        self.board=board;
        self.principal=principal;
        self.no_of_student=no_of_student;
    def display_school_details(self):
        print(f"school name {self.name} establishment year {self.establish_yaer} in {self.board} principal name is {self.principal} and total no of student{self.no_of_student}")    
stu=School("new apostolic","1965","CBSE","WANDANA","8000");
stu.display_school_details();

#8 create a hospital class and store doctor information 
class Doctor:
    def __init__(self,name,reg_no,speciality,adress,timing):
        self.name=name;
        self.reg_no=reg_no;
        self.speciality=speciality;
        self.adress=adress;
        self.timing=timing;
    def display_doctor_details(self):
        print(f"doctor name is { self.name } his registration number is  {self.reg_no} his speciality in  {self.speciality} adress is {self.adress} and timing is {self.timing}");
stu=Doctor("Anjali Powar","15467899","IVF","Bajaj nagar" ,"11am to 6pm")  
stu.display_doctor_details() ; 

#3 create product class and product  name and price details
class Product:
    def __init__(self,name,price):
        self.name=name;
        self.price=price;
    def display_product_detais(self):
        print(f"Product name is {self.name} and its price is {self.price}")
stu=Product("Lakme 9 to 5 ","499")
stu.display_product_detais();

#4 create  rectangle class with length and breadth

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length;
        self .breadth=breadth;
    def display_rectangle(self):
        print(F"Rectangle length is {self.length} and is breadth is {self.breadth}")
stu=Rectangle("46cm" , "22cm");
stu.display_rectangle();

#5 create acircle class with radius

class Circle:
    def __init__(self,daimeter,radius):
        self.daimeter=daimeter;
        self.radius=radius;
    def display_circle(self):
        print(f"circle daimeter is {self.daimeter} and its radius is {self.radius}")
stu=Circle("50cm" ,"25cm ");
stu.display_circle();

#6 create a vehicle class with brand and model

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand;
        self.model=model;
    def display_vehicle(self):
        print(f"Vehicle brand is {self.brand} and its model is {self.model}")
veh=Vehicle("Toyota", "Fortuner")
veh.display_vehicle()

#7 CREATE A CUSTOMER CLASS AND INITILIZE CUSTOMER DETAILS

class Customer:
    def __init__(self,name,id,email,balance):
        self.name=name;
        self.id=id;
        self.email=email;
        self.balance=balance;
    def display_customer_details(self):
        print(f"Customer name is {self.name} his id is {self.id}  and its email is {self.email} remaining balance is {self.balance}")
cuv=Customer("Amit Rangari ", "1987654","amit@gmail.com","50000");
cuv.display_customer_details();

#create a class calculatorusing add,subtract,divide

# class Calculator:

#     def __init__(self,add,subtract,multiply,divide):
#         num1=10
#         num2=20
#     def add num1 add num2        