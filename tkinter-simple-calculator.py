#F.Rakin_Tkinter_Calculator

# Simple calculator with gui using a YT tutorial

import tkinter as tk

# Start with an empty string
calculation = " "

def add_to_Calculator(symbol: str) -> str:
    """
    Function to add string to the calculation 
    """
    # Have calculation as a global variable to manipulate it inside function
    global calculation

    # Add symbols typecasted as string to the calculation
    calculation += str(symbol)

    # Display input in the text grid 
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    
    

def evaluate_calculation() -> str:
    """
    Function to evaluate the calculation string
    """
    # Have calculation as a global variable to manipulate it inside function
    global calculation

    # Validate for Math errors
    try:
        # Use the evaluate function to calculate the "Calculation" string
        calculation = str(eval(calculation))

        # Display the result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except: 
        # Clear the string if math error occurs
        clear_field()
        text_result.insert(1.0, "Error")
    
    

def clear_field() -> str:
    """
    Function to clear the interface
    """
    # Have calculation as a global variable to manipulate it inside function
    global calculation

    # Clear the calculation stirng
    calculation = ""
    text_result.delete(1.0, "end")
    

# Root window or interface
root = tk.Tk()

# Add a title to the GUI
root.title("Simple GUI Calculator")

# Shape of the interface
root.geometry("550x300")

# Add a text input grid
text_result = tk.Text(root, height= 2, width= 40, font= ("Arial", 20))
text_result.grid(columnspan=10)

# Add buttons and commands

# Number buttons. Use lambda to send arguements to the functions instead of calling it immediately
btn_1 = tk.Button(root, text="1", command=lambda: add_to_Calculator(1), width=8, font=("Arial", 18))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_Calculator(2), width=8, font=("Arial", 18))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_Calculator(3), width=8, font=("Arial", 18))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_Calculator(4), width=8, font=("Arial", 18))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_Calculator(5), width=8, font=("Arial", 18))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_Calculator(6), width=8, font=("Arial", 18))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_Calculator(7), width=8, font=("Arial", 18))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_Calculator(8), width=8, font=("Arial", 18))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_Calculator(9), width=8, font=("Arial", 18))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_Calculator(0), width=8, font=("Arial", 18))
btn_0.grid(row=5, column=2)

# Symbol/Function buttons

btn_add = tk.Button(root, text="+", command=lambda: add_to_Calculator("+"), width=8, font=("Arial", 18))
btn_add.grid(row=2, column=4)

btn_subtract = tk.Button(root, text="-", command=lambda: add_to_Calculator("-"), width=8, font=("Arial", 18))
btn_subtract.grid(row=3, column=4)

btn_multiply = tk.Button(root, text="x", command=lambda: add_to_Calculator("*"), width=8, font=("Arial", 18))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(root, text="÷", command=lambda: add_to_Calculator("/"), width=8, font=("Arial", 18))
btn_divide.grid(row=5, column=4)

# Parentheses buttons

btn_open = tk.Button(root, text="(", command=lambda: add_to_Calculator("("), width=8, font=("Arial", 18))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_Calculator(")"), width=8, font=("Arial", 18))
btn_close.grid(row=5, column=3)

# Equal and clear buttons 
# Greater columnspan to reduce empty space in the GUI
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=16, font=("Arial", 18))
btn_equals.grid(row=6, column=1, columnspan= 2)

btn_clear = tk.Button(root, text="clear", command=clear_field, width=16, font=("Arial", 18))
btn_clear.grid(row=6, column=3, columnspan=2)


# Main loop of the interface
root.mainloop()