# occurence of each element in list

def oc(lst,x):
    count=0
    for i in lst:
        if(i==x):
            count+=1

    return count
    
lst = [ 5,1, 4, 5, 7, 8,5 ]
x=5
print("{} occured {} times:".format(x,oc(lst,x)))


