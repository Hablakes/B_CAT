import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import yfinance as yf

from tkinter import Button, Entry, Tk, mainloop


current_date = str(dt.date.today())
start_date_ode = str(str(current_date[0:-2]) + str(int(current_date[-2::]) - 1))
start_date_fye = str(str(int(current_date[0:4]) - 5) + str(current_date[4::]))


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('INF')


def get_commands_gui():
    command_entered = []

    root = Tk()
    root.title('SHARES AND PRICE ENTRY')
    root.geometry('325x30')

    shares_command = Entry(root)
    shares_command.grid(row=0, column=1)

    price_command = Entry(root)
    price_command.grid(row=0, column=2)

    def get_command_globals():
        command_entered.append(shares_command.get())
        command_entered.append(price_command.get())
        root.destroy()

    button_entry = Button(root, text='SUBMIT', command=get_command_globals)
    button_entry.grid(row=0, column=3)

    def enter_press(*args, **kwargs):
        button_entry.invoke()

    shares_command.bind('<Return>', enter_press)
    price_command.bind('<Return>', enter_press)

    mainloop()
    print(command_entered)
    # return command_entered


get_commands_gui()

