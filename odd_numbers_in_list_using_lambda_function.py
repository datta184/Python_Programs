# odd numbers in list using lambda function
l=[10,24,50,15,40,13,40,49]
even=list(filter(lambda x:(x%2!=0),l))
print("odd numbers in the list are:",even,end=" ")