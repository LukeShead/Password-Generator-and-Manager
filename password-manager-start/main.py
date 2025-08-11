from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    #

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    #
    gen_password = ""
    for char in password_list:
        gen_password += char

    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    web = web_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    new_data = {web: {
            "email": email_user,
            "password": password,
        }
    }
    if web == "" or password == "":
        messagebox.showerror(title="Missing information", message="You do not have the required information.")
        return

    yes_or_no = messagebox.askokcancel(title=web, message=f"These are the details entered:\n Email: {email_user},\n Password: {password}")

    if yes_or_no:
        with open("SavedPasswords.json", "r") as data_file:
            #json.dump(new_data, data_file, indent=4)
            data = json.load(data_file)
            data.update(new_data)

            password_entry.delete(0, END)
            web_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx= 50, pady= 50, background="grey")
canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_txt = Label(text="Website:")
website_txt.grid(column=0, row=1)

mail_user_txt = Label(text="Email/Username:")
mail_user_txt.grid(column=0, row=2)

password_txt = Label(text="Password:")
password_txt.grid(column=0, row=3)

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_entry.insert(0, "lukemshead+___@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

gen_butt = Button(text="Generate Password", command=gen_password)
gen_butt.grid(column=2, row= 3, sticky="EW")

add_butt = Button(text="Add", width=36, command=add_password)
add_butt.grid(column=1, row=4, columnspan=2, sticky="EW")
window.mainloop()