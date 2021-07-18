from tkinter import *


def calc_button():
    my_Label3.config(text=str(int(my_entry.get()) * 1.6))


window = Tk()
window.title("Test")
window.minsize(150, 100)
window.config(padx=20, pady=20)

my_entry = Entry()
my_entry.config(width=10)
my_entry.grid(column=1, row=0)

my_Label1 = Label(text="Miles", padx=5)
my_Label1.grid(column=2, row=0)
my_Label2 = Label(text="is equal to")
my_Label2.grid(column=0, row=1)
my_Label3 = Label(text="0")
my_Label3.grid(column=1, row=1)
my_Label4 = Label(text="Km", padx=5)
my_Label4.grid(column=2, row=1)

my_button = Button(text="Calculate", command=calc_button)
my_button.grid(column=1, row=2)
window.mainloop()
