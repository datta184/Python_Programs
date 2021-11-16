#program for printing square pattern with provided fixed digit in every row
n=int(input("enter teh number of rows:"))
for i in range (n):
    print((str(i+1)+' ')*n)