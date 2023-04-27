import math
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
from PIL import Image, ImageTk

class Program:
    def __init__(self, master=tk.Tk):
        #Set up the window, create the widgets and set up some fonts and styles for the widgets
        self.master = master
        self.master.title("Quadratic equation solver")
        self.master.geometry("1080x720+420+180")
        self.master.iconbitmap("icon.ico")
        self.result_font = ("Roboto", 30, "bold")
        self.font = ("Roboto", 20, "bold")
        self.style = ttk.Style()
        self.style.configure("my.TButton", font=("Roboto", 20, "bold"))
        self.create_widgets()
    
    def create_widgets(self):
        """Create the widgets."""
        #a value
        self.a_label = tk.Label(self.master, text="x**2", font=self.font)
        self.a_label.place(relx=0.405, rely=0.05, anchor=tk.CENTER)
        self.a_entry = ttk.Entry(self.master, width=3, font=self.font, justify=tk.CENTER)
        self.a_entry.place(relx=0.35, rely=0.05, anchor=tk.CENTER)
        self.a_dropdown = ttk.Combobox(self.master, state="readonly", values=["+", "-"], width=2, font=self.font)
        self.a_dropdown.current(0)
        self.a_dropdown.place(relx=0.3, rely=0.05, anchor=tk.CENTER)

        #b value
        self.b_label = tk.Label(self.master, text="x", font=self.font)
        self.b_label.place(relx=0.5451, rely=0.05, anchor=tk.CENTER)
        self.b_entry = ttk.Entry(self.master, width=3, font=self.font, justify=tk.CENTER)
        self.b_entry.place(relx=0.51, rely=0.05, anchor=tk.CENTER)
        self.b_dropdown = ttk.Combobox(self.master, state="readonly", values=["+", "-"], width=2, font=self.font)
        self.b_dropdown.current(0)
        self.b_dropdown.place(relx=0.46, rely=0.05, anchor=tk.CENTER)

        #c value
        self.c_label = tk.Label(self.master, text=" = 0", font=self.font)
        self.c_label.place(relx=0.67, rely=0.05, anchor=tk.CENTER)
        self.c_entry = ttk.Entry(self.master, width=3, font=self.font, justify=tk.CENTER)
        self.c_entry.place(relx=0.63, rely=0.05, anchor=tk.CENTER)
        self.c_dropdown = ttk.Combobox(self.master, state="readonly", values=["+", "-"], width=2, font=self.font)
        self.c_dropdown.current(0)
        self.c_dropdown.place(relx=0.58, rely=0.05, anchor=tk.CENTER)

        #Button for calculating the results
        self.calculate_button = ttk.Button(self.master, text="Calculate x values", command=self.calculate, style="my.TButton")
        self.calculate_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #Label for showing the results
        self.result_var = tk.StringVar()
        self.result_var.set("x1 = ?, x2 = ?")
        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=self.result_font, relief=tk.SOLID, borderwidth=2, padx=10, pady=10)
        self.result_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        #Button for resetting the program
        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset, style="my.TButton")
        self.reset_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        #Button for showing the user what conditions need to meed in a quadratic equation in order for it to be valid
        self.conditions_button = ttk.Button(self.master, text="Quadratic equation conditions", command=self.show_conditions, style="my.TButton")
        self.conditions_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        #Button for showing the user the quadratic formula
        self.formula_button = ttk.Button(self.master, text="Show formula", command=self.show_formula, style="my.TButton")
        self.formula_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    
    def calculate(self):
        """Calculate the results."""
        #Except any errors
        try:
            #Set up the values and the discriminant
            a = int(self.a_dropdown.get() + self.a_entry.get())
            b = int(self.b_dropdown.get() + self.b_entry.get())
            c = int(self.c_dropdown.get() + self.c_entry.get())
            discriminant = b**2 - 4*a*c

            #Check if there's any zero
            if a == 0:
                msgbox.showerror(title="Error", message="The a value cannot be zero!")
                return
        
        #Check if all values are a number
        except ValueError:
            msgbox.showerror(title="Error", message="Please insert a valid integer.")
            return

        #If the discriminant is a negative value, tell the user there're no real solutions
        if discriminant < 0:
            self.result_var.set("No real solutions")
        
        #Else, calculate the results as normal
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)

            #Round the numbers
            if x1 == int(x1):
                x1 = int(x1)
            else:
                x1 = round(x1, 2)
            
            if x2 == int(x2):
                x2 = int(x2)
            else:
                x2 = round(x2, 2)
            
            #Display the results
            self.result_var.set(f"x1 = {x1}, x2 = {x2}")
    
    def reset(self):
        """Reset all entries, dropdowns and values."""
        #Reset entries
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)

        #Reset dropdowns
        self.a_dropdown.current(0)
        self.b_dropdown.current(0)
        self.c_dropdown.current(0)

        #Reset values
        self.result_var.set("x1 = ?, x2 = ?")
    
    def show_conditions(self):
        """Show the user what conditions does a quadratic equation need to meet in order for it to be valid."""
        #Create a variable for the message
        message = "To have a quadratic equation, the following conditions must be met:\n\n\n"
        message += "1. The equation must be in standart form for a quadratic equation: ax**2 + bx + c = 0, where a, b and c are constants and x is the variable.\n\n"
        message += "2. The coefficient a must not be zero, i.e. a ≠ 0. If a = 0, the equation is not quadratic, but rather linear.\n\n"
        message += "3. The equation must have real solutions. This means that the discriminant D of the equation (D = b^2 - 4ac) must be greater than or equal to zero, i.e. D ≥ 0. "
        message += "If the discriminant is negative, the equation has no real solutions and therefore is not valid in the set of real numbers."

        #Show the message
        msgbox.showinfo(title="Conditions for having a valid quadratic equation", message=message)
    
    def show_formula(self):
        """Show the user the quadratic formula."""
        #Create a new toplevel window
        toplevel_window = tk.Toplevel(self.master)

        #Label for the quadratic formula
        image = Image.open("formula.png")
        image = image.resize((800, 285))
        self.formula_image = ImageTk.PhotoImage(image)
        self.formula_label = tk.Label(toplevel_window, image=self.formula_image)
        self.formula_label.pack()

        #Create a button for closing the window
        self.ok_button = ttk.Button(toplevel_window, text="OK", command=toplevel_window.destroy)
        self.ok_button.pack()

#Start up the program
root = tk.Tk()
program = Program(master=root)
program.master.mainloop()