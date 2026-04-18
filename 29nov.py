# factorial : 
"""
5!  = 1*2*3*4*5 =120 
"""

"""
n=int(input("enter the  number  : "))
mul=1 
i=1 
while i <=n :
    mul = mul * i 
    i = i+1 
print("factorial is  :",mul)
"""

# factorial +sum :
"""n=int(input("enter the  number  : "))
mul=1 
i=1
sum=0  
while i <=n :
    mul = mul * i 
    sum =sum + i
    i = i+1 
print("factorial is  :",mul)
print("sum is  :",sum)
"""
# pattern  : 
"""
1. 
* * * * * 
* * * * *
* * * * * 
* * * * *
* * * * *
"""
i=1 
while i<=5 :
    j=1 
    while j<=5 :
        print("*",end=" ")
        j+=1
    print() 
    i+=1