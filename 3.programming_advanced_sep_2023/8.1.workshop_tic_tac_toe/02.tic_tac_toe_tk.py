import tkinter as tk

app_config = {
    'board': [[None] * 3 for _ in range(3)],
    'buttons': [[None] * 3 for _ in range(3)],
    'sign': 'X',
    'X': None,
    '0': None
}


def render_board(window):
    grid_frame = tk.Frame(master=window)
    grid_frame.pack(padx=10, pady=10)
    for row in range(3):
        for col in range(3):
            app_config['buttons'][row][col] = tk.Button(
                master=grid_frame,
                text=' '
            )


def start_game(window, player_one, player_two):
    window.destroy()
    window = tk.Tk()
    window.geometry('240x240')
    window.title('Tic Tac Toe')

    render_board(window)


def start_screen():
    window = tk.Tk()
    window.geometry('240x240')
    window.title('Tic Tac Toe')

    tk.Label(window, text="First player name: ").pack()
    player_one = tk.Entry(window)
    player_one.pack()

    tk.Label(window, text="Second player name: ").pack()
    player_two = tk.Entry(window)
    player_two.pack()

    tk.Button(window, text='Start game', command=lambda: start_game(window, player_one, player_two)).pack()

    window.mainloop()


if __name__ == '__main__':
    start_screen()
