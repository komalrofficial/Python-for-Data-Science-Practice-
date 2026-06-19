#13 find duplicate values in a list using sets
mylist=[10,20,30,20,60,70]

for i in range(len(mylist)):
    duplicate = mylist.count(mylist[i])
    if(duplicate>1):
        print(f"{mylist[i]} is duplicate")
        break;

MySet = set(mylist)
print(MySet)



#14 check whether two list contain the same unique elements
ch1 = {"a", "b", "c"}
ch2 = {"c", "d", "e"}
print(ch1 & ch2)

#15 find all unique character in a string`
str = "Hey Hello"
b= set(str)
print(b)

#16 find common character between two string

ch={"a","b","c","d"}
chb={"b","e","k","c"}
print(ch1 & chb)

#17determine wether a string contains all unique character
str = "Hey Hello komal"
b= set(str)
print(b)

