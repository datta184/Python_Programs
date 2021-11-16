# program To print square pattern with fixed alphabet symbol and asking for row
n=int(input("Enter the number of rows:"))
a=input("Enter the alphabet:")
for i in range(n):
    print(str(a)*n)