# if else : 
"""
syntax : 
if condition : 
    print("condition is true")
else : 
    print("condition is false")
    
"""
# ex :1  check  number is even or odd
"""n=int(input("enter the number : "))
if n% 2==0 : 
    print("even")
else : 
    print("odd")
"""

# ex :2 ask user to enter the age  and  check it is  eligible to vote or not. 
"""
age =int(input("enter the age : "))
if age >=18 :
    print("eligible to vote")
else : 
    print("not eligible to vote")
    
"""
# task: 1 ask user to enter the  number and  check it is  divisible  by 5  or  not. 

# ex :3  grade system : 

maths =int(input("enter the maths  marks: "))
science =int(input("enter the science  marks : "))
english =int(input("enter the english marks: "))
gujarati =int(input("enter the gujarati marks  : "))
geography =int(input("enter the geography  marks : "))
history =int(input("enter the history  marks : "))

print("===============GOTIRTH VIDHYAPITH=================")
print("DATE :11/04/2022\t\t\tROLLNO :19\n")
print("NAME :Kiyan K Patel\n")
print("Srno\t\t\tSubjects\t\t\tMarks")
print("1.\t\t\tMaths\t\t\t\t",maths)
print("2.\t\t\tScience\t\t\t\t",science)
print("3.\t\t\tEnglish\t\t\t\t",english)
print("4.\t\t\tGujarati\t\t\t",gujarati)
print("5.\t\t\tGeography\t\t\t",geography)
print("6.\t\t\tHistory\t\t\t\t",history)
print("7.\t\t\tTotal\t\t\t\t",maths+science+english+gujarati+geography+history)
print("==============================================")

percentage = (maths+science+english+gujarati+geography+history)/5 

if percentage >=90 :
    print("Grade :A+")
elif percentage >=80 :
    print("Grade :A")
elif percentage >=70 :
    print("Grade :B+")
elif percentage >=60 :
    print("Grade :B")
elif percentage >=50 :
    print("Grade:C+")
elif percentage >=40 :
    print("Grade:C")
else : 
    print("Grade:Fail")
    
    







