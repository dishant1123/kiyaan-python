#task :1 check if a number is prime or not  and print  list of prime number. 

"""l1=[12,45,17,99,13,19]
l2=[]
for i in  l1:
    count =0
    for j in range(1,i+1):
        if i % j==0 :
            count+=1
    if count==2:
        l2.append(i)
print(l2)

"""

#task :2 print reverse of a number of list. 

"""l1=[123,456,245,789,13,19]
l2=[]
for i in l1 : 
    rev =0  
    temp =i 
    while temp > 0 :   # 0  > 0 
        r= temp % 10   # r = 1  % 10 = 1
        rev = rev *10 +r  # rev = 32 *10 +1 =321
        temp = temp // 10  # temp = 1 //10 =0
    l2.append(rev)
print(l2) 
"""

#task :3 print of a num factorial of list. 

l1=[1,4,5,6,8]
l2=[]
for i in l1 :
    fact=1 
    for j in range(1,i+1):
        fact=fact*j
    l2.append(fact)
print(l2)