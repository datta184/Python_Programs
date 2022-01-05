# program to find the second laarg number in teh list

#first creating the empty list
emp=[]

# asking use for the user for size of list or element of list 
n=int(input("Enter the number of elements how many element to be inseted:"))

for i in range(1,n+1):
    ele=int(input("Enter the element in the lsit:"))
    emp.append(ele)

# now sorting the list emp

emp.sort()

# prirtning the second larg number in list
print(emp[-2])
    