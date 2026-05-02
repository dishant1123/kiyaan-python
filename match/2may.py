# match  : use when you want  menu driven program . 
# ex :1
""" 
a=int(input("enter the number : "))
b= int(input("enter the number : "))
print("CALCULATOR")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6.exit")
choice=int(input("enter the choice : "))
match choice : 
    case 1 :
        print("addition of two  number  is : ",a+b)
    case 2 :
        print("subtraction of two  number  is : ",a-b)
    case 3 :
        print("multiplication of two  number  is : ",a*b)
    case 4 :
        print("division of two  number  is : ",a/b)
    case 5 :
        print("modulus of two  number  is : ",a%b)
    case 6 :
        print("thanks for using the calculator")
"""

# ex: 2 vowel  or consonant

"""ch =input("enter the character : ")

match ch : 
    case 'a' | 'e' | 'i' | 'o' | 'u' :
        print("vowel") 
    case _ :
        print("consonant")
"""
# ex :3 ask user to enter the number and  print the  month name and  its days. 

# nested match  : 

print("1.FRUITS")
print("2.VEGETABLES")
choice =int(input("enter the choice : "))

match choice : 
    case 1 : 
        print("1.APPLE : 100rs.")
        print("2.BANANA: 50rs ")
        print("3.ORANGE: 120rs")
        print("enter the  subchoice : ")
        subchoice =int(input("enter the subchoice : "))
        match subchoice :
            case 1 : 
                print("you selected apple")
                print("enter the fruit quantity : ")
                qty =int(input("enter the quantity : "))
                price = qty*100
                print("the price is : ",price,"rs.")
            case 2 :
                print("you selected banana")
                print("enter the fruit quantity : ")
                qty =int(input("enter the quantity : "))
                price = qty*50
                print("the price is : ",price,"rs.")
            case 3 :
                print("you selected orange")
                print("enter the fruit quantity : ")
                qty =int(input("enter the quantity : "))
                price = qty*120
                print("the price is : ",price,"rs.")
    case 2 : 
        print("1.CARROT : 40rs.")
        print("2.POTATO : 30rs ")
        print("3.ONION  : 60rs")
        print("enter the  subchoice : ")
        subchoice =int(input("enter the subchoice : "))
        match subchoice :
            case 1 : 
                print("you selected carrot")
                print("enter the fruit quantity : ")
                qty =int(input("enter the quantity : "))
                price = qty*40
                print("the price is : ",price,"rs.")
            case 2 :
                print("you selected potato")
                print("enter the fruit quantity : ")
                qty =int(input("enter the quantity : "))
                price = qty*30
                print("the price is : ",price,"rs.")
            case 3 :
                print("you selected onion")
                print("enter the fruit quantity : ")
                qty =int(input("enter the quantity : "))
                price = qty*60
                print("the price is : ",price,"rs.")