#This software is licensed by MIT License.
import tkinter as tk
import os
import sys
import matplotlib.pyplot as plt

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def title():
    label_title.grid_forget()
    button.grid_forget()
    label_2.grid(row=0, column=0)
    task_main()

def task_main():
    menu = tk.Menu(root)
    root.config(menu=menu)
    menu.add_command(label='6:00～', command=lambda: create_schedule_window("6:00-18:00"))
    menu.add_command(label='18:00～', command=lambda: create_schedule_window_2("18:00-6:00"))

def create_schedule_window(time_range):
    sub_win = tk.Toplevel()
    sub_win.geometry("230x400")
    sub_win.title("tasks")
    sub_win.iconbitmap(resource_path("images/icon.ico"))
    entries = []
    for i in range(12):
        hour = (6 + i) if "6:00" in time_range else (18 + i) % 24
        label = tk.Label(sub_win, text=f"{hour}:00-{hour+1}:00")
        label.grid(row=i, column=0, padx=5, pady=5)
        txt = tk.Entry(sub_win, width=20)
        txt.grid(row=i, column=1, padx=5, pady=5)
        entries.append(txt)
    tk.Button(sub_win, text="plot", command=lambda: plot_circle([e.get() for e in entries])).grid(row=12, column=0, padx=30)

def create_schedule_window_2(time_range_2):
    sub_win_2 = tk.Toplevel()
    sub_win_2.geometry("230x400")
    sub_win_2.title("tasks2")
    sub_win_2.iconbitmap(resource_path("images/icon.ico"))
    entries = []
    for i in range(12):
        hour = (18 + i) if "18:00" in time_range_2 else (18 + i) % 24
        label_range2 = tk.Label(sub_win_2, text=f"{hour%24}:00-{(hour+1)%24}:00")
        label_range2.grid(row=i, column=0, padx=5, pady=5)
        txt_2 = tk.Entry(sub_win_2, width=20)
        txt_2.grid(row=i, column=1, padx=5, pady=5)
        entries.append(txt_2)
    tk.Button(sub_win_2, text="plot", command=lambda: plot_circle([e.get() for e in entries])).grid(row=12, column=0, padx=30)

def plot_circle(labels):
    plt.pie([1]*12, labels=labels, wedgeprops={'linewidth': 3, 'edgecolor':'white'},labeldistance=0.5, textprops={'color':'white', 'weight':'bold'}, startangle=270, counterclock=False)
    plt.axis('equal')
    plt.show()

root = tk.Tk()

root.title("TaskManeger")
icon_path = resource_path('images/icon.ico')
root.iconbitmap(icon_path)

gazou = tk.PhotoImage(file=resource_path("images/title.png"))
label_title = tk.Label(root, image=gazou)
label_title.grid(row=0, column=0)
button = tk.Button(root, text="始める", command=title)
button.grid(row=1, column=0)

gazou2 = tk.PhotoImage(file=resource_path("images/kokuban.png"))
label_2 = tk.Label(root, image=gazou2)

root.mainloop()
