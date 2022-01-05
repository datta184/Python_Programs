#python program for printing all odd numbers in the range
ran=[10,20,304,50,607,7,70,90]
count=0
con=0
for i in ran:
    if i%2==0:
        count+=1
    else:
        con+=1
        
        
print("even numbers in the list are ",count)
print("odd numbers in the list are ",con)