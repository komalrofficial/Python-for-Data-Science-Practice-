# parent class / main class.
class Teacher:
    def __init__(self,name,age,dept,payment,course):
        self.name=name;
        self.age=age;
        self.dept=dept;
        self.payment=payment;
        self.course=course;
    def displayteacherdetails(self):
        print(f"teacher name is{self.name} she is {self.age} years old and speciality in a{self.course}in {self.dept}and offered salary in rs{self.payment}")
    
#child class /sub class

class student(Teacher):
    def __init__(self,stu_name,stu_age,fees,selected_course,name,age,dept,payment,course):
        super().__init__(name,age,dept,payment,course);
        self.stu_name=stu_name;
        self.stu_age=stu_age;
        self.fees=fees;
        self.selected_course=selected_course;
    def displaystudentdetails(self):
        print(f"New student name is {self.stu_name}{self.stu_age}years old taken admission in{self.selected_course} and offered fess is rs{self.fees}")
stu=student("R Pavani",28,50000,"MERN","KOMAL",27,"IT",70000,"MERN,PYTHON")
stu.displaystudentdetails()
stu.displayteacherdetails()


#student teacher

class Student:
    name="Komal"
    def display_name(self):
        print(f"name of student : {self.name}");
class Teacher(Student):
    teach_name="Pawani"
    def display_teach(self):
        print(f"{self.name} is the student of {self.teach_name}")
teach=Teacher();
teach.display_teach()
teach.display_name()


#inheritance with constructor

class Student:
    def __init__(self,name,course,fees,stu_phone_no):
        self.name=name;
        self.course=course;
        self.fees=fees;
        self.stu_phone_no=stu_phone_no;
    
    def display_name(self):
        print(f"name of student : {self.name}");  

class Teacher(Student):
     def __init__(self,tea ch_name,degis,sala,phone_no,name,course,fees,stu_phone_no):
        super().__init__(name,course,fees,stu_phone_no);
        self.teach_name=teach_name;
        self.degis=degis;
        self.sala=sala;
        self.phone_no=phone_no;
    def display_teach(self):
        print(f"{self.name} is the student of {self.teach_name}");

    def set_teacher_salary(self,sala):
        print(f"curent salary is {self.sala}")
        self,sala=sala
        print(f"Increament Salary is {self.sala}")

    def get_teacher_phone_no(self):
        #return self.phone_no
        #or
        print(f"Teacher contact no:{self.phone_no}")
teach=Teacher("Pavani","fsd","20000","86543789","komal","python developer","50000","86543789")
teach.display_teach()
teach.display_name()
teach.get_teacher_phone_no()
teach.set_teacher_salary(50000)
    