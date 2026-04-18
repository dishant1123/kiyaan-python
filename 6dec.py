"""
# 1 :       2 :
1 2 3 4 5     *
1 2 3 4 5     * *
1 2 3 4 5     * * * 
1 2 3 4 5     * * * *
1 2 3 4 5     * * * * *

"""
"""
i=1 
while i<=5 :
    j=1 
    while j<=5 :
        print(j,end=" ")
        j+=1 
    print()
    i+=1
"""

# 2:      
"""
*
* *
* * *
* * * *
* * * * *
"""
"""
i=1
while i<=5 :
    j=1 
    while j<=i :
        print("*",end=" ")
        j+=1 
    print()
    i+=1
"""
#3 :
"""
* * * * *  
* * * *
* * *
* *
*
"""
i=1
while i<=5 :
    j=5
    while j>=i :
        print("*",end=" ")
        j-=1 
    print()
    i+=1
