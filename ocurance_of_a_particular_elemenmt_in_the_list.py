# ocurance of a particular elemenmt in the list 
l=[]
n=int(input("how many elements list you want:"))

for i in range(0,n):
    
    n = int(input("Enter the list element :"))  #taking input from user
    l.append(n)  # inserting elements in the list with the help of append function
  
count=int(input("which elements occurance you want:"))
print("\noccurance of",count,"is",l.count(count),"times")

