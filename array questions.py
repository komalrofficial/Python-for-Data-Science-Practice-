#find sum of elements in an array

arr=[85,34,76,20,90,45]
def sum_array(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum
ans=sum_array(arr)
print("sum of array is",ans);

#find largest element
def largest_element(arr):
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    return largest
ans2=largest_element(arr)
print("largest element is",ans2);

#find smallest element
def smallest_element(arr):
    smallest=arr[0]
    for i in arr:
        if i<smallest:
            smallest=i
    return smallest
ans3=smallest_element(arr)
print("smallest element is",ans3);

#search for an element in an array
def search_element(arr,element):
    for i in arr:
        if i==element:
            return(i)
    return False
ans4=search_element(arr,76)
print("element found:",ans4);

#reverse an array

def reverse_array(arr):
    reverse_arr=[]
    for i in range(len(arr)-1,-1,-1):
        reverse_arr.append(arr[i])
    return reverse_arr
ans5=reverse_array(arr)
print("reversed array is",ans5);

#sort an array
def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
ans6=sort_array(arr)
print("sorted array is",ans6);

#count even and odd numbers in an array
arr=[85,34,76,20,90,45]
def count_even_odd(arr):
    even_count=0
    odd_count=0
    for i in arr:
        if i%2==0:
            even_count+=1
            print(i,"is even")
        else:
            odd_count+=1
            print(i,"is odd")
    return even_count,odd_count

ans7, ans8 = count_even_odd(arr)
print("even numbers:", ans7, "in the array")
print("odd numbers:", ans8, "in the array")

#find average of elements in an array
# def average_array(arr):
#     sum=0
#     for i in arr:
#         sum=sum+i
#     average=sum/len(arr)
#     return average
# ans9=average_array(arr)
# print("average of array is",ans9);


def average_array(arr):
    sum=0
    for i in arr:
        sum=sum+i
    average=sum/len(arr)
    print("average of array is",average);

average_array(arr)
average_array([10,20,30,40,50])
average_array([1,2,3,4,5]);

sum=0
for i in arr:
    sum=sum+i
average=sum/len(arr)
print("average of array is",average);

arr=[85,34,76,20,90,45]
