# F.Rakin_Advanced_GUI_Calculator

# Import custom tkinter model for better UI
import customtkinter as ctk

# Import math library for complex calculations
import math

# Import pre made messagebox layout for error message popup
from tkinter import messagebox

# Define the functions for each operation
def add() -> float: 
    """
    This function will be used to add numbers inputted
    """ 
    try:
        # Store the 2 number inputs in variables from the entry field by using the "get" function
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        # Add the 2 numbers
        result = number_1 + number_2

        # Show the result in the result box
        label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def subtract() -> float:
    """
    This function will be used to subtract one number from another
    """
    try:
        # Store the 2 number inputs in variables from the entry field by using the "get" function
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        # Subtract the 2 numbers
        result = number_1 - number_2

        # Show the result in the result box
        label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def multiply() -> float:
    """"
    This function will be used to multiply numbers
    """
    try:
        # Store the 2 number inputs in variables from the entry field by using the "get" function
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        # Multiply the 2 numbers
        result = number_1 * number_2

        # Show the result in the result box
        label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def divide() -> float:
    """
    This function will be used to divide numbers
    """
    try:
        # Store the 2 number inputs in variables from the entry field by using the "get" function
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        # Check if the 2nd number is 0 or not
        if number_2 == 0:
            # If 2nd number is 0, show Math Error message in popup messagebox
            messagebox.showerror("Math Error", "Cannot divide by zero.")

        else:
            # Divide the 1st number by the 2nd number otherwise
            result = number_1 / number_2

        # Show the result in the result box
            label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def square_root() -> float:
    """
    This function will be used to square root the first number selected by the user
    """
    try:
        # Only store the first number entered into a variable
        number_1 = float(entry_number_1.get())

        # If the number is negative show Math error message in the popup messagebox
        if number_1 < 0:
            messagebox.showerror("Math Error", "Cannot take square root of negative number.")

        # Otherwise do the square root calculation and display the result
        else:
            result = math.sqrt(number_1)
            label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def factorial() -> float:
    """
    This function will be used to find the factorial of the first number selected by the user
    """
    try:
        # Only store the first number entered into a variable
        number_1 = float(entry_number_1.get())

        # Check if the input number is negative
        if number_1 < 0:

            # Show Math error message if number is negative
            messagebox.showerror("Math Error", "Factorial is only defined for non-negative integers.")

        # Check is the input number is an integer
        elif not number_1.is_integer(): 

            #  Show Math error message if the number is not an integer 
            messagebox.showerror("Math Error", "Factorial is only defined for integers.") 

        else:
            # Otherwise find the factorial of the number and display the result
            result = math.factorial(int(number_1))
            label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def absolute_value() -> float:
    """
    This function wu=ill display the absolute value of a number
    """  
    try:
        # Only store the first number entered into a variable
        number_1 = float(entry_number_1.get())

        # Find the absolute value of the number using the "abs" function
        result = abs(number_1)

        # Display the result
        label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def exponent() -> float:
    """"
    This function will be used to find the exponent of a number
    """
    try:
        # Store the 2 number inputs in variables from the entry field by using the "get" function
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        # Find the result when the 2nd number is an exponent of the 1st number
        result = number_1 ** number_2

        # Display the result
        label_result.configure(text=f"Result: {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def convert_degrees_to_radians() -> float:
    """
    This function converts degrees to radians
    """
    try:
        # Only store the first number entered into a variable
        number_1 = float(entry_number_1.get())

        # Find result when the number is converted to radians
        result = math.radians(number_1)

        # Display the result
        label_result.configure(text=f"Result (radians): {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def convert_radians_to_degrees() -> float:
    """
    This function converts radians to degrees
    """
    try:
        # Only store the first number entered into a variable
        number_1 = float(entry_number_1.get())

        # Find result when the number is converted to degrees
        result = math.degrees(number_1)

        # Display the result
        label_result.configure(text=f"Result (degrees): {result}")

    except ValueError:
        # Validation to check for invalid inputs
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def round_number():
    """
    This function rounds the result displayed to 4 decimal places.
    """
    try:
        # Retrieve the current result text from the label and strip "Result: " part

        # Store the current result in a variable as a string using the "cget" function
        result_text = label_result.cget("text")

        # Use the "split" function to split the string when ":" shows up in the string
        # Use the index value to access the number part of the string
        result_value = float(result_text.split(": ")[1]) 

        # Round the result to 4 decimal places
        rounded_result = round(result_value, 4)

        # Update the label with the rounded result
        label_result.configure(text=f"Result: {rounded_result}")

    except ValueError:
        # If the result text is not a valid number show an error message
        messagebox.showerror("Error", "No valid result to round.")
    

# Set the appearance mode to "Dark"
ctk.set_appearance_mode("Dark")  

# Set custom theme
ctk.set_default_color_theme("blue")  

# Create a CustomTkinter window
root = ctk.CTk()  
root.geometry("370x450")
root.title("Advanced Calculator")

# Create input fields for numbers
label_number_1 = ctk.CTkLabel(root, text="Please enter the 1st number:")
label_number_1.grid(row=0, column=0, padx=10, pady=10)

# Grid to enter the 1st number
entry_number_1 = ctk.CTkEntry(root)
entry_number_1.grid(row=0, column=1, padx=10, pady=10)

# Labeling grid to guide user
label_number_2 = ctk.CTkLabel(root, text="Please enter the 2nd number:")
label_number_2.grid(row=1, column=0, padx=10, pady=10)

# Grid to enter 2nd number
entry_number_2 = ctk.CTkEntry(root)
entry_number_2.grid(row=1, column=1, padx=10, pady=10)

# Create result label
label_result = ctk.CTkLabel(root, text="Result: ", font=("Arial", 18))
label_result.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Create buttons for operations
button_add = ctk.CTkButton(root, text="Add", command=add)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_subtract = ctk.CTkButton(root, text="Subtract", command=subtract)
button_subtract.grid(row=2, column=1, padx=10, pady=10)

button_multiply = ctk.CTkButton(root, text="Multiply", command=multiply)
button_multiply.grid(row=3, column=0, padx=10, pady=10)

button_divide = ctk.CTkButton(root, text="Divide", command=divide)
button_divide.grid(row=3, column=1, padx=10, pady=10)

button_square_root = ctk.CTkButton(root, text="Square Root", command=square_root)
button_square_root.grid(row=4, column=0, padx=10, pady=10)

button_factorial = ctk.CTkButton(root, text="Factorial", command=factorial)
button_factorial.grid(row=4, column=1, padx=10, pady=10)

button_absolute_value = ctk.CTkButton(root, text="Absolute Value", command=absolute_value)
button_absolute_value.grid(row=5, column=0, padx=10, pady=10)

button_exponent = ctk.CTkButton(root, text="Exponent", command=exponent)
button_exponent.grid(row=5, column=1, padx=10, pady=10)

button_degrees_to_radians = ctk.CTkButton(root, text="Degrees to Radians", command=convert_degrees_to_radians)
button_degrees_to_radians.grid(row=6, column=0, padx=10, pady=10)

button_radians_to_degrees = ctk.CTkButton(root, text="Radians to Degrees", command=convert_radians_to_degrees)
button_radians_to_degrees.grid(row=6, column=1, padx=10, pady=10)

# Add button to round the final result to 4 decimal place
button_round = ctk.CTkButton(root, text="Round", command=round_number)
button_round.grid(row=7, column=0, padx=10, pady=10)

# Start the main loop
root.mainloop()
