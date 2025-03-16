import tkinter as tk

def add_to_Calculator():
    pass

def evaluate_calculation():
    pass

def clear_field():
    pass

root = tk.Tk()
root.geometry("600x550")

text_result = tk.Text(root, height= 2, width= 40, font= ("Arial", 20))
text_result.grid(columnspan=10)
root.mainloop()