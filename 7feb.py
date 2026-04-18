#dictionary  (use dict): mutable  ==> changes in dict . key value  pair 

"""
d1={"maths" :99,"eng":78,"com":89}
# maths ==>99  ==> maths  ==> key  99 ==>value 

print(d1) 
print(type(d1))
"""
# add in dict : 
"""
d1={"maths" :99,"eng":78,"com":89}
d1["science"] =93
print(d1)
"""
# built in function  : 

"""
d1={"maths" :99,"eng":78,"com":89}
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

# method : 
d1={"maths" :99,"eng":78,"com":89}

# d1.clear()
# print(d1)

# d2= d1.copy()
# print(d2)

# print(d1.keys())
# print(d1.values())
# print(d1.items())

"""
for i  ,j in d1.items(): 
    print(i,j)
"""
"""l1=["kiyan","ram"] 
# {"kiyan" :100,"ram" :100}

d2= dict.fromkeys(l1,100)
print(d2)

d1.update(d2)
print(d1)
"""

# delete : 

"""
d1={"maths" :99,"eng":78,"com":89}

d1.pop("eng")
print(d1)

d1.popitem()
print(d1)
"""
# get : 
"""
d1={"maths" :99,"eng":78,"com":89}

print(d1.get("com"))"""


"""
MCQ : 

1. what  is the len of dict ? 
    d1= {"kiyan" :100, "ramesh":89,"mihir" :67,"kiran" :89}
    print(len(d1))
    a. 2  b. 3  c. 4  d. 5
    
2. what  is the max of dict ?
    d1= {"kiyan" :100, "ramesh":89,"mihir" :67,"kiran" :89}
    print(max(d1))
    a. 100  b. 89  c. 67  d. none 

3. 

"""