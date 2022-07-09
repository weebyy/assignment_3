def a():
    num_day = int("Please enter the a number between 1 to 7: ")
    if num_day == 1:
        print("The day of the week to corresponding to the number you have entered is Sunday")
    elif num_day == 2:
        print("The day of the week to corresponding to the number you have entered is Monday")
    elif num_day == 3:
        print(
            "The day of the week to corresponding to the number you have entered is Tuesday")
    elif num_day == 4:
        print(
            "The day of the week to corresponding to the number you have entered is Wednesday")
    elif num_day == 5:
        print(
            "The day of the week to corresponding to the number you have entered is Thursday")
    elif num_day == 6:
        print(
            "The day of the week to corresponding to the number you have entered is Friday")
    elif num_day == 7:
        print(
            "The day of the week to corresponding to the number you have entered is Saturday")
    else:
        print("You havent entered the correct number!")
a()

def b():
    month = input("Please enter the name of a month: ")
    month.islower()
    if month == "january" or "march" or "june" or "august" or "october" or "december":
        print("The month u have entered has 31 days")
    elif month == "febraury":
        print("The month you have entered has 28 days")
    else:
        print("The month you have entered has 30 days")
b()

def c():
    alpha = input("Please enter an alphabet: ")
    alpha.islower()
    if alpha == "a" or "e" or "i" or "o" or "u":
        print("The alphabet you entered is a vowel!")
    else:
        print("The alphabet entered is consonant!")
c()

def d():
    print("Not done yet!")
d()

def e():
    usr_input = input("Please enter something: ")
    if(usr_input.isalpha()):
        print("The character entered is an alphabet!")
    elif(usr_input.isdigit()):
        print("The character is a number!")
    else:
        print("The character entered is a speical character!")
e()

def f():
    usr_input = int(input("Please enter a number: "))
    if usr_input % 2 == 0:
        print("The entered number is an even number!")
    else:
        print("The entered number is an odd number!")
f()

def g():
    usr_input = int(input("Please enter a number: "))
    if usr_input % 8 == 0:
        print("The entered number is divisible by 8")
    else:
        print("The entered number is not divisible by 8!")
g()

def h():
    usr_input = int(input("Please enter an integer: "))
    if usr_input < 0:
        print("The enetred the number is a negative number!")
    elif usr_input == 0:
        print("The number is niether negative nor positive!")
    else:
        print("The number is a positive integer!")
h()

def i():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))

    if num1 < num2:
        print("num2 is greater than num1!")
    else:
        print("num1 is greater than num2")
i()

def j():
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You arent eligible to vote!")
j()

def k():
    print("not done yet!")
k()

def l():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))
    if num1 % num2 == 0 or num2 % num1 == 0:
        print("The numbers are divisable!")
    else:
        print("The enters arent divisable")
l()

def m():
    angle_1 = float(
        int(input("Please enter the first angle of the triangle: ")))
    angle_2 = float(
        int(input("Please enter the second angle of the triangle: ")))
    angle_3 = float(
        int(input("Please enter the third angle of the triangle: ")))

    sum = angle_1 + angle_2 + angle_3

    if sum == 180:
        print("The angles form a triangle!")
    else:
        print("The angles dont form a triangle!")
m()

def n():
    a = float(int(input("Please enter the length of side1: ")))
    b = float(int(input("Please enter the length of side2: ")))
    c = float(int(input("Please enter the length of side3: ")))
    if a + b > c or a + c > b or c + b > a:
        print("The sides form a triangle!")
    else:
        print("The sides dont form a triangle!")
n()

def o():
    year = int(input("Please enter the year: "))
    if(year % 4 == 0) and (year % 100 != 0):
        print(year, "is a leap year!")
    elif(year % 400 == 0) and (year % 100 == 0):
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year!")
o()

def p():
    phy = float(input("Please enter the physics marks out of 100: "))
    chem = float(input("Please enter the chem marks out of 100: "))
    maths = float(input("Please enter the maths marks out of 100: "))
    bio = float(input("Please enter the biology marks out of 100: "))

    percent = (phy + chem + maths + bio)/400 * 100
    if percent >= 90:
        print("You got an A grade!")
    elif percent >= 80:
        print("You got a B grade!")
    elif percent >= 70:
        print("You got a C grade!")
    elif percent >= 60:
        print("You got a D grade!")
    elif percent >= 40:
        print("You got an E grade!")
    else:
        print("You got a F grade!")
p()

def q():
    print("not done yet!")
q()

def r():
    print("not doen yet")
r()

def factoral():
    num = int(input("Please enter the number whos factoral you want: "))
    first_val = 1
    for i in range(1, num + 1):
        first_val = i * first_val
    print(first_val)
factoral()

def fibonacci():
    first_val = 0
    next_val = 1
    num_range = int(input("Please enter the range: "))
    for i in range(0, num_range):
        if i <= 1:
            result = i
        else:
            result = first_val + next_val
            first_val = next_val
            next_val = result
        print(result)
fibonacci()

def series():
    num_range = int(input("Please enter the range: "))
    print(1)
    for i in range(1, num_range):
        j = i + 1
        result = (j**2 - i)
        print(result)
series()
        
def num():
    number = int(input("Please enter a number: "))
    for i in range(1, number+1):
        sum = i + i + 2
        i = sum 
    print(sum)
num()

def tabel():
    num = int(input("Please enter the number whos table you would want: "))
    for i in range(1, 11):
        product = num * i
        print(num, "*", i, "=", product)
tabel()

def list():
    my_list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for i in my_list:
        if(i%5 == 0) and (i <= 150):
            print(i)
        elif i > 150:
            break
        else:
            pass
list()

def negative():
    for i in range(-10, 0):
        print(i)
negative()

def odd():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in my_list:
        if i%2 != 0:
            print(i)
        else:
            pass
odd()

def sum_series():
    range_num = int(input("Please enter a range: "))
    val = 2
    sec_val = "2"
    for i in range(1, range_num):
        sec_val = str(sec_val)
        series = sec_val + '2'
        series = int(series) 
        result = val + series
        val = result
        sec_val = series
    print(result)       
sum_series()

def a_pattern():
    school = ["s","c", "h", "o", "l"]
    for i in range(1, 6):
        for j in range(1, i+1):
            k = i - 1
            first = school[k]
            print(first, end="")
        print() 
a_pattern()

def b_pattern():
    for i in range(1,6):
        for j in range(1,i + 1):
            print("*", end="")
        print()
b_pattern()