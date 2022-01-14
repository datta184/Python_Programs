# program for taking an integer input from user and print that table

n=int(input("inpu the number:"))#taking input from user

while 1:
    i=1;# initializing i with 1 for sequence purpose

    while i<=10: # checking the condition 
        print("%d X %d = %d"%(n,i,n*i));#printing the table

        i+=1;# increamenting the value of i

    choice=int(input("for continue printing next table press 0 for stop press 1:")) # asking for user to exit or continue

    if choice==0:
        break;

    n+=1
            