"""
menu  driven  program : 

match  : 
"""

"""a= int(input("enter the number 1 :"))
b= int(input("enter the number 2 :"))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")

choice =int(input("enter the choice :"))

match choice :
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3 :
        print(a*b)
    case 4 :
        print(a/b)
    case 5 :
        print(a%b)
    case 6 :
        print("invalid choice")
"""
# hotel  menu  :

print("KIYAN HOTEL")
print("1. Punjabi")
print("2. Gujarati")
print("3. Kathiyawadi")

choice =int(input("enter the choice :"))
match choice :
    case 1 :
        print("Punjabi fix thali  : 300")
        qty =int(input("enter the quantity :"))
        bill =qty *300
        print("bill amount : Rs",bill)
    case 2:
        print("Gujarati fix thali  : 200")
        qty =int(input("enter the quantity :"))
        bill =qty *200
        print("bill amount : Rs",bill)
    case 3:
        print("Kathiwadi fix thali  : 400")
        qty =int(input("enter the quantity :"))
        bill =qty *400
        print("bill amount : Rs",bill)
        