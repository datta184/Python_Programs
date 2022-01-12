# cearting a data of 5 student with first anme and a last name  
l=[]
# n=int(input("enter the number of students:"))
# def data():
for i in range(0,5):
    fname=input("enter first name:")
    lname=input("enter the last name:")
    print("\nname of the ",i+1 ,"student are :",fname,"",lname,"\n")
    a=fname+lname
    l.append(a)
# data()
print(" list of name of students are:\n",l)
for i in l:
    print("\n",i)
    
    
    

