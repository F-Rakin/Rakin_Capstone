#F.Rakin_Simple_Calculator

# Ask for user's name and greet them
def greeting() -> str :
    """
    This function asks the user's name and greets the user
    """
    name = input("What is your name? \n").title().strip()

    print(f"Hi {name}! Welcome to my Simple Calculator.") 



def add(number_1, number_2) -> float: 
    """
    This function will be used to add numbers inputted
    """ 
    addition = number_1 + number_2
    print(f"The result of addition is: {addition}")

    return addition


def subtract(number_1, number_2) -> float:
    """
    This function will be used to subtract one number from another
    """
    subtraction = number_1 - number_2
    print(f"The result of subtraction is: {subtraction}")

    return subtraction
    pass


def multiply(number_1, number_2) -> float:
    """"
    This function will be used to multiply numbers
    """
    multiplication = number_1 * number_2
    print(f"The result of multiplication is: {multiplication}")

    return multiplication
    pass


def divide(number_1, number_2) -> float:
    """
    This function will be used to divide numbers
    """
    division = round(number_1 / number_2, 4)
    print(f"The result of division is: {division}")

    return division
    pass


def calculation() -> float:
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


def use_again() -> str:
    """
    This function gives the user the choice to use the calculator again.
    """
    while True:

        # Ask if they want to use the calculator again, only accepting 'y' or 'n'
        choice = input("Do you wish to use the calculator again? [y/n] - ").strip().lower()

        # Run game function again if user chooses "y"
        if choice == "y":
            calculation()

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
    calculation()
    use_again()