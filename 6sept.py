# for loop  : 
"""
loop : ==> iteration  == > repeation  

1-100 : 

syntax : 

for variable in range() :
    print(variable)
"""

# 1-100 : 
"""for i in range(1,101):
    print(i,end=" ")
"""
# 100-1 : 
"""
for k in range(100,0,-1) :
    print(k,end=" ")
"""
# odd : 
"""for z in range(1,101,2):
    print(z,end=" ")
"""
# even : 
"""
for z in range(2,101,2):
    print(z,end=" ")
"""

n=int(input("enter the  number  : "))  # 5
count =0 
for i in range(1,n+1):  # 5 , 6
    if n % i == 0 :   #5 % 5  == 0 
        count +=1    # 2  
if count == 2 :
    print("prime")
else :
    print("not prime")
