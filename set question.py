#1 create and print a set
set={10,20,30,50,79}
print(set)

#2 add element to a set using add()

set={10,20,30,50,79}
set.add(90)
print(set)

#3 add multiple element using update
set={10,20,30,50,79}
set.update([69,78,65,53,43])
print(set)

#4remove element using remove
set.remove(78)
print(set)

#5 discard element using discard
set.discard(30)
print(set)

#6 remove random element using pop

popped_set=set.pop()
print("poped element:",popped_set)
print(set)

#7 clear all element from set

set.clear()
print(set)

#8 copy one set to anotherset2={}
set={10,30,70,67}
set2={}
set.copy()
print(set)

#9 find length of set
set={10,30,59,76}
n=len(set)
print(n)

# #10 check element exist in set
# set={10,20,30,40,50}
# num=int(input("enter the number:"));
# if num in set:
#     print("the number exist:");
# else:
#     print("set empty")

#5 add multiple element to a set using update
set={20,10,80,89,}
set.update([43,89,76,56])
print(set)

#6 remove an element using remove

set={20,30,80,78,65,43,67}
set.remove(67)
print(set)

#remove an element using discard
set={20,30,80,78,65,43,67}
set.discard(15)               #if value is not given in set output is same
print(set)

set={20,30,80,78,65,43,67}
set.discard(78)               #if value is given in set then it discard that particular value
print(set)


#8 remove and return a random element using pop()

set={20,30,80,78,65,43,67}
set.pop()
print(set)

#9 clear all element from a set

set={20,30,80,78,65,43,67}
set.clear()
print(set)

#10 copy a set and verify that changes to the copy do not affect the original
set={20,30,80,78,65,43,67}
set.copy()
print(set)


#14check wether two list contain the same unique elements.
