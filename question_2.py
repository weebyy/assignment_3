from calendar import month


class Q2:
    def a(self):
        num_day = int("Please enter the a number between 1 to 7: ")
        if num_day == 1:
            print("The day of the week to corresponding to the number you have entered is Sunday")
        elif num_day == 2:
            print("The day of the week to corresponding to the number you have entered is Monday")
        elif num_day == 3:
            print("The day of the week to corresponding to the number you have entered is Tuesday")
        elif num_day == 4:
            print("The day of the week to corresponding to the number you have entered is Wednesday")
        elif num_day == 5:
            print("The day of the week to corresponding to the number you have entered is Thursday")
        elif num_day == 6:
            print("The day of the week to corresponding to the number you have entered is Friday")
        elif num_day == 7:
            print("The day of the week to corresponding to the number you have entered is Saturday")
        else:
            print("You havent entered the correct number!")
    
    def b(self):
        month = input("Please enter the name of a month: ")
        month.islower()
        if month == "january" or "march" or "june" or "august" or "october" or "december":
            print("The month u have entered has 31 days")
        elif month == "febraury":
            print("The month you have entered has 28 days")
        else:
            print("The month you have entered has 30 days")
 
    def c(self):
        alpha = input("Please enter an alphabet: ")
        alpha.islower()
        if alpha == "a" or "e" or "i" or "o" or "u":
            print("The alphabet you entered is a vowel!")
        else:
            print("The alphabet entered is consonant!")
    
    def d(self):
        print("Not done yet!")
        
    def e(self):
        usr_input = input("Please enter something: ")
        if(usr_input.isalpha()):
            print("The character entered is an alphabet!")
        elif(usr_input.isdigit()):
            print("The character is a number!")
        else:
            print("The character entered is a speical character!")
    
    def f(self):
        usr_input = int(input("Please enter a number: "))
        if usr_input%2 == 0:
            print("The entered number is an even number!")
        else:
            print("The entered number is an odd number!")
            
    def g(self):
        usr_input = int(input("Please enter a number: "))
        if usr_input%8 == 0:
            print("The entered number is divisible by 8")
        else:
            print("The entered number is not divisible by 8!")
            
    def h(self):
        usr_input = int(input("Please enter an integer: "))
        if usr_input < 0:
            print("The enetred the number is a negative number!")
        elif usr_input == 0:
            print("The number is niether negative nor positive!")
        else:
            print("The number is a positive integer!")
            
    def i(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        
        if num1 < num2:
            print("num2 is greater than num1!")
        else:
            print("num1 is greater than num2")
            
    def j(self):
        age = int(input("Please enter your age: "))
        if age >= 18:
            print("You are eligible to vote!")
        else:
            print("You arent eligible to vote!")
            
    def k(self):
        print("not done yet!")
        
    def l(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        if num1%num2 == 0 or num2%num1 == 0:
            print("The numbers are divisable!")
        else:
            print("The enters arent divisable")
            
    