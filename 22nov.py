# while  loop :
"""
syntax : 

i=intial value  
while  con :
    print(i)
    i =i+1 /dec  
"""
# 1-100 : 
"""
i=1   # start 
while  i <=100 :  # 100 ==> end 
    print(i,end=" ")
    i = i+1 
"""

# 100-1 : 
"""i=100 
while i >=1 :
    print(i,end=" ")
    i=i-1    
"""

# odd 
"""
i=1 
n=int(input("enter the number : "))

while i< n : 
    if i %2 ==1 :
        print(i,end=" ")
    i=i+1
"""
# sum  : 
"""i=1 
n=int(input("enter the number  : "))
sum =0 
while i <=n : 
    sum =sum +i 
    i =i+1 
print("sum of  n natural  number  is  :",sum)
"""
# odd even  sum : 

i=1 
n=int(input("enter the  number : "))
oddsum =0 
evensum =0 

while i<=n :
    if i %2 ==0 :
        evensum =evensum +i 
    else :
        oddsum =oddsum +i
    i+=1
print("sum of  odd natural  number  is  :",oddsum)
print("sum of  even natural  number  is  :",evensum)
