#Addition
def add(a, b):
    return a + b
#Subtraction
def subtract(a, b):
    return a - b
#Multiplication
def multiply(a, b):
    return a * b
#Division
def division(a, b):
    return a / b

#functions for the calculator

print("Welcome to Calculator")

#Loop Calculator Program
while True:
    try:
        #User selects what operation they want to do
        print("Select an Operation\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
        selection = float(input("Select 1,2,3, or 4 for Operation: "))
        #If they choose one of the options, then they will be allowed to enter the numbers
        if selection in (1, 2, 3, 4):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            #If they enter a value that is not applicable it will say invalid, and repeat entering numbers
            except ValueError:
                print("Invalid input, please try again.")
                continue
        if selection == (1):
                num3 = int(add(num1, num2))
                num4 = num3
                print("The answer is: " + str(num3))
        elif selection == (2):
            num3 = int(subtract(num1, num2))
            num4 = num3
            print("The answer is: " + str(num3))
        elif selection == (3):
            num3 = int(multiply(num1, num2))
            num4 = num3
            print("The answer is: " + str(num3))
        elif selection == (4):
            num3 = int(division(num1, num2))
            num4 = num3
            print("The answer is: " + str(num3))

        try:
            print("1)Continue\n2)Clear")
            selection2 = float(input("Select 1 or 2: "))
        except selection2 != 1:
            print("Invalid input, please try again.")
            continue
        except selection2 != 2:
            print("Invalid input, please try again.")
            continue
#So I have a bug here, i want it to loop where if I dont say 1 or 2 it'll say invalid input and go back to asking continue or clear?
#But right now it just goest back to the beginning, not sure what I did wrong here

        #All the if/elif statements made depending on what operation user chooses. I add another variable num4.
        #So if user wants to continue and use the calculated value to do another operation they can do that.
        #Gives option for user to continue with calculated value or clear the calculator for a new calculation
        try:
#This will loop the continue mode in the calculator if the user wants to calculate with the existing calulated value
                while selection2 == 1:
                    try:
                        print("Select an Operation\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
                        selection = float(input("Select 1,2,3, or 4 for Operation: "))
                        num1 = float(input("Enter number: "))
                    except ValueError:
                        print("Invalid input, please try again.")
                        continue
                    if selection == (1):
                        num3 = int(add(num4, num1))
                        num4 = num3
                        print("The answer is: " + str(num3))
                    elif selection == (2):
                        num3 = int(subtract(num4, num1))
                        num4 = num3
                        print("The answer is: " + str(num3))
                    elif selection == (3):
                        num3 = int(multiply(num4, num1))
                        num4 = num3
                        print("The answer is: " + str(num3))
                    elif selection == (4):
                        num3 = int(division(num4, num1))
                        num4 = num3
                        print("The answer is: " + str(num3))

                    print("1)Continue\n2)Clear")
                    selection2 = float(input("Select 1 or 2: "))
        except ValueError:
            print("Invalid input, please try again.")
            continue

    except ValueError:
        print("Invalid input, please try again.")
        continue

#Except ValueErrors are in there so if a letter is put in then itll say invalid input. What would be a way to be like if this does not equal
#1, 2, 3, 4.  I was thinking not ( ==), or x !=.
                        # except selection != 1, etc... :
                        #print("Invalid input, please try again.")
                        #continue
