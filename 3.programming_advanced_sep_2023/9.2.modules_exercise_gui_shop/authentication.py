import tkinter as tk
import json
from canvas import app
from helpers import clean_screen
from products import render_products_screen


def register(**user):
    user.update({"products": []})
    with open("db/user_credentials_db.txt", "r+", newline="\n") as file:
        users = [line.strip().split(",")[0] for line in file]
        if user["username"] in users:
            render_register_screen(error="User already exists!")
            return
        file.write(f"{user['username']}, {user['password']}\n")

    with open("db/users.txt", "a", newline="\n") as file:
        file.write(json.dumps(user) + "\n")

    render_login_screen()


def login(username, password):
    with open("db/user_credentials_db.txt", "r") as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(", ")
            if username == name and password == pwd:
                with open("db/current_user.txt", "w") as f:
                    f.write(name)
                render_products_screen()
                return

    render_login_screen(error="Invalid username or password")


def render_login_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)

    if error is not None:
        tk.Label(app, text=error).grid(row=3, column=0)

    tk.Button(app, text="Enter", bg="green", fg="black", command=lambda: login(username.get(), password.get())).grid(row=2, column=0)


def render_register_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    if error is not None:
        tk.Label(app, text=error).grid(row=5, column=0)

    tk.Button(app, text="Enter", bg="green", fg="black", command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(), last_name=last_name.get())).grid(row=4, column=0)


def render_main_enter_screen():
    tk.Button(app, text="Login", bg="green", fg="white", command=render_login_screen).grid(row=0, column=0)
    tk.Button(app, text="Register", bg="yellow", fg="black", command=render_register_screen).grid(row=0, column=1)
