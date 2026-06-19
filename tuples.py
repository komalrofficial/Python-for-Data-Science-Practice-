#tuples


#create tuples
#syntax:variable=();


tuple1 = (1,2,3)
print(tuple1)

#individual value
#using indexing

print(tuple1[1])
print(tuple1[0])

print ("value using for loop")
for value in tuple1:
    print(value)

#tuple operator
t1=(2,3,4)    
t2=(4,5,6)
print(t1+t2)   #

print(t1*4)

#convertion 
tuple2=(30,40,50)
tuple_in_list=list(tuple2)
print(tuple_in_list)

tuple2=(30,40,50)
tuple_in_set=set(tuple2)
print(tuple_in_set)


#tuple convert into set

tuple_in_set1=set(tuple2)
print(tuple_in_set)


#combine two different tuples and convert it into set

tuple_in_set1=set(t1+t2)
print(tuple_in_set1)

#remove the duplicate value of tuples using set
tup=(10,20,30,10,30,40)

removedup=set(tup)
print(removedup)
print(tuple(removedup))

#methods
#count()
no_ofele=tup.count(10)
print(no_ofele)


#len()
print(len(tup))

#min()
print(min(tup))
 
#max
print(max(tup))

#sum 
print(sum(tup))

#sorted
print(sorted(tup))


student = ("Komal", "IT", 50000)

name, dept, sala = student

print(name)
print(dept)
print(sala)


print(student[0])