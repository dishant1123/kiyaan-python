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

num =int(input("enter the number"))

if num % 5==0 and num %11 ==0:
    print("divisible by 5 and 11")
elif num % 5==0:
    print("divisible by 5")
elif num % 11 ==0:
    print("divisible by 11")
else :
    print("not divisible by 5 or 11")
