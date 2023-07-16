# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import tkinter
import tkinter
from tkinter import ttk
# Create a gui window
gui = tkinter.Tk()
gui.title ("Covid-19 Tracing")
# Add window size
gui.geometry ("600x400")
# Create a pack widgets
pad1 = tkinter.Frame(gui)
pad1.pack()
pad1_lable = tkinter.LabelFrame(pad1, text="Personal Information")
pad1_lable.grid (row=0, column=2)
# Add Entries
# Add Label
fname_entry = tkinter.Entry(pad1_lable)
fname_entry.grid(row=1, column=0)
fname_label = tkinter.Label(pad1_lable, text="First Name")
fname_label.grid (row=0, column=0)

mname_entry = tkinter.Entry(pad1_lable)
mname_entry.grid(row=1, column=1)
mname_label = tkinter.Label(pad1_lable, text="Middle Name")
mname_label.grid (row=0, column=1)

lname_entry = tkinter.Entry(pad1_lable)
lname_entry.grid(row=1, column=2)
lname_label = tkinter.Label(pad1_lable, text="Last Name")
lname_label.grid (row=0, column=2)

suffix_entry = ttk.Combobox(pad1_lable, values=["", "Jr.", "Sr.", "II", "III", "IV", "V"])
suffix_entry.grid(row=1, column=3)
suffix_label = tkinter.Label(pad1_lable, text="Suffix Name")
suffix_label.grid (row=0, column=3)

housenum_entry = tkinter.Entry(pad1_lable)
housenum_entry.grid(row=4, column=0)
housenum_label = tkinter.Label(pad1_lable, text="House Number")
housenum_label.grid (row=3, column=0)

street_entry = tkinter.Entry(pad1_lable)
street_entry.grid(row=4, column=1)
street_label = tkinter.Label(pad1_lable, text="Street")
street_label.grid (row=3, column=1)

brgy_entry = tkinter.Entry(pad1_lable)
brgy_entry.grid(row=4, column=2)
brgy_label = tkinter.Label(pad1_lable, text="Barangay/Village")
brgy_label.grid (row=3, column=2)

city_entry = tkinter.Entry(pad1_lable)
city_entry.grid(row=4, column=3)
city_label = tkinter.Label(pad1_lable, text="Municipality")
city_label.grid (row=3, column=3)

gui.mainloop()
