#set operator union

set1={10,20,30}
set2={40,50,60}
print(set1|set2)

#difference
set1={10,20,30}
set2={20,10,60}
print(set1-set2)

#symetric difference
set1={10,20,30}
set2={20,10,60}
print(set1^set2)

#create empty set and add elements to it
Myset=set();

Myset.add(10)
Myset.add(20)
Myset.add(30)
Myset.add(40)
Myset.add(50)
print(Myset)

# set1=set();
# for i in range(5):
#     ele=int(input("enter element"));
#     set1.add(ele)
# print(set1);

#create a set from alist containing duplicate value.
mylist=[10,20,30,40,50]
myset=set(mylist);
print(myset)

# #find the length  of the set 
# set={10,20,30,40,50}
# n=len(set)
# print(n)

# #add multiple element to a set
# set={10,20,30,40,50}
# set.update([30,60,67])
# print(set)

#remove duplicate elements from a list using a set
mylist=[10,20,30,10,30,60,80,60]
myset=set(mylist)
print(myset)