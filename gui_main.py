# Mohammad Mishal S. Noroña | BSCPE 1-5 | Contact Tracing
# Import tkinter
import tkinter

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
gui.mainloop()
