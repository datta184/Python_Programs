# program for Right Half Diamond Pattern with alphabet symbols in dictionary ordern
n= int(input("enter the number of rows:"))
for i in range (n):
    for j in range (i+1):
        print(chr(65+j),end=' ')
    print()