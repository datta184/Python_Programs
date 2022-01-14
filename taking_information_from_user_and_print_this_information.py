# taking information from user and print this information
emp_name=str(input("enter the name:"))
emp_country=str(input("enter the country name:"))
emp_mob=int(input("enter the mob no:"))

data=[emp_name,emp_mob,emp_country]# storing input in list
print("\n**************************printing the data******************************")
print("employee name is : %s\nemployee mobile number is:%d\nemployee country is :%s\n"%(data[0],data[1],data[2]))
