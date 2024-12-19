'''
numb=int(input("enter a number:"))
if numb==1:
   print('sunday')
elif numb==2:
   print('monday')
elif numb==3:
   print('tuesday')
elif numb == 4:
   print('wednesday')
elif numb == 5:
   print('thursday')
elif numb == 6:
   print('friday')
elif numb == 7:
   print('saturday')
else :
   print('number is out of range')
   '''


'''
   #even or odd
num=int(input('enter a number'))
if num % 2 == 0:
    print("it is even number")
else:
    print("it is odd number")
   ''' 
   
   #Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
'''
a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
'''


'''
#3. Write a program that asks the user for a number in the range of 1 to 12.
a={
    1:"january",
    2:"february",
    3:"march",
    4:"april",
    5:"may",
    6:"june",
    7:"july",
    8:"august",
    9:"september",
    10:"october",
    11:"november",
    12:"december"
}
b = int(input("enter a number between 1 to 12:"))
if (b in a):
    print(f"the month is {a[b]}")
else:
    print("number is out of range")
    '''


'''
#A school has following rules for grading system:
a=int(input("enetr mark of student:"))
if a<25:
    print("F")
elif a>=25 and a<45:
    print("E")
elif a>=45 and a<50:
    print("D")
elif a>=50 and a<60:
    print("C")
elif a>=60 and a<80:
    print("B")
else:
    print("A")
'''


'''
#Write a program to check whether a number is divisible by 7 or not.
a= int(input("Enter a number:"))
if a%7==0:
    print("the number is divisible by 7")
else:
    print("the number is not divisible by 7")
'''

'''
#Write a program to accept two numbers and mathematical operators and perform operation accordingly.
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
operator=(input("Enter operator (+,-,*,/)"))
if operator =='+':
    print(a+b)
elif operator =='-':
    print(a-b)
elif operator =='*':
    print(a*b)
elif operator =='/':
    if b !=0:
       print(a/b)
    else:
        print("mathmatical error")
else:
    print("Invalid operator")
'''

'''
#Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
a=int(input("Enter a number"))
if a%5==0:
    print("Hello")
else:
    print("Bye")
'''

'''
#8. Write a Python program that takes an integer input n n. From given number,
num=int(input("Enter a number"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(f"{num}")
'''

'''
#Write a Python program that takes a character input and checks whether it is a vowel or consonant.
alpha=str(input("Enter a letter"))
if alpha in 'aeiou':
    print(f"{alpha} is vowel")
elif alpha.isalpha():
    print(f"{alpha} is a consonant")
else:
    print("Please enter a valid alphabet")
    '''

'''
# Write a Python program to input marks and determine the grade based on the following conditions:
a=int(input("Enter a number:"))
if a>=90 and a<=100:
    print("A")
elif a>=80 and a<90:
    print("B")
elif a>=70 and a<80:
    print("C")
else:
    print("Fail")
'''

''''
#Write a Python program to categorize a person’s age:
a=int(input("Enter your age:"))
if a<13:
    print("Child")
elif a>=13 and a<=19:
    print("Teenager")
else:
    print("Adult")
'''

'''
#Write a Python program to check if a given character is uppercase, lowercase, or a digit.
a=input("Enter a character")

if a.isdigit():
    print("It is digit")
elif a.isupper():
    print("It is uppercase")
elif a.islower():
    print("It is lowercase")
else:
     print("Enter number or words")
   '''

'''
#Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").
a=str(input("Enter a traffic light color:"))
if a =='red':
    print("Stop")
elif a=='green':
    print('Go')
elif a=='yellow':
    print('Get Ready')
else:
    print("Please,Enter Red or Yellow or Green color to get the output")
'''

'''
#Write a Python program to check eligibility for a job based on age and experience:
age=int(input("Enter your age:"))
exp=int(input("Enter your job experience (in years):"))
if age>=18 and exp>=2:
    print("Eligible")
else:
    print("Not Eligible")
'''

'''
#Write a Python program to give advice based on the temperature:
tem= int(input("Enter temperature of your area:"))
if tem>30:
    print("It's hot,stay hydrated!")
elif tem<15:
    print("It's cold,wear warm clothes")
else:
    print("Enjoy the weather")
'''

'''
#Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
print("1:Pizza 2:Burger 3:Pasta")
g=str(input("Place an Order"))
if g=='pizza':
    print('$10')
elif g=='burger':
    print('Burger will be $7')
elif g=='pasta':
    print('$8')
else:
    print("It's not on our menu")

'''

'''
#Write a Python program to select players based on height:
a=float(input('Enter your height(in feet):'))
if a>=6:
    print("selected")
else:
    print("not selected")
'''

'''
#Write a Python program to check login credentials:
usnm=str(input('Enter username :'))
pas=str(input('Typr your password :'))
if usnm =='admin' and pas == 'password123':
    print("Access Granted")
else:
    print("Access Denied")
'''

'''
#Write a Python program that takes a month number (1–12) and outputs the corresponding season:
moth=int(input("Enter month number to see the season :"))
if moth ==12 or moth==1 or moth==2:
    print("Winter")
elif moth==3 or moth==4 or moth==5:
    print("Spring")
elif moth==6 or moth==7 or moth==8:
    print("Summer")
elif moth==9 or moth==10 or moth==11:
    print("Autumn")
else:
    print("There are only 12 months in a year")
'''

'''
#Write a Python program to check car loan eligibility:
sal=int(input("Enter your salary"))
cs=int(input("What is your credit score"))
if sal>=50000 and cs>=700:
    print("Eligible")
else:
    print("Not Eligible")
'''

'''
#Write a program to check whether the given number is in between 1 and 100 or not.
a=int(input("Enter a number :"))
if a>0 and a<=100:
    print("It's between 1 to 100")
else:
    print("It's not between 1 to 100")
   ''' 