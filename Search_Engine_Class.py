# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import modules
import tkinter 
from tkinter import ttk
from tkinter import messagebox
import csv
# Create a class
class search_info:
    def __init__(self):
        # Create a gui window
        self.gui = tkinter.Tk()
        self.gui.title ("Covid-19 Contact Tracing")
        # Add window size
        self.gui.geometry ("600x400")
        # Create a pack widgets
        self.pad1 = tkinter.Frame(self.gui)
        self.pad1.pack()
        self.pad1_lable = tkinter.LabelFrame(self.pad1, text="Personal Information")
        self.pad1_lable.grid (row=0, column=2, padx=15, pady=15)
        # Add Entries and Labels For pad1
        # First Name Entry and Label
        self.fname_entry = tkinter.Entry(self.pad1_lable)
        self.fname_entry.grid(row=1, column=0)
        fname_label = tkinter.Label(self.pad1_lable, text="First Name")
        fname_label.grid (row=0, column=0)
        # Middle Name Entry and Label
        self.mname_entry = tkinter.Entry(self.pad1_lable)
        self.mname_entry.grid(row=1, column=1)
        mname_label = tkinter.Label(self.pad1_lable, text="Middle Name")
        mname_label.grid (row=0, column=1)
        # Last Name Entry and Label
        self.lname_entry = tkinter.Entry(self.pad1_lable)
        self.lname_entry.grid(row=1, column=2)
        lname_label = tkinter.Label(self.pad1_lable, text="Last Name")
        lname_label.grid (row=0, column=2)
        # Suffix Entry and Label
        self.suffix_entry = ttk.Combobox(self.pad1_lable, values=["N/A", "Jr.", "Sr.", "II", "III", "IV", "V"])
        self.suffix_entry.grid(row=1, column=3)
        suffix_label = tkinter.Label(self.pad1_lable, text="Suffix Name")
        suffix_label.grid (row=0, column=3)
        # House Number Entry and Label
        self.housenum_entry = tkinter.Entry(self.pad1_lable)
        self.housenum_entry.grid(row=4, column=0)
        housenum_label = tkinter.Label(self.pad1_lable, text="House Number")
        housenum_label.grid (row=3, column=0)
        # Street Entry and Label
        self.street_entry = tkinter.Entry(self.pad1_lable)
        self.street_entry.grid(row=4, column=1)
        street_label = tkinter.Label(self.pad1_lable, text="Street")
        street_label.grid (row=3, column=1)
        # Barangay Entry and Label
        self.brgy_entry = tkinter.Entry(self.pad1_lable)
        self.brgy_entry.grid(row=4, column=2)
        brgy_label = tkinter.Label(self.pad1_lable, text="Barangay/Village")
        brgy_label.grid (row=3, column=2)
        # Municiplality Name Entry and Label
        self.city_entry = tkinter.Entry(self.pad1_lable)
        self.city_entry.grid(row=4, column=3)
        city_label = tkinter.Label(self.pad1_lable, text="Municipality")
        city_label.grid (row=3, column=3)
        # Age Entry and Label
        self.age_entry = tkinter.Scale(self.pad1_lable, from_=1, to=100, orient="horizontal")
        self.age_entry.grid(row=6, column=0)
        age_label = tkinter.Label(self.pad1_lable, text="Age")
        age_label.grid (row=5, column=0)
        # Contact No. Entry and Label
        self.contactnum_entry = tkinter.Entry(self.pad1_lable)
        self.contactnum_entry.grid(row=6, column=1)
        contactnum_label = tkinter.Label(self.pad1_lable, text="Contact No.")
        contactnum_label.grid (row=5, column=1)
        # Email Entry and Label
        self.email_entry = tkinter.Entry(self.pad1_lable)
        self.email_entry.grid(row=6, column=2)
        email_label = tkinter.Label(self.pad1_lable, text="E-mail Address")
        email_label.grid (row=5, column=2)
        # Gender Entry and Label
        self.gender_entry = ttk.Combobox(self.pad1_lable, values=["Male", "Female", "Transgender Male", "Transgender Female", "Non-Binary", "Bigender", "Genderqueer", "Other", "Prefer not to say"])
        self.gender_entry.grid(row=6, column=3)
        gender_label = tkinter.Label(self.pad1_lable, text="Gender")
        gender_label.grid (row=5, column=3)
        # Add a Search Button
        self.search = tkinter.Button(self.pad1, text="Search", command=self.search_engine)
        self.search.grid(row=13, column=2, padx=20, pady=20)
   
    # Mainloop Function
    def mainloop(self):
        self.gui.mainloop()

    # Search Function
    def search_engine(self):
    # Create an Object for the variables
        search_value = None
    # Determine the search value
        if self.fname_entry.get():
            search_value = self.fname_entry.get().lower()
        elif self.mname_entry.get():
            search_value = self.mname_entry.get().lower()
        elif self.lname_entry.get():
            search_value = self.lname_entry.get().lower()
        elif self.suffix_entry.get():
            search_value = self.suffix_entry.get().lower()
        elif self.housenum_entry.get():
            search_value = self.housenum_entry.get().lower()
        elif self.street_entry.get():
            search_value = self.street_entry.get().lower()
        elif self.brgy_entry.get():
            search_value = self.brgy_entry.get().lower()
        elif self.city_entry.get():
            search_value = self.city_entry.get().lower()
        elif self.age_entry.get():
            search_value = self.age_entry.get()
        elif self.contactnum_entry.get():
            search_value = self.contactnum_entry.get().lower()
        elif self.email_entry.get():
            search_value = self.email_entry.get().lower()
        elif self.gender_entry.get():
            search_value = self.gender_entry.get().lower()
    # Check if search value is entered
    # Create a Temp Storage
    # Read csv file
    # Check each criteria 
    # Show Result
    # Add message box if entry not found or found