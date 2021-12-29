# defining the function for changing the element
def swap(list,m,n):
    list[m],list[n]=list[n],list[m]
    return list

# program for the taking element in lilst from user
list=[] # creating the empty list

n=int(input("Enter the size of the list:"))

for i in range(0,n):
    print("enter the number at index:",i)

    items=int(input())
    list.append(items)
    
print("list is:",list)

m=int(input("enter the frist element`s position that you want to change:"))
n=int(input("enter the second element`s position that you want to change:"))

# a=list.index(m)
# b=list.index(m)

print(swap(list,m,n))