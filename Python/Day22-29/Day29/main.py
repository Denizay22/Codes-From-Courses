from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import sample, randint


# TODO
# save credentials to csv format
# add a in app table to see saved credentials

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    alphabet = ascii_lowercase + ascii_uppercase + digits + punctuation
    password_length = randint(15, 25)
    password_list = sample(alphabet, password_length)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any of the credential boxes empty!")
        return
    user_choice = messagebox.askokcancel(title=website, message=f"These are your credentials:\nWebsite: {website}\n"
                                                                f"Email: {email}\nPassword: {password}.\n"
                                                                f"Do you want to save these credentials?")
    if user_choice:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website},{email},{password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=40, pady=40)
window.title("Password MANAGER")
window.minsize(240, 240)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Mail/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(text="Generate Password", command=create_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=save_info)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
