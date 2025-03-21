# F.Rakin_Advanced_GUI_Calculator

import customtkinter as ctk
import math

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
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

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

button_degrees_to_radians = ctk.CTkButton(root, text="Degrees to Radians", command=convert_degrees_to_radians)
button_degrees_to_radians.grid(row=6, column=0, padx=10, pady=10)

button_radians_to_degrees = ctk.CTkButton(root, text="Radians to Degrees", command=convert_radians_to_degrees)
button_radians_to_degrees.grid(row=6, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()

