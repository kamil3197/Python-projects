from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady = 50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row = 0)
empty_list=[]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    password = ''.join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get()
    mail = email_input.get()
    password = pass_input.get()
    new_data = {web: {"email": mail,
                      "password": password,
                      }
                }
    #checking if website and password are provided
    if len(web) > 2 and len(password) > 2:
        pop_up = messagebox.askokcancel(title='Success', message='Credentials saved')
    else:
        messagebox.showinfo(title='Wrong', message='Provide correct credentials')

    if pop_up:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
#------------------------------SEARCH CREDENTIALS----------------------#
def find_password():
    web = web_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error404', message='You have not provided any credentials yet')
    else:
        if web in data:
            messagebox.showinfo(title='Credentials', message=data[web])
        else:
            messagebox.showinfo(title='Error', message='No details for this website')

# ---------------------------- UI SETUP ------------------------------- #
#TITLES
title_web = Label(text='Website:')
title_web.grid(column=0, row=1)

title_email = Label(text='Email/Username:')
title_email.grid(column=0, row = 2)

title_pass = Label(text='Password:')
title_pass.grid(column = 0, row = 3)

#INPUTS
web_input = Entry(width = 21)
web_input.grid(column = 1, row = 1)
web_input.focus()

email_input = Entry(width = 35)
email_input.grid(column = 1, row = 2, columnspan=2)
email_input.insert(0, 'kamil31@ymail.com')

pass_input = Entry(width = 21)
pass_input.grid(column = 1, row = 3)


#BUTTONS
pass_button = Button(text='Generate Password', width=23, command=password_generator)
pass_button.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=23, command=find_password)
search_button.grid(column=2, row =1, columnspan=2)

window.mainloop()
