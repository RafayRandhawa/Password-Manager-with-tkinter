from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip

OFF_WHITE = "#FFF5E1"
LIGHT_RED = "#FF6969"
RED = "#C80036"
DARK_BLUE = "#0C1844"
BLUE = "#4C3BCF"
ALL_BACKGROUND = OFF_WHITE
TEXT_COLOR = RED


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_letters = [random.choice(letters) for x in range(random.randint(8, 10))]
    password_list_symbols = [random.choice(symbols) for y in range(random.randint(2, 4))]
    password_list_numbers = [random.choice(numbers) for z in range(random.randint(2, 4))]
    password_list = password_list_numbers + password_list_symbols + password_list_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    with open(file="passwords.txt", mode="a") as file:
        website = website_text.get()
        email = email_text.get()
        password_ = password_text.get()
        if len(website) == 0 or len(password_) == 0:
            messagebox.showwarning(title="Warning", message="Please make sure no fields are empty")
        elif email == "123@abc,com":
            messagebox.showwarning(title="Warning", message="You forgot to enter your email")
        else:
            is_ok = messagebox.askokcancel(title="Confirm Data",
                                           message=f"Please check the details\nWebsite: {website}\nEmail: {email}\nPassword:{password_}\nIs this okay?")
            if is_ok:
                website_text.delete(0, END)
                password_text.delete(0, END)

                file.write(f"{website} | {email} | {password_}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50, bg=ALL_BACKGROUND)

password_logo_canvas = Canvas(height=200, width=200, highlightthickness=0, bg=ALL_BACKGROUND)
logo_image = PhotoImage(file="D:/Python/Password Manager/logo.png")
password_logo_canvas.create_image(100, 100, image=logo_image)
password_logo_canvas.grid(row=0, column=1)

#Labels

website_label = ttk.Label(window, text="Website:", background=ALL_BACKGROUND)
website_label.grid(row=1, column=0)

email_label = ttk.Label(window, text="Email/Username:", background=ALL_BACKGROUND)
email_label.grid(row=2, column=0)

password_label = ttk.Label(window, text="Password:", background=ALL_BACKGROUND)
password_label.grid(row=3, column=0)

#Entries

website_text = ttk.Entry(window, foreground=TEXT_COLOR)
website_text.config(width=52)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()


def on_entry_click(event):
    if email_text.get() == "123@abc.com":
        email_text.delete(0, END)


def on_focus_out(event):
    if email_text.get() == "":
        email_text.insert(0, "123@abc.com")


email_text = Entry(window, foreground=TEXT_COLOR)
email_text.insert(0, "123@abc.com")
email_text.bind('<FocusIn>', on_entry_click)
email_text.bind('<FocusOut>', on_focus_out)
email_text.config(width=52)
email_text.grid(row=2, column=1, columnspan=2)

password_text = ttk.Entry(window, foreground=TEXT_COLOR)
password_text.config(width=27)
password_text.grid(row=3, column=1)

#Buttons

generate_password_button = ttk.Button(window, text="Generate Password", width=24, cursor="hand1", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = ttk.Button(window, text="Add", width=52, cursor="hand1", command=add_password)
add_button.bind('<Enter>', )
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()