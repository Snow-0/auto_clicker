from autoclicker import AutoClicker
from tkinter import *
import tkinter as ttk
import time

root = Tk()
root.title("Auto Clicker")
root.geometry('500x400')
root.resizable(False, False)


def main():
    # keep track of what time units the numbers are
    time_list_keys = ["hours", "minutes", "seconds", "milliseconds"]
    sum_time = 0
    time_dict = {time_list_keys[i]: int(root.entries[i].get()) for i in range(len(time_list_keys))}
    # converts other time units into seconds
    for key, value in time_dict.items():
        if key == "hours":
            sum_time += value * 3600
        elif key == "minutes":
            sum_time += value * 60
        elif key == "milliseconds":
            sum_time += value / 1000
        else:
            sum_time += value
    click = AutoClicker()
    time.sleep(5)


def show():
    label.config(text=clicked.get())


def select_button():
    selection = var.get()
    label.config(text=selection)
    return selection


# create frame widgets
frame_click_interval = ttk.LabelFrame(root, text="Click Interval")
frame_click_options = ttk.LabelFrame(root, text="Click options")
frame_cursor_pos = ttk.LabelFrame(root, text="Cursor Position")

frame_click_interval.grid(column=0, row=0, padx=20, pady=20, columnspan=2)
frame_click_options.grid(column=0, row=1, sticky="N", ipadx=15)
frame_cursor_pos.grid(column=1, row=1, rowspan=2)

interval_entries = ("hours", "mins", "seconds", "milliseconds")
grid_column = 0
root.entries = []
for interval_entry in interval_entries:
    # creates the labels for the entries: hours, minutes, etc
    label = ttk.Label(frame_click_interval, text=interval_entry)
    # creates entries for click interval
    entry = ttk.Entry(frame_click_interval, width=5, justify=RIGHT)
    entry.insert(0, "0")
    root.entries.append(entry)

    # positions the widgets
    entry.grid(column=grid_column, row=0, ipadx=5, ipady=5, padx=3, pady=10)
    grid_column += 1
    label.grid(column=grid_column, row=0, ipadx=3, ipady=3)
    grid_column += 1

# Creates widgets for the click option frame
repeat_label = ttk.Label(frame_click_options, text="Repeat", justify=LEFT, anchor="w")
repeat_entry = ttk.Entry(frame_click_options, width=5, justify=CENTER)
repeat_entry.insert(0, "1")
time_label = ttk.Label(frame_click_options, text="times")
click_type_label = ttk.Label(frame_click_options, text="Click type: ")
mouse_button_label = ttk.Label(frame_click_options, text="Mouse Button: ")

# creating drop down menus for click options and button options
click_options = ["Single click", "Double click"]
clicked = StringVar()
clicked.set("Single Click")
click_drop = OptionMenu(frame_click_options, clicked, *click_options)

button_options = ["Left", "Right"]
buttons = StringVar()
buttons.set("Left")
button_drop = OptionMenu(frame_click_options, buttons, *button_options)

# places the widgets
repeat_label.grid(column=0, row=0, padx=3, pady=10, sticky=W)
repeat_entry.grid(column=1, row=0, padx=3, pady=10)
time_label.grid(column=2, row=0, padx=4, pady=10)
click_type_label.grid(column=0, row=1, padx=4, pady=10, sticky=W)
mouse_button_label.grid(column=0, row=2, padx=4, pady=10, sticky=W)
click_drop.grid(column=1, row=1, sticky=E)
button_drop.grid(column=1, row=2, sticky=E)

var = StringVar()

# creates widgets for the cursor position frame
current_location_radio = ttk.Radiobutton(frame_cursor_pos, text="Current location", variable=var,
                                         value="Current location")
pick_location_radio = ttk.Radiobutton(frame_cursor_pos, text="Pick location", justify=LEFT, anchor="w", variable=var,
                                      value="Pick location")
x_pos_label = ttk.Label(frame_cursor_pos, text="X", padx=10, justify=LEFT, anchor="w")
y_pos_label = ttk.Label(frame_cursor_pos, text="Y", padx=10, justify=LEFT, anchor="w")
x_entry = ttk.Entry(frame_cursor_pos, width=5)
y_entry = ttk.Entry(frame_cursor_pos, width=5)

# places the widgets
current_location_radio.grid(column=0, row=0, padx=3, pady=10, columnspan=2)
pick_location_radio.grid(column=0, row=1, padx=3, pady=10, sticky=W, columnspan=2)
x_pos_label.grid(column=0, row=2, ipadx=5, ipady=5, padx=3, pady=10)
y_pos_label.grid(column=0, row=3, ipadx=5, ipady=5, padx=3, pady=10)
x_entry.grid(column=1, row=2, ipadx=5, ipady=5, padx=3, pady=10, sticky=W)
y_entry.grid(column=1, row=3, ipadx=5, ipady=5, padx=3, pady=10, sticky=W)

# start and stop buttons

start = ttk.Button(text="Start", command=main, justify=LEFT)
stop = ttk.Button(text="Stop (q)")
quit_app = ttk.Button(text="quit", command=root.destroy)

start.grid(column=0, row=2, padx=35, sticky=W)
stop.grid(column=0, row=2, pady=17, sticky=S)
quit_app.grid(column=0, row=2, sticky=E, padx=35)

root.mainloop()
