# program for inverted right angle triangle pattern with digit
n=int(input("enter the number fof rows:"))
for i in range (n):
    for j in range (n-i):
        print(j+1,end=' ')
    print()