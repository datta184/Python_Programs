# program for  Right Angle Triangle pattern with fixed alphabet symbol
n = int(input("entert the number of rows:"))
for i in range (n):
    print((chr(65+i)+' ')*(i+1))