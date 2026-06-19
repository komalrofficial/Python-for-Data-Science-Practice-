


#SET CREATE

myset={10,20,30,40,50,30}
print(myset)

#get each element of the set

print("get each element of the set")
#convert it into list

set_into_list=list(myset)
print(set_into_list)

print(set_into_list[3])

#empty set
emptyset=set()
print(type(emptyset))
print(emptyset)

emptyset.add(100)
emptyset.add(102)
emptyset.add(106)
emptyset.add(109)
print(emptyset)

emptyset.update([103,147,166,107])
print(emptyset)

#remove element from the set
emptyset.remove(107)
print(emptyset)

#discard element from the set

emptyset.discard(109)
print(emptyset)

#pop element from the set(delite one element)

popped_element=emptyset.pop()
print("popped element:",popped_element)
print(emptyset)

#clear the set
emptyset.clear()
print(emptyset)