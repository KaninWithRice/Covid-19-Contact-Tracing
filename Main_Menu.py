# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import modules
import tkinter 
from tkinter import messagebox
# import class
from Register_Info_Class import register_info
from Search_Engine_Class import search_info
# Create a Class for Main Menu
class main_menu:
    def __init__(self):
        # Create a Gui for Main Menu
        self.gui = tkinter.Tk()
        self.gui.title ("Covid-19 Contact Tracing")
        self.gui.geometry ("600x400")
        self.gui["background"] = "grey"
        # Add Label
        title_label = tkinter.Label(self.gui, text="COVID-19 TRACE PH", fg="white" , bg="grey", font=("Times New Roman", 30))
        title_label.pack(pady=60)               
        # Add Register Option Button
        register_button = tkinter.Button(self.gui, text="Register", bg="white", fg="black", command=self.open_register, width=30)
        register_button.pack(pady=10)
        # Add Search Option Button
        self.search = tkinter.Button(self.gui, text="Search", bg="white", fg="black", command=self.open_search_engine, width=30)
        self.search.pack(pady=10)
    # Call register class and run
    def open_register(self):
        register_gui = register_info()
        register_gui.mainloop()
    # Call search class and run
    def open_search_engine(Self):
        search_gui = search_info()
        search_gui.mainloop()        
    # Create a mainloop
    def run(self):
        self.gui.mainloop()
# Run the Menu Class
start = main_menu()
start.run()
# Done