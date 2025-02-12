"""Faizan A. Rakin"""

print("Welcome to Calculator!")

# Call functions every time a button is pressed on my GUI

def add(number_1, number_2): 
    """
    This function will be used to add numbers inputted
    """ 
    addition = number_1 + number_2
    print(f"The result of addition is: {addition}")

    return addition

def subtract(number_1, number_2):
    """
    This function will be used to subtract one number from another
    """
    subtraction = number_1 - number_2
    print(f"The result of subtraction is: {subtraction}")

    return subtraction
    pass

def multiply(number_1, number_2):
    """"
    This function will be used to multiply numbers
    """
    multiplication = number_1 * number_2
    print(f"The result of multiplication is: {multiplication}")

    return multiplication
    pass

def divide(number_1, number_2):
    """
    This function will be used to divide numbers
    """
    division = number_1 / number_2
    print(f"The result of division is: {division}")

    return division
    pass


def calculation():
    """
    This function will do the calculation by calling other functions and display results
    """

    while True:
        try:
            number_1 = float(input("Please enter the 1st number: "))
            number_2 = float(input("Please enter the 2nd number: "))

            print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
            operation = int(input("Please enter your choice of operation [1/2/3/4]: "))

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

            break
        except ValueError:
            print("Please enter valid numbers")

    return number_1, number_2


    
calculation()