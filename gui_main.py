# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import tkinter
import tkinter
from tkinter import ttk
# Create a gui window
gui = tkinter.Tk()
gui.title ("Covid-19 Contact Tracing")
# Add window size
gui.geometry ("600x400")
# Create a pack widgets
pad1 = tkinter.Frame(gui)
pad1.pack()
pad1_lable = tkinter.LabelFrame(pad1, text="Personal Information")
pad1_lable.grid (row=0, column=2)
# Add Entries and Labels For pad1
# First Name Entry and Label
fname_entry = tkinter.Entry(pad1_lable)
fname_entry.grid(row=1, column=0)
fname_label = tkinter.Label(pad1_lable, text="First Name")
fname_label.grid (row=0, column=0)
# Middle Name Entry and Label
mname_entry = tkinter.Entry(pad1_lable)
mname_entry.grid(row=1, column=1)
mname_label = tkinter.Label(pad1_lable, text="Middle Name")
mname_label.grid (row=0, column=1)
# Last Name Entry and Label
lname_entry = tkinter.Entry(pad1_lable)
lname_entry.grid(row=1, column=2)
lname_label = tkinter.Label(pad1_lable, text="Last Name")
lname_label.grid (row=0, column=2)
# Suffix Entry and Label
suffix_entry = ttk.Combobox(pad1_lable, values=["", "Jr.", "Sr.", "II", "III", "IV", "V"])
suffix_entry.grid(row=1, column=3)
suffix_label = tkinter.Label(pad1_lable, text="Suffix Name")
suffix_label.grid (row=0, column=3)
# House Number Entry and Label
housenum_entry = tkinter.Entry(pad1_lable)
housenum_entry.grid(row=4, column=0)
housenum_label = tkinter.Label(pad1_lable, text="House Number")
housenum_label.grid (row=3, column=0)
# Street Entry and Label
street_entry = tkinter.Entry(pad1_lable)
street_entry.grid(row=4, column=1)
street_label = tkinter.Label(pad1_lable, text="Street")
street_label.grid (row=3, column=1)
# Barangay Entry and Label
brgy_entry = tkinter.Entry(pad1_lable)
brgy_entry.grid(row=4, column=2)
brgy_label = tkinter.Label(pad1_lable, text="Barangay/Village")
brgy_label.grid (row=3, column=2)
# Municiplality Name Entry and Label
city_entry = tkinter.Entry(pad1_lable)
city_entry.grid(row=4, column=3)
city_label = tkinter.Label(pad1_lable, text="Municipality")
city_label.grid (row=3, column=3)
# Contact No. Entry and Label
contactnum_entry = tkinter.Entry(pad1_lable)
contactnum_entry.grid(row=6, column=1)
contactnum_label = tkinter.Label(pad1_lable, text="Contact No.")
contactnum_label.grid (row=5, column=1)
# Email Entry and Label
email_entry = tkinter.Entry(pad1_lable)
email_entry.grid(row=6, column=2)
email_label = tkinter.Label(pad1_lable, text="E-mail Address")
email_label.grid (row=5, column=2)

# Create a pack widgets
pad2 = tkinter.Frame(gui)
pad2.pack()
pad2_lable = tkinter.LabelFrame(pad2, text="Vaccination Details")
pad2_lable.grid (row=7, column=2)
# Add Entries and Labels For pad2
# Vaccine Status Entry and Label
vstatus_entry = ttk.Combobox(pad2_lable, values=["None", "1st Dose", "2nd Dose", "1st Booster", "2nd Booster"])
vstatus_entry.grid(row=9, column=0)
vstatus_label = tkinter.Label(pad2_lable, text="Vaccination Status")
vstatus_label.grid (row=8, column=0)
# Vaccine Type Entry and Label
vtype_entry = ttk.Combobox(pad2_lable, values=["None", "Pfizer", "Johnson & Johnson", "AstraZeneca", "Moderna", "Sinovac", "Sputnik"])
vtype_entry.grid(row=9, column=1)
vtype_label = tkinter.Label(pad2_lable, text="Type of Vaccine")
vtype_label.grid (row=8, column=1)
# Symptoms Entry and Label
symptoms_entry = ttk.Combobox(pad2_lable, values=["Fever", "Cough", "Loss of Smell", "Loss of Taste", "Body Pain", "None of the above"])
symptoms_entry.grid(row=9, column=2)
symptoms_label = tkinter.Label(pad2_lable, text="Symptoms in the past 7 Days")
symptoms_label.grid (row=8, column=2)
# Contact with Symptoms Entry and Label
contact_symp_entry = ttk.Combobox(pad2_lable, values=["Yes", "No"])
contact_symp_entry.grid(row=11, column=0)
contact_symp_label = tkinter.Label(pad2_lable, text="Do you had contact with \n someone with the Symptoms?")
contact_symp_label.grid (row=10, column=0)
gui.mainloop()
