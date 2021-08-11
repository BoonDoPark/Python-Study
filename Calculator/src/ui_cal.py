import tkinter as tk
import Calculator


class UiCalculator:
    def __init__(self):
        self.ui_cal = tk.Tk()
        self.ui_cal.title('계산기')
        self.ui_cal.geometry('500x400')

        self.clicked_button()

        self.tk_mainloop()

    def tk_entry(self, number):
        self.entry = tk.Entry(self.ui_cal)
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0,str(current)+str(number))

    def mainboard_clear(self):
        self.entry.delete(0, tk.END)

    def clicked_button(self):
        print('success')
        self.button = tk.Button(self.ui_cal, text='1', height=4, width=8, command=lambda: self.tk_entry(1)).grid(column=0, row=4)
        self.button1 = tk.Button(self.ui_cal, text='1', height=4, width=8, command=lambda: self.tk_entry(1)).grid(column=0,row=1)
        self.button2 = tk.Button(self.ui_cal, text='2', height=4, width=8, command=lambda: self.tk_entry(2)).grid(column=1,row=1)
        self.button3 = tk.Button(self.ui_cal, text='3', height=4, width=8, command=lambda: self.tk_entry(3)).grid(column=2,row=1)
        self.button4 = tk.Button(self.ui_cal, text='4', height=4, width=8, command=lambda: self.tk_entry(4)).grid(column=0,row=2)
        self.button4 = tk.Button(self.ui_cal, text='4', height=4, width=8, command=lambda: self.tk_entry(4)).grid(column=1,row=2)
        self.button6 = tk.Button(self.ui_cal, text='6', height=4, width=8, command=lambda: self.tk_entry(6)).grid(column=2,row=2)
        self.button7 = tk.Button(self.ui_cal, text='7', height=4, width=8, command=lambda: self.tk_entry(7)).grid(column=0,row=3)
        self.button8 = tk.Button(self.ui_cal, text='8', height=4, width=8, command=lambda: self.tk_entry(8)).grid(column=1,row=3)
        self.button9 = tk.Button(self.ui_cal, text='9', height=4, width=8, command=lambda: self.tk_entry(9)).grid(column=2,row=3)
        self.button8 = tk.Button(self.ui_cal, text='+', height=4, width=8, command=lambda: self.tk_entry('+')).grid(column=3,row=3)
        self.button11 = tk.Button(self.ui_cal, text='-', height=4, width=8, command=lambda: self.tk_entry('-')).grid(column=3,row=4)
        self.button12 = tk.Button(self.ui_cal, text='x', height=4, width=8, command=lambda: self.tk_entry('x')).grid(column=1,row=4)
        self.button13 = tk.Button(self.ui_cal, text='/', height=4, width=8, command=lambda: self.tk_entry('/')).grid(column=2,row=4)
        self.button14 = tk.Button(self.ui_cal, text='=', height=4, width=8, command=lambda: self.tk_entry('=')).grid(column=3,row=2)
        self.button14 = tk.Button(self.ui_cal, text='C', height=4, width=8, command=lambda: self.tk_entry('C')).grid(column=3,row=1)
        self.button16 = tk.Button(self.ui_cal, text='.', height=4, width=8, command=lambda: self.tk_entry('.')).grid(column=3, row=5)

    def tk_mainloop(self):
        self.ui_cal.mainloop()


if __name__ == '__main__':
    uc = UiCalculator()