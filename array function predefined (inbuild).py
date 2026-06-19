#append add new variable at the end
# arr=[10,30,40,60]
# num=int(input("enter a number:"));
# arr.append(num)
# print(arr)
# #insert add element on specific position or index

arr=[10,30,40,60]
arr.insert(1,20)
arr.insert(4,50)
print(arr)

#remove specific value
arr=[10,30,40,90,60,30,30,50]
arr.remove(30)
arr.remove(90)
print(arr)

#pop remove specific index value
arr=[10,20,30,50,60]
arr.pop(2)
print(arr)
#sort assending or desending
arr=[60.87,45,453,65,32]
arr.sort();
print(arr)
arr.sort(reverse=True)
print(arr)

#reverse
arr=[60.87,45,453,65,32]
arr.reverse()
print(arr) 
#index

arr=[10,20,30,50,60]
position=arr.index(50)
print(position+1)
print(position)

#count the elementsar
arr=["komal","shende"]; 
count=arr.count(10)
print(count)

#copy
arr=[]
arr1=["komal","shende"];
print("before copy:",arr)
arr=arr1.copy()
print(arr)

#clear
arr=["komal","shende"];   
arr.clear()
print(arr)

#extended
arr=[10,50];
arr1=[56,98,76,];
arr.extend(arr1)
print(arr)

#length
arr=["komal","shende","rangari"]; 
n=len(arr)
print(n)

#maximum value
arr=[10,20,30,50,60]
largest=max(arr)
print(largest)

#manimum value
arr=[10,20,30,50,60]
smallest=min(arr)
print(smallest)

#sorted
arr=[69,87,65,45,36]
sorted_arr=sorted(arr)
print(sorted_arr)

#sum
arr=[10,20,30]
sum_result=sum(arr)
print(sum_result)

#find sum of elements
arr=[10,20,30,40,50]
sum1=sum(arr)
print(sum1)

#find average of  array elements
arr=[10,20,30,40,50]
sum=sum(arr)
n=len(arr)
average=sum/n
print(average)

#find largest
arr=[10,20,30,40,50]
largest=max(arr)
print(largest)

#find smallest
arr=[10,20,30,40,50]
smallest=min(arr)
print(smallest)

#reverse arry
arr=[10,20,30,40,50]
arr.reverse()
print(arr)

#count even and odd
# arr=[87,97,65,44,22,11]
# def even_odd_numbers(arr):
#     even_count=0
#     for i in arr:
#         if i%2==0:
#             even_count+=1
#             print("even numbers");
#         else:
#             print("odd numbers");
# print("even_number:",arr);

#14 extend value using 2arr
arr=[10,20,30,40]
arr1=[50,87,56,80]
arr.extend(arr1)
print(arr)

#13 arr=[8,9,-6,-4,9,-2]
for i in (arr):
    if i<0:
        print("negative numbers:",i);

#12  sort program in desending order

arr=[20,60,10,75,45,34]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

#2  program to merge two arry and sort it in asending order
arr=[20,60,10,75,45,34]
arr1=[70,47,34,13]
arr.extend(arr1)
print(arr)
arr.sort()
print(arr)

#program to merge two sorted arrays into a single sorted array

# arr=[10,70,64,76]
# arr1=[50,89,76,32]
# arr.sort()
# print(arr)
# print(arr1)
# print(arr,arr1)

# 11  program to merge two sorted arrays into a single sorted array
arr=[10,70,64,76]
arr1=[50,89,76,32]
arr.extend(arr1)
print(arr)
arr.sort()
print(arr)

#8 write a program to  count and display the frequency of each element of an arry

arr=[10,30,10,87,10,70,60,10,76,10]
count=arr.count(10)
print(count)
length=len(arr)
print(length)

#7 write a program to remove duplicate value

arr=[10,30,10,87,10]
arr.pop(0)
arr.pop(1)
arr.pop(2)
print(arr)

#1 print the index position if the element is found
arr=[10,60,56,45,34]
position=arr.index(56)
print(position+1)

#2nd largesr element

arr=[40, 41, 42, 44, 45, 46, 47, 49]
find = arr[0];
for i in range(1, len(arr)):
    if(arr[i]==find+1):
        find+=1;
        continue;
    else:
        print("missing number ", find+1);
        find+=2;



# 9 
maxdiff =0;
arr=[40,78,65,54,98]

arr1=[]

for i in range(len(arr)):
    if i+1<len(arr):
        diff = arr[i] - arr[i+1];
    if maxdiff<diff:
        maxdiff=diff;
        arr1 = [arr[i], arr[i+1]];
print(f"The maximum differ is {maxdiff} of {arr1}");


maxdiff =0;
arr=[90,88,65,45,30]

arr1=[]

for i in range(len(arr)):
    if i+1<len(arr):
        diff = arr[i] - arr[i+1];
    if maxdiff<diff:
        maxdiff=diff;
        arr1 = [arr[i], arr[i+1]];
print(f"The maximum differ is {maxdiff} of {arr1}");
  

