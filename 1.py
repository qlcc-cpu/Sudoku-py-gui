import tkinter as tk
from tkinter import messagebox
 
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True
 
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '*':
                for num in range(1, 10):
                    num = str(num)
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = '*'
                return False
    return True
 
def get_board_from_input(entries):
    board = []
    for row in range(9):
        board_row = []
        for col in range(9):
            value = entries[row][col].get().strip()
            if value == '' or value == '*':
                board_row.append('*')
            else:
                board_row.append(value)
        board.append(board_row)
    return board
 
def show_result(board):
    result = '\n'.join([' '.join(row) for row in board])
    messagebox.showinfo("数独解", f"解答结果：\n{result}")
 
def on_submit(entries):
    board = get_board_from_input(entries)
    solve_sudoku(board)
    show_result(board)
 
def create_gui():
    window = tk.Tk()
    window.title("数独解答器")
 
    entries = []
    for row in range(9):
        row_entries = []
        for col in range(9):
            entry = tk.Entry(window, width=5, font=("Arial", 14), justify='center')
            entry.grid(row=row, column=col, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)
 
    default_board = [
        ['8', '*', '6', '*', '*', '3', '*', '9', '*'],
        ['*', '4', '*', '*', '1', '*', '*', '6', '8'],
        ['2', '*', '*', '8', '7', '*', '*', '*', '5'],
        ['1', '*', '8', '*', '*', '5', '*', '2', '*'],
        ['*', '3', '*', '1', '*', '*', '*', '5', '*'],
        ['7', '*', '5', '*', '3', '*', '9', '*', '*'],
        ['*', '2', '1', '*', '*', '7', '*', '4', '*'],
        ['6', '*', '*', '*', '2', '*', '8', '*', '*'],
        ['*', '8', '7', '6', '*', '4', '*', '*', '3']
    ]
 
    for i in range(9):
        for j in range(9):
            entries[i][j].insert(0, default_board[i][j])
 
    submit_button = tk.Button(window, text="确定", font=("Arial", 14), command=lambda: on_submit(entries))
    submit_button.grid(row=9, column=4, columnspan=2, pady=10)
 
    window.mainloop()
 
create_gui()
