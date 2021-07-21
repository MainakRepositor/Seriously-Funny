row =6
col=4
t = '😂'

for i in range(row-1):
    print(t)
    
for i in range (col+1):
    print(t,end=" ")
print()
    
for i in range(0,row):
    for j in range(0,col):
        if((j == 0 or j == col-1) and (i!=0 and i!=row-1)) :
            print(t,end=' ')   
        elif( ((i==0 or i==row-1) and (j>0 and j<col-1))):
            print(t,end=" ")
        else:
            print(end='   ')  

    print()  

    
for i in range(row-1):
    print(t)
    
for i in range (col+1):
    print(t,end=" ")


#Coded by Mainak, 21/7/2021
