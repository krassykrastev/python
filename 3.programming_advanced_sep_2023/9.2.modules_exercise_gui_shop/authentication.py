import tkinter as tk
from canvas import app


def render_main_enter_screen():
    tk.Button(app, text="Login", bg="green", fg="white").grid(row=0, column=0)
    tk.Button(app, text="Register", bg="yellow", fg="black").grid(row=0, column=1)
