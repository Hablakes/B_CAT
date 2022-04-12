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
    root.title('TICKER SYMBOL ENTRY')
    root.geometry('300x30')

    command = Entry(root)
    command.grid(row=0, column=1)

    def get_command_globals():
        command_entered.append(command.get())
        root.destroy()

    button_entry = Button(root, text='SUBMIT', command=get_command_globals)
    button_entry.grid(row=0)

    def enter_press(*args, **kwargs):
        button_entry.invoke()

    command.bind('<Return>', enter_press)

    mainloop()
    return command_entered[0].upper()


coin_ticker_symbol = get_commands_gui()


def create_graph_from_yf_data():
    yf_data = yf.download(coin_ticker_symbol, start_date_fye, current_date)
    yf_data['Adj Close'].plot(figsize=(10, 6))

    plt.title(str(coin_ticker_symbol), fontsize=12)
    plt.ylabel('PRICE', fontsize=8)
    plt.xlabel('YEAR', fontsize=8)
    plt.grid(which="major", color='k', linestyle='-', linewidth=0.5)

    plt.show()


create_graph_from_yf_data()


"""
pdr_data = pdr.DataReader(coin_ticker_symbol, 'yahoo', start_date_fye, current_date)
"""
