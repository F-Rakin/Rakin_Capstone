# F.Rakin_Advanced_GUI_Calculator

import tkinter as tk

root= tk.Tk()
root.title('Advanced Calculator')
root.geometry("500x400")
root.configure(bg="darkgrey")

display_result = tk.Entry(root, width= 30, font= ("Arial", 20), bd=10, relief="sunken")
display_result.grid(column=0, row=0, columnspan=2)

button_text_list = []

button = tk.Button(root, text="1", width=8, font=("Arial", 20))
button.grid(column=1, row=1)
 
root.mainloop()

