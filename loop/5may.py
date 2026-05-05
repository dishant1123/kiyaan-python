"""
loop  : iteration  == > repeation

1. for  : entry control  loop  
2. while : entry control  loop
3. do while   : exit 


for loop  : syntax : 

for variable name in range(start , end , step) : 
    statement(s)
"""

# 1-100 : 

"""for i in range(1,101): 
    print(i,end=" ")
"""
# 100-1 : 
"""
for i in range(100,0,-1): 
    print(i,end=" ")
"""    
# odd number  : 
"""for x in range(1,100,2): 
    print(x,end=" ")

"""
# even number  : 
"""for i in range(0,100,2): 
    print(i,end=" ")
"""

# a to z using for  loop  : 

"""for  i in range(97,123):
    print(chr(i),end=" ")
"""

# user input  : 
"""
n=int(input("enter the  number  : ")) 
for i in range(1,n+1): 
    print(i,end=" ")
    
"""

# odd even : 
"""
n=int(input("enter the  number  : ")) 
for i in range(0,n+1,2): # if start with  0 then print  even and start with 1 then print odd 
    print(i,end=" ")
"""

# n natural  number sum  : 

"""
n=int(input("enter the  number  : "))
sum =0 
for i in range(1,n+1) :    # ex : natural number  : if user enter 3 then 1+2+3 = 6. 
    sum = sum +i 
print("n natural  number sum is  : ",sum)
"""