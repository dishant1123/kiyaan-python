"""
python  data type  :
1. list 
2. tuple
3. set
4. dictionary
5. string
"""
# list  : mutable sequence of element  ==> mutable ==> it can be changed. 

"""
l1 =[1,2,3,4,5,"kiyan",45.67] # you can take any variable name instead of l1 or anything.
print(l1) 
print(type(l1))
"""
# update in list : 
"""
l1 =[10,20,30,40,50,"kiyan",45.67] 
# index starts from 0    ==> backward for like 1 value index number is 0 , 2nd value index number is 1 and so on.
l1[3]="mind"
print(l1) 
"""
# remove from list :

"""
l1 =[10,20,30,40,50,"kiyan",45.67] 
num =int(input("enter the value  you want to delete : "))
if num in l1 :
    l1.remove(num)
    print(l1)
else :
    print("value not found")
"""

#odd even :
l1=[1,4,7,8,34,77,22]
even=[]
odd=[]
for i in l1:
    if i %2==0:
      even.append(i)  
    else:
        odd.append(i)
print("even number list : ",even)
print("odd number list : ",odd)
        