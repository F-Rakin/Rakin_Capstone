#F.Rakin_Simple_Calculator

import math

# Ask for user's name and greet them
def greeting() -> str :
    """
    This function asks the user's name and greets the user
    """
    name = input("What is your name? \n").title().strip()

    print(f"Hi {name}! Welcome to my Simple Calculator.") 


def add(number_1: float, number_2: float) -> float: 
    """
    This function will be used to add numbers inputted
    """ 
    addition = number_1 + number_2
    print(f"The result of addition is: {addition}")

    return addition


def subtract(number_1: float, number_2: float) -> float:
    """
    This function will be used to subtract one number from another
    """
    subtraction = number_1 - number_2
    print(f"The result of subtraction is: {subtraction}")

    return subtraction


def multiply(number_1: float, number_2: float) -> float:
    """"
    This function will be used to multiply numbers
    """
    multiplication = number_1 * number_2
    print(f"The result of multiplication is: {multiplication}")

    return multiplication


def divide(number_1: float, number_2: float) -> float:
    """
    This function will be used to divide numbers
    """
    division = round(number_1 / number_2, 4)
    print(f"The result of division is: {division}")

    return division


def exponent(number_1: float, number_2: float) -> float:
    """
    This function will give the result when number_2 is an exponent of number_1
    """
    exponent_number = number_1 ** number_2
    print(f"The result is: {exponent_number}")

    return exponent_number   


def square_root(number_1: float) -> float:
    """
    This function will be used to square root the first number selected by the user
    """
    square_rooted_number = math.sqrt(number_1)
    print(f"The square rooted number is: {square_rooted_number}")

    return square_rooted_number    
      
        
def calculate(operation: int) -> float:
    """
    This function asks user to input numbers and calls functions based on the operation selected to do the calculation

    :return: The 2 input numbers
    """
    while True:
        try:  

            number_1 = float(input("Please enter the 1st number: "))
            number_2 = float(input("Please enter the 2nd number: "))

            if operation == 1:
                add(number_1, number_2)
                break

            elif operation == 2:
                subtract(number_1, number_2)
                break

            elif operation == 3:
                multiply(number_1, number_2)
                break

            elif operation == 4:
                divide(number_1, number_2)
                break

            elif operation == 5:
                exponent(number_1, number_2)

            elif operation == 6:
                square_root(number_1)
                break

            else: 
                print("This is not a valid option! ")
                break

        except ValueError:
            print("Please enter a valid operation integer! \n")

            return number_1, number_2


def get_operation() -> float:
    """
    This function asks the user for the operation they want to do. 
    Runs the calculation function if valid operation is selected.

    :return: Operation input
    """
    while True: 
        try:    
            print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division (1st number/2nd number) \n 5. Exponent \n 6. Square Root (2nd number does not matter) \n")

            operation = int(input("Please enter your choice of operation [1/2/3/4/5/6]: "))
                
            if operation < 1:
                print("This is not a valid option! ")
                continue

            elif operation > 6:
                print("This is not a valid option! ")
                continue

            else: 
                calculate(operation)
                break

        except ValueError:
            print("Please enter a valid operation integer! \n")

    return operation


def use_again() -> str:
    """
    This function gives the user the choice to use the calculator again.
    """
    while True:

        # Ask if they want to use the calculator again, only accepting 'y' or 'n'
        choice = input("Do you wish to use the calculator again? [y/n] - ").strip().lower()

        # Run game function again if user chooses "y"
        if choice == "y":
            get_operation()

        # End the game if user chooses "n"    
        elif choice == "n":
            break

        # Tell user to choose only between "y/n"
        else:
            print("Please enter y/n ") 


# Call the function to run the game
# Can be used to import the main function and run in a different file
if __name__ == "__main__": 
    greeting()
    get_operation()
    use_again()
