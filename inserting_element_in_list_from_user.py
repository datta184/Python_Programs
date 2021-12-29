# program for the taking element in lilst from user
list=[] # creating the empty list

n=int(input("Enter the size of the list:"))

for i in range(0,n):
    print("enter the number at index:",i)

    items=int(input())
    list.append(items)
    
print("list is:",list)