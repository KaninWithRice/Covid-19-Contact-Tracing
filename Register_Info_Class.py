# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import tkinter
import tkinter
from tkinter import ttk
from tkinter import messagebox
# Import Csv for data recording
import csv
# Create a Class
class register_info:
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


        # Create a pack widgets
        self.pad2 = tkinter.Frame(self.gui)
        self.pad2.pack()
        self.pad2_lable = tkinter.LabelFrame(self.pad2, text="Vaccination Details")
        self.pad2_lable.grid (row=7, column=2)
        # Add Entries and Labels For pad2
        # Vaccine Status Entry and Label
        self.vstatus_entry = ttk.Combobox(self.pad2_lable, values=["None", "1st Dose", "2nd Dose", "1st Booster", "2nd Booster"])
        self.vstatus_entry.grid(row=9, column=0)
        vstatus_label = tkinter.Label(self.pad2_lable, text="Vaccination Status")
        vstatus_label.grid (row=8, column=0)
        # Vaccine Type Entry and Label
        self.vtype_entry = ttk.Combobox(self.pad2_lable, values=["None", "Pfizer", "Johnson & Johnson", "AstraZeneca", "Moderna", "Sinovac", "Sputnik"])
        self.vtype_entry.grid(row=9, column=1)
        vtype_label = tkinter.Label(self.pad2_lable, text="Type of Vaccine")
        vtype_label.grid (row=8, column=1)
        # Symptoms Entry and Label
        self.symptoms_entry = ttk.Combobox(self.pad2_lable, values=["Fever", "Cough", "Loss of Smell", "Loss of Taste", "Body Pain", "None of the above"])
        self.symptoms_entry.grid(row=9, column=2)
        symptoms_label = tkinter.Label(self.pad2_lable, text="Symptoms in the past 7 Days")
        symptoms_label.grid (row=8, column=2)
        # Contact with Symptoms Entry and Label
        self.contact_symp_entry = ttk.Combobox(self.pad2_lable, values=["Yes", "No"])
        self.contact_symp_entry.grid(row=11, column=0)
        contact_symp_label = tkinter.Label(self.pad2_lable, text="Do you had contact with \n someone with the Symptoms?")
        contact_symp_label.grid (row=10, column=0)
        # Tested for Covid Entry and Label
        self.tested_entry = ttk.Combobox(self.pad2_lable, values=["Yes-Positive", "Yes-Negative", "No"])
        self.tested_entry.grid(row=11, column=1)
        tested_label = tkinter.Label(self.pad2_lable, text="Have you been tested for \n Covid-19 for the past 10 days?")
        tested_label.grid (row=10, column=1)
        # Travel Concern Entry and Label
        self.travel_entry = ttk.Combobox(self.pad2_lable, values=["Yes", "No"])
        self.travel_entry.grid(row=11, column=2)
        travel_label = tkinter.Label(self.pad2_lable, text="Have you Traveled International \n  for the past 14 days?")
        travel_label.grid (row=10, column=2)
        # Add a button
        self.reg_button = tkinter.Button(self.pad2, text="Register Information", command = self.register_entry)
        self.reg_button.grid(row=13, column=2, padx=20, pady=20)
    # Mainloop Function
    def mainloop(self):
        self.gui.mainloop()
    # Create a Register function
    def register_entry(self):
        first_name = self.fname_entry.get()
        middle_name =self.mname_entry.get()
        last_name = self.lname_entry.get()
        suffix = self.suffix_entry.get()
        housenum = self.housenum_entry.get()
        street = self.street_entry.get()
        bgry = self.brgy_entry.get()
        city = self.city_entry.get()
        age = self.age_entry.get()
        contactnum = self.contactnum_entry.get()
        email = self.email_entry.get()
        gender = self.gender_entry.get()
        vstatus = self.vstatus_entry.get()
        vtype = self.vtype_entry.get()
        symptoms = self.symptoms_entry.get()
        contact_symp = self.contact_symp_entry.get()
        tested = self.tested_entry.get()
        travel = self.travel_entry.get()
        # Add Error Input
        if not first_name or not middle_name or not last_name or not suffix or not housenum or not street or not bgry or not city or not age or not contactnum or not email or not gender or not vstatus or not vtype or not symptoms or not contact_symp or not tested or not travel:
            messagebox.showerror("ERROR << PLEASE FILL UP ALL INFORMATION >> ERROR")    
            return
        # Create Data Label and Entry Variable
        label = ["First Name", "Middle Name", "Last Name", "Suffix", "House Number", "Street", "Baranggay/Village", "City", "Age", "Contact No.", "Gender", "Vaccine Status", "Type of Vaccine", "Question 1", "Question 2", "Question 3", "Question 4"]
        regd_data = [first_name, middle_name, last_name, suffix, housenum, street, bgry, city, age, contactnum, email, gender, vstatus, vtype, symptoms, contact_symp, tested, travel]
        # Check if a csv file exists
        file_checker = False
        try:
            with open("Data_List.csv", "r") as List:
                read = csv.reader(List)
                if any(read):
                    file_checker = True
        except FileNotFoundError:
            pass
        # Write info to the csv file
        with open("Data_List.csv", "a", newline="") as List:
            write = csv.writer(List)
            if not file_checker:
                write.writerow(label)  # Write label 
            write.writerow(regd_data)  # Write current entry data
        # Show success message
        messagebox.showinfo("Data Registered", "Data Registered Successfully")
        # Close the window
        self.gui.destroy()
