# task :1 ask user to enter the character and  check it is  vowel or  consonant or digit or special character.

"""ch =input("enter the character")

if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("vowel")
elif ch >'a' and ch<='z' :
    print("consonant")
elif ch >'0' and ch<='9' :
    print("digit")
else : 
    print("special character")
"""

# task :2 ask user to enter the  number and check it is  divisible by 5 or 11 or both. 

"""num =int(input("enter the number"))

if num % 5==0 and num %11 ==0:
    print("divisible by 5 and 11")
elif num % 5==0:
    print("divisible by 5")
elif num % 11 ==0:
    print("divisible by 11")
else :
    print("not divisible by 5 or 11")
"""
# task  :3 ask user to enter the salary  and calculate the HRA and DA . 
"""
salary           HRA       DA  

salary <10000    20%        70% 
salary <20000    30%        80%
above  25000     35%        90% 

"""

salary = int(input("enter the  salary : "))

if salary <10000 : 
    hra = salary * 0.2 
    da = salary * 0.7
    basic = salary + hra + da
    print("basic salary is :",basic)
elif salary <20000 :
    hra = salary * 0.3 
    da = salary * 0.8
    basic = salary + hra + da
    print("basic salary is :",basic)
else :
    hra = salary * 0.35 
    da = salary * 0.90
    basic = salary + hra + da
    print("basic salary is :",basic)