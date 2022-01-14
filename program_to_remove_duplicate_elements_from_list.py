# program to remove duplicate elements from list
# naming convention used is snake case
list_1=[1,2,3,4,5,6,7,5,4,3,2,7,8]

# creating a empty list

list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)