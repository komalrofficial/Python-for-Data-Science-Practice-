
class Teacher:
    __salary=30000;
    name="Pavani"

    def get_salary(self):
        print(f"Pavani's salary is {self.__salary}");
    
    def set_salary(self, sala, role):
        if(sala<50000 and sala>20000 and role=="Principle"):
            self.__salary =sala;
        else:
            print("you are not autorised person to update")
class Student(Teacher):
    def display_my_teacher(self):
        print(f"my teacher is {self.name}")

stud= Student()
stud.display_my_teacher()
stud.set_salary(20000,"Student")
stud.get_salary()
stud.set_salary(25000,"principal")
stud.get_salary()
