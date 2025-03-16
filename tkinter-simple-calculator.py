import tkinter as tk

calculation = " "

def add_to_Calculator(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    
    pass

def evaluate_calculation() :
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except: 
        clear_field()
        text_result.insert(1.0, "Error")
    
    pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1,0, "end")
    pass

root = tk.Tk()
root.geometry("600x550")

text_result = tk.Text(root, height= 2, width= 40, font= ("Arial", 20))
text_result.grid(columnspan=10)
root.mainloop()