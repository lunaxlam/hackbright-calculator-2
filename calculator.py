"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:

    token = input("Enter an equation > ").split(" ")

    if "q" in token:
        break
    elif len(token) < 3:
        print("Not enough arguments.")
    elif len(token) > 3:
        print("Too many arguments!")
    else:

        operator = token[0]
        num1 = token[1]
        num2 = token[2]
        
        if num1.isdigit() and num2.isdigit():

            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                print(add(num1, num2))
            elif operator == "-":
                print(subtract(num1, num2))
            elif operator == "*":
                print(multiply(num1, num2))
            elif operator == "/":
                print(divide(num1, num2))
            elif operator == "square":
                print(square(num1, num2))
            elif operator == "cube":
                print(cube(num1, num2))
            elif operator == "power":
                print(power(num1, num2))   
            elif operator == "mod":
                print(mod(num1, num2))                             
            else:
                print("Operator does not exist. Try again. ")
        else:
            print("Those are not numbers. Try again.")