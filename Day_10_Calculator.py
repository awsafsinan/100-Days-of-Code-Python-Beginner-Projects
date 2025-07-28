import os
def clear_screen():
    os.system('cls')

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return float(n1 + n2)
def subtract(n1, n2):
    return float(n1 - n2)
def multiply(n1, n2):
    return float(n1 * n2)
def divide(n1, n2):
    return float (n1 / n2)

operations = {"+": add,
               "-": subtract,
               "*": multiply,
              "/": divide,
}

def calculator():
    print(logo)

    first_number = float(input("Enter first number: "))

    more_calculation = True

    while more_calculation:
        for key in operations:
            print(key)

        sign = input("Pick an operation: ")

        second_number = float(input("Enter the new number: "))
        recent_result = 0

        for key in operations:
            if key == sign:
                recent_result = operations[key](first_number, second_number)
                print(f"{first_number} {sign} {second_number} = {recent_result}")

        print(f"Type 'y' to continue calculating with {recent_result}, or type 'n' to start a new calculation: ")
        continue_with_recent_result = input()
        if continue_with_recent_result == "y":
            first_number = recent_result
        else:
            more_calculation = False
            clear_screen()
            calculator()

calculator()