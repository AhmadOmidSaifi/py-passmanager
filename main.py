from dataclasses import dataclass
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

FONT_NAME = ("Courier", 8, "bold")


# ------------------------------PASSWORD GENERATOR-----------------------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '8', '7', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_number + password_letter + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ------------------------------SAVE PASSWORD----------------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields emty!!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Reading the data
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # save the data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------------- SEARCH MECANISM --------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No Data File Found!!")
    else:
        if (website in data):
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="error", message=f"There is no detail for {website} exists.")
# ------------------------------UI SETUP----------------------------------#
window = Tk()
window.title("PassWord Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=198, height=298)

lock_image = PhotoImage(file="lock.PNG")
canvas.create_image(99, 149, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=(FONT_NAME, 20, "bold"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username: ", font=(FONT_NAME, 20, "bold"))
email_label.grid(row=2, column=0)

email_entry = Entry(width=55)
email_entry.insert(0, "osaifi359@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", font=(FONT_NAME, 20, "bold"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
