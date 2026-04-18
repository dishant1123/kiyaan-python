"""
match (choice) :
    case 1 :
        print()
    case 2 :
        print()

"""
"""a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
print("WELCOME  TO MY CALCULATOR")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULUS")
choice =int(input("ENTER YOUR CHOICE : "))
match choice:
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5 :
        print(a%b)
    case 6:
        print("THANK YOU FOR USING MY CALCULATOR")
"""

# vowel  consonant : 

"""ch =input("enter the  character : ")

if ch =='a' :
    print("vowel")
elif ch =='e' :
    print("vowel")
elif ch =='i' :
    print("vowel")
elif ch =='o' :
    print("vowel")
elif ch =='u' :
    print("vowel")
else :
    print("consonant")
"""

ch=input("enter the  character : ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
elif ch >'a' and ch <='z' :
    print("consonant")
elif ch >'0' and ch <='9':
    print("num")
else :
    print('special character')