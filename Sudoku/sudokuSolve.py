import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def solve(event=None):
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = cells[i][j].get()
            if val == "":
                row.append(0)
            else:
                try:
                    row.append(int(val))
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers.")
                    return
        board.append(row)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(tk.END, str(board[i][j]))
    else:
        messagebox.showerror("No Solution", "No solution exists.")

def clear_board(event=None):
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)

def move(event):
    row, col = current_focus.get()
    if event.keysym == "Up" and row > 0:
        row -= 1
    elif event.keysym == "Down" and row < 8:
        row += 1
    elif event.keysym == "Left" and col > 0:
        col -= 1
    elif event.keysym == "Right" and col < 8:
        col += 1
    cells[row][col].focus_set()
    current_focus.set((row, col))

def on_focus(event, row, col):
    current_focus.set((row, col))
    highlight_cell(row, col)

def highlight_cell(row, col):
    for i in range(9):
        for j in range(9):
            bg_color = get_cell_color(i, j)
            cells[i][j].configure(bg=bg_color)
    cells[row][col].configure(bg=theme["highlight"])

def get_cell_color(i, j):
    block_color = theme["block1"] if (i // 3 + j // 3) % 2 == 0 else theme["block2"]
    return block_color

def toggle_theme():
    global theme
    theme = light_theme if theme == dark_theme else dark_theme
    root.configure(bg=theme["bg"])
    for i in range(9):
        for j in range(9):
            cells[i][j].configure(
                fg=theme["fg"],
                bg=get_cell_color(i, j),
                insertbackground=theme["fg"],
                font=(theme["font"], 18),
                highlightbackground=theme["grid"],
                highlightcolor=theme["grid"],
                highlightthickness=1,
            )
    solve_button.configure(bg=theme["button"], fg=theme["fg"], activebackground=theme["button"])
    clear_button.configure(bg=theme["button"], fg=theme["fg"], activebackground=theme["button"])
    toggle_button.configure(bg=theme["button"], fg=theme["fg"], activebackground=theme["button"])
    row, col = current_focus.get()
    highlight_cell(row, col)

# --- Themes ---
dark_theme = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "block1": "#2b2b2b",
    "block2": "#333333",
    "highlight": "#505050",
    "button": "#444444",
    "button_hover": "#666666",
    "grid": "#888888",
    "font": "Consolas"
}

light_theme = {
    "bg": "#fdf6e3",
    "fg": "#000000",
    "block1": "#f3f3e8",
    "block2": "#e8f3f1",
    "highlight": "#dddccc",
    "button": "#cccccc",
    "button_hover": "#dddddd",
    "grid": "#888888",
    "font": "Consolas"
}

theme = dark_theme  # start in dark mode

root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg=theme["bg"])

current_focus = tk.Variable(value=(0, 0))
cells = []

for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(root, width=3, font=(theme["font"], 18), justify="center",
                         bg=theme["block1"], fg=theme["fg"], insertbackground=theme["fg"],
                         relief="solid", bd=1,
                         highlightthickness=1, highlightbackground=theme["grid"])
        entry.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)
        entry.bind("<FocusIn>", lambda e, r=i, c=j: on_focus(e, r, c))
        row.append(entry)
    cells.append(row)

for i in range(9):
    root.grid_columnconfigure(i, weight=1, uniform="equal")
    root.grid_rowconfigure(i, weight=1, uniform="equal")

solve_button = tk.Button(root, text="Solve", font=("Arial", 14), command=solve,
                         bg=theme["button"], fg=theme["fg"], activebackground=theme["button_hover"])
solve_button.grid(row=10, column=0, columnspan=2, pady=10, padx=5)

clear_button = tk.Button(root, text="Start Over", font=("Arial", 14), command=clear_board,
                         bg=theme["button"], fg=theme["fg"], activebackground=theme["button_hover"])
clear_button.grid(row=10, column=3, columnspan=2, pady=10, padx=5)

toggle_button = tk.Button(root, text="Toggle Theme", font=("Arial", 14), command=toggle_theme,
                          bg=theme["button"], fg=theme["fg"], activebackground=theme["button_hover"])
toggle_button.grid(row=10, column=6, columnspan=3, pady=10, padx=5)

root.bind("<Return>", solve)
root.bind("<Command-r>", clear_board)
root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

highlight_cell(0, 0)

root.mainloop()
