# F.Rakin_Advanced_GUI_Calculator

# Commit next time after cleaning up names before editing

import customtkinter as ctk
import math
from tkinter import messagebox


# Define the functions for each operation
def add() -> float: 
    """
    This function will be used to add numbers inputted
    """ 
    try:
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        result = number_1 + number_2

        label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def subtract():
    """
    This function will be used to subtract one number from another
    """
    try:
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        result = number_1 - number_2

        label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def multiply():
    """"
    This function will be used to multiply numbers
    """
    try:
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        result = number_1 * number_2

        label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    """
    This function will be used to divide numbers
    """
    try:
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        if number_2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

        else:
            result = number_1 / number_2
            label_result.configure(text=f"Result: {result:.4f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def square_root():
    """
    This function will be used to square root the first number selected by the user
    """
    try:
        number_1 = float(entry_number_1.get())

        if number_1 < 0:
            messagebox.showerror("Math Error", "Cannot take square root of negative number.")

        else:
            result = math.sqrt(number_1)
            label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def factorial():
    """
    This function will be used to find the factorial of the first number selected by the user
    """
    try:
        number_1 = float(entry_number_1.get())

        if number_1 < 0 or not number_1.is_integer():
            messagebox.showerror("Math Error", "Factorial is only defined for non-negative integers.")

        else:
            result = math.factorial(int(number_1))
            label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def absolute_value():
    """
    This function wu=ill display the absolute value of a number
    """  
    try:
        number_1 = float(entry_number_1.get())
        result = abs(number_1)

        label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def exponent():
    """"
    This function will be used to find the exponent of a number
    """
    try:
        number_1 = float(entry_number_1.get())
        number_2 = float(entry_number_2.get())

        result = number_1 ** number_2

        label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def convert_degrees_to_radians():
    """
    This function converts degrees to radians
    """
    try:
        number_1 = float(entry_number_1.get())
        result = math.radians(number_1)

        label_result.configure(text=f"Result (radians): {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def convert_radians_to_degrees():
    """
    This function converts radians to degrees
    """
    try:
        number_1 = float(entry_number_1.get())
        result = math.degrees(number_1)

        label_result.configure(text=f"Result (degrees): {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Create input fields for numbers
# Create the main window using CustomTkinter
ctk.set_appearance_mode("Dark")  # Set the appearance mode to "Dark"
ctk.set_default_color_theme("blue")  # You can change the color theme

root = ctk.CTk()  # Create a CustomTkinter window
root.geometry("480x400")
root.title("Advanced Calculator")

# Create input fields for numbers with your preferred names
label_number_1 = ctk.CTkLabel(root, text="Please enter the 1st number:")
label_number_1.grid(row=0, column=0, padx=10, pady=10)

entry_number_1 = ctk.CTkEntry(root)
entry_number_1.grid(row=0, column=1, padx=10, pady=10)

label_number_2 = ctk.CTkLabel(root, text="Please enter the 2nd number:")
label_number_2.grid(row=1, column=0, padx=10, pady=10)

entry_number_2 = ctk.CTkEntry(root)
entry_number_2.grid(row=1, column=1, padx=10, pady=10)

# Create result label
label_result = ctk.CTkLabel(root, text="Result: ", font=("Arial", 14))
label_result.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

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

# Start the main loop
root.mainloop()

