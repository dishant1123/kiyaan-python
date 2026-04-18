# tuple  :  immtuble sequence of element  ==> immutable ==> it can't be changed.
"""
t1=(1,2,3,4,5,"kiyan",45.67)
print(t1)
print(type(t1))
"""
# update in tuple  : not possible  bcz  tuple is immutable.  
"""
t1=(1,2,3,4,5,"kiyan",45.67)
t1[3] ="patel"
print(t1)
"""
# built in function  : len min max sorted sum 
"""
t1=(1,23,45,67,12,34,56,78,90)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc 
print(sum(t1))
"""
# slicing  : 
"""
t1=    ( 1, 23, 45, 67, 12, 34, 56, 78, 90)
#index:  0  1   2   3   4   5   6   7   8 
print(t1[3])
print(t1[5])
print(t1[2:5]) 
"""

# method : 
"""
t1= ( 12, 12, 45, 67, 12, 34, 56, 78, 90)
print(t1.count(12))
print(t1.index(45))
"""

# task:1  convert tuple in to the  list  and  add your name in the list.
t1= ( 12, 12, 45, 67, 12, 34, 56, 78, 90)

l1= list(t1)
l1.append("kiyan")
print(tuple(l1))
