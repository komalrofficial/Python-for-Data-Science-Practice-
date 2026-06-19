#1 create a tuple with 10 integer value and display all elements

tuple=(1,2,3,4,5,6,7,8,9,56)
print(tuple)

#2 find the length of a tuple without using len()

tuple1=(3,5,7,8,9)
count=0;
for i in tuple1:
    count=count+1;
print(count)

#3 access and print the first,last and middle elementin a tuple

tuple1=(3,5,7,8,9)
print(tuple1[0])
print(tuple1[2])
print(tuple1[4])

#4 count the number of accourance of a given element in a tuple

tuple2=(1,3,2,5,1,2,3,7,3)
no_of_ele=tuple2.count(3)
print(no_of_ele)

#5 find the index of a specific element in a tuple
tuple3=("komal","IT","nagpur")
print(tuple3[0])
print(tuple3[1])
print(tuple3[2])

#6 check wether element exist in a tuple

# tuple3=("komal","IT","nagpur")
# element=input("enter to search element:");
# if element in tuple3:
#     print("element exist")
# else:
#     print("not exist")

#9 convert a list into a tuple



    

#10 convert a tuple into a list

tuple1=(3,5,7,8,9)
tuple_in_list=list(tuple1)
print(tuple_in_list)

#14 concatenate two tuples and print the result
t1=(4,6,8,9)
t2=(6,8,9,3)
print(t1+t2)

#15 repeat a tuple 3times using opeartor
tuple1=(3,5,7,8,9)
print(tuple1*3)

#20 find the maximum element in a tuple
tuple4=(40,89,65,87,99,34,23)
print(max(tuple4))

print(max(tuple4))

#21 find the manimum element in a tuple
tuple4=(40,89,65,87,99,34,23)
print(min(tuple4))

#22 find the sum of all element in a tuple
tuple4=(40,89,65,87,99,34,23)
print(sum(tuple4))

#24 print all positive number from tuple
tup=(40,89,65,87,99,34,23)
for tu in tup:
    if tu>0:
        print ("positive number:",tu);
    else:
        print("not posi:",tu);

#25 print all negative number from tuple
tup2=(-9,8,76,-98,-65,)
for tup in tup2:
    if tup<0:
        print("negative number:",tup);
    else:
        print("positive number:",tup);