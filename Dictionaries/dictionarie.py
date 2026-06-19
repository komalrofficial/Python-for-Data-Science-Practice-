#1 create a dictionery containing student detail
student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        }
print(student)

#2 access and print the value of a specific key

student={
        "name" :"minal",
        }
print(student["name"])

#3 add a new key-value pair to a dictionery

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }

print(student)

#4 update the value of existing key

student["name"]="komal shende"
print(student["name"])

#5 delite a specific key from a dictionery

del student["name"]
print(student)

#6 check wether a key exist in a dictionery

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }
key=input("enter key to search:");
if key in student:
        print("key exist")
else:
        print("key not exist")
 
   
#7 find  the total number of  key-values  pair in dictioner

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }
count=0
count=count+1;
count=len(student)
print(count) 

#7 alternate method


student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }
print("total key-value pairs:",len(student)) 




#8 display all keys in a dictionery

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "napur",
        "DOJ" : "01-JAN-202"
        }

print(student.keys())

#9 display all values  in a dictionery

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }

print(student.values())

#10 display all key value pair in a dictionery

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }

print(student)

#11 iterate through all keys using a loop

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }
for key in student.keys():
        print(key) 
#12 iterate through all values using a loop

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }
for value in student.values():
        print(value) 


#13 iterate through all key-values using a loop

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }
for item in student.items():
        print(item) 

#14 print dictionery key in sorted order
student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }

for key in sorted(student.keys()):
        print(key)


#15 print dictionery key in sorted order

student={
        "id" : "101",
        "name" : "komal",
        "age" : "31",
        "city" : "nagpur",
        "DOJ" : "01-JAN-202"
        }

for value in sorted(student.values()):
        print(value)
