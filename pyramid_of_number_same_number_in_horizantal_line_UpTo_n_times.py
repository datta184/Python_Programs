# program for the printing pyramid with fixed digit
n=int(input("enter the number of rows:"))
for i in range (n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))