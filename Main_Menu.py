# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import modules
import tkinter 
from tkinter import messagebox
# import class
from Register_Info_Class import register_info
# Create a Class for Main Menu
class main_menu:
    def __init__(self):
        # Create a Gui for Main Menu
        self.gui = tkinter.Tk()
        self.gui.title ("Covid-19 Contact Tracing")
        self.gui.geometry ("600x400")
        # Add Label
        title_label = tkinter.Label(self.gui, text="The Solution \n Let's End Covid As One!!", font=("Calibri", 14))
        title_label.pack(pady=20)               
# Add button
# Call class and run
# Run the Menu Class