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
            num1 = float(input("Enter first number: "))
            continue_calculation = True
            while continue_calculation == True:
                print("Select an Operation\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division")
                selection = float(input("Select 1,2,3, or 4 for Operation: "))
                if selection in (1, 2, 3, 4):
                    try:
                        num2 = float(input("Enter second number: "))
                    except ValueError:
                        print("Invalid input, please try again.")
                        continue
                if selection == (1):
                    sum = int(add(num1, num2))
                    print("The answer is: " + str(sum))
                elif selection == (2):
                    sum = int(subtract(num1, num2))
                    print("The answer is: " + str(sum))
                elif selection == (3):
                    sum = int(multiply(num1, num2))
                    print("The answer is: " + str(sum))
                elif selection == (4):
                    sum = int(division(num1, num2))
                    print("The answer is: " + str(sum))

                try:
                    print("1)Continue\n2)Clear")
                    selection2 = float(input("Select 1 or 2: "))
                    if selection2 == 1:
                        continue_calculation = True
                        num1 = sum
                        continue
                    elif selection2 == 2:
                        continue_calculation = False
                        continue
                except ValueError:
                    print("Invalid input, please try again.")
                    continue

        except ValueError:
            print("Invalid input, please try again.")
            continue