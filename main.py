# F.Rakin_Advanced_GUI_Calculator

import tkinter as tk
import math
import tkinter.messagebox

root= tk.Tk()
root.title('Advanced Calculator')
root.geometry("480x400")
root.configure(bg="darkgrey")


# Create input fields for numbers
label_num1 = tk.Label(root, text="Enter 1st Number:", font=("Arial", 16))
label_num1.grid(row=2, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=2, column=1)

label_num2 = tk.Label(root, text="Enter 2nd Number:", font=("Arial", 16))
label_num2.grid(row=3, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=3, column=1)

# Create result label
label_result = tk.Entry(root, width= 30, font= ("Arial", 20), bd=10, relief="sunken")
label_result.grid(row=0, column=0, columnspan=2)


# Start the main loop
root.mainloop()

