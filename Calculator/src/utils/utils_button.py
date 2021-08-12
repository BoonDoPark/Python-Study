import tkinter as tk


class UtilButton:

    @staticmethod
    def button(master, arith, entry, column: int, row: int):
        tk_button = tk.Button(master, text=f'{arith}', height=4, width=8,
                              command=lambda: entry(arith)).grid(column=column, row=row)
        return tk_button
