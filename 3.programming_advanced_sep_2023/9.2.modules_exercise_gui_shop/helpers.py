from canvas import app


def clean_screen():
    for el in app.grid_slaves():
        el.destroy()