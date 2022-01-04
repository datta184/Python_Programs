# Python program to find minimum number in a list

# creating empty list
list1 = []

# Taking inpput from user
num = int(input("Enter number of elements in list: "))


for i in range(1, num + 1):
	ele= int(input("Enter elements: "))
	list1.append(ele)
	
# print minimummum element
print("Smallest element is:", min(list1))
