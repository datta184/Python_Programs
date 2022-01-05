# printing the even numbers in list using list comprehension
list1 = [66, 21, 6, 35, 44, 93]
 
# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]
 
print("Even numbers in the list: ", even_nos)
