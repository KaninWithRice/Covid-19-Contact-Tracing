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
# Add Entries
fname_entry = tkinter.Entry(pad1)
fname_entry.grid(row=1, column=0)

mname_entry = tkinter.Entry(pad1)
mname_entry.grid(row=1, column=1)

lname_entry = tkinter.Entry(pad1)
lname_entry.grid(row=1, column=2)

suffix_entry = ttk.Combobox(pad1, values=["", "Jr.", "Sr.", "II", "III", "IV", "V"])
suffix_entry.grid(row=1, column=3)
gui.mainloop()
