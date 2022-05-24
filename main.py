from autoclicker import AutoClicker
from tkinter import *
import tkinter as ttk

root = Tk()
root.title("Auto Clicker")
root.geometry('530x400')

# get the current item selected between the radio buttons
var_1 = StringVar()
var = StringVar()


def main():
    # keep track of what time units the numbers are
    repeat = int(repeat_entry.get())
    click_type = clicked.get()
    mouse_button = buttons.get()
    try:
        x_cursor_pos = int(x_entry.get())
        y_cursor_pos = int(y_entry.get())
    except ValueError:
        x_cursor_pos = None
        y_cursor_pos = None

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
    mouse = AutoClicker(repeat, mouse_button, sum_time, x_cursor_pos, y_cursor_pos)
    # determine if user chooses a single or double click
    if click_type == "Double click":
        mouse.double_click()
    if click_type == "Single click" and var.get() != "Repeat":
        mouse.repeat_until_stop()
    else:
        mouse.single_click()


def show():
    label.config(text=clicked.get())


def select_button():
    selection = var_1.get()
    label.config(text=selection)
    return selection


def select_radio_button():
    selection = var_1.get()
    repeat_selection = var.get()
    x_entry.config(state=ttk.DISABLED if selection == "Current location" else ttk.NORMAL)
    y_entry.config(state=ttk.DISABLED if selection == "Current location" else ttk.NORMAL)
    repeat_entry.config(state=ttk.DISABLED if repeat_selection == "Repeat until stopped" else ttk.NORMAL)


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
repeat_button = ttk.Radiobutton(frame_click_options, text="Repeat", justify=LEFT, anchor="w", variable=var,
                                value="Repeat", command=select_radio_button)
repeat_entry = ttk.Entry(frame_click_options, width=5, justify=CENTER)
repeat_entry.insert(0, "1")
until_stop_button = ttk.Radiobutton(frame_click_options, text="Repeat until stopped", justify=LEFT, anchor="w",
                                    variable=var, value="Repeat until stopped", command=select_radio_button)
time_label = ttk.Label(frame_click_options, text="times")
click_type_label = ttk.Label(frame_click_options, text="Click type: ")
mouse_button_label = ttk.Label(frame_click_options, text="Mouse Button: ")

# creating drop down menus for click options and button options
click_options = ["Single click", "Double click"]
clicked = StringVar()
clicked.set("Single click")
click_drop = OptionMenu(frame_click_options, clicked, *click_options)

button_options = ["Left", "Right"]
buttons = StringVar()
buttons.set("Left")
button_drop = OptionMenu(frame_click_options, buttons, *button_options)

# places the widgets
repeat_button.grid(column=0, row=0, padx=3, pady=10, sticky=W)
repeat_entry.grid(column=1, row=0, padx=3, pady=10)
time_label.grid(column=2, row=0, padx=4, pady=10)

click_type_label.grid(column=0, row=2, padx=4, pady=10, sticky=W)
mouse_button_label.grid(column=0, row=3, padx=4, pady=10, sticky=W)
click_drop.grid(column=1, row=2, sticky=E)
button_drop.grid(column=1, row=3, sticky=E)
until_stop_button.grid(column=0, row=1, padx=3, pady=10, sticky=W)

# creates widgets for the cursor position frame
current_location_radio = ttk.Radiobutton(frame_cursor_pos, text="Current location", variable=var_1,
                                         value="Current location", command=select_radio_button)
pick_location_radio = ttk.Radiobutton(frame_cursor_pos, text="Pick location", justify=LEFT, anchor="w", variable=var_1,
                                      value="Pick location", command=select_radio_button)
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
stop = ttk.Label(text="hold q to stop or move cursor to top left corner")
quit_app = ttk.Button(text="quit", command=root.destroy)

start.grid(column=0, row=2, padx=35, sticky=W)
stop.grid(column=0, row=3, pady=17, sticky=S)
quit_app.grid(column=0, row=2, sticky=S)

root.mainloop()
