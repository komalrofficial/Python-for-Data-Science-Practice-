studentdata=[1,"komal",20000.00,True]
print(type(studentdata))

print(studentdata[0])
print(studentdata[1])
print(studentdata[2])
print(studentdata[3])

#positive indexing negative indexing

studentdata=[1,"komal",20000.00,True]
print(type(studentdata))
print(studentdata[-2])


#1  create and print a list

my_list=["komal",5.00,1994,"shende",True]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

#we fetch data directly by using index number
for item in my_list:
    print(item)

#we can fetch data by using loop
for index in range(len(my_list)):
    print(my_list[index])

#2 Traverse all element in a list
my_list=["komal",5.00,1994,"shende",True]
for index in range(len(my_list)):
    print(my_list[index])

#3 find sum of list elements
list=[80,98,67,54,43]
sum_result=sum(list)
print(sum_result)

#4 find largest elements in the list
list=[80,98,67,54,43]
largest=max(list)
print(largest)

#5 find smallest elements in the list
list=[80,98,67,54,43]
smallest=min(list)
print(smallest)

#6 find average of list element
list=[80,98,67,54,43]
sum_result=sum(list)
print(sum_result)
n=len(list)
print(n)
average=sum_result/n
print(average)

#7 search an element in list
list=[10, 30, 10, 33, 88, 24, 10, 89, 10, 45]
position=list.index(33)
print(position+1)


#8 insert element at specific position 
list=[10,30,40,60,70]
list.insert(1,20)
list.insert(4,50)
print(list)

#9 append element to list
list=[10,30,40,60,70]
list.append(80)
print(list)

#10 remove element from list
list=[10,30,40,60,70]
list.remove(30)
print(list)

#11 delite element using pop
list=[10,30,40,60,70]
list.pop(2)
print(list)

#12 reverse a list
list=[10,30,40,60,70]
list.reverse()
print(list)

#13 sort list in ascending order
list=[10,30,80,40,60,70]
list.sort()
print(list)

#14 sort list in desending order
list=[10,30,80,40,60,70]
list.sort(reverse=True)
print(list)

#15 count even and odd number in a list
list=[10,30,55,33,88,24]
even_count=0
odd_count=0
for i in (list):
    if i%2==0:
       even_count+=1
       print("even number", i)
    else:
       odd_count+=1
       print("odd number",i)
print("Even : ", even_count)
print("Odd :", odd_count)

#16 copy one list to another
list=[]
list1=[10,20,30]
list=list1.copy()
print(list)

#17 merge two list
list=[10,30,55,33,88,24]
list1=[10,89,65,45]
list.extend(list1)
print(list)

#18 count occurence of an element
list=[10, 30, 10, 33, 88, 24, 10, 89, 10, 45]
count=list.count(10)
print(count)

#19 find index position of an element
list=[10, 30, 10, 33, 88, 24, 10, 89, 10, 45]
position=list.index(89)
print(position+1)

#20 clear all element from list

list=[10, 30, 10, 33, 88, 24, 10, 89, 10, 45]
list.clear()
print(list)
