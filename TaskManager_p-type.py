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
    label.forget()
    button.forget()
    label2.grid(row=0, column=0)
    task_main()

def task_main():
    #メニューバー
    menu = tk.Menu(root)
    root['menu']=menu
    menu.add_command(label='6:00～', command=menufunc_1)
    menu.add_command(label='18：00～', command=menufunc_2)

def menufunc_1():
    #サブウィンドウ
    sub_win2 = tk.Toplevel()
    sub_win2.geometry("220x400")
    #label1
    labelw = tk.Label(sub_win2, text="6:00-7:00")
    labelw.grid(row=0, column=0, padx=5, pady=5)
    txt = tk.Entry(sub_win2, width=20)
    txt.grid(row=0, column=1, padx=5, pady=5)
    #label2
    labelw2 = tk.Label(sub_win2, text="7:00-8:00")
    labelw2.grid(row=1, column=0, padx=5, pady=5)
    txt2 = tk.Entry(sub_win2, width=20)
    txt2.grid(row=1, column=1, padx=5, pady=5)
    #label3
    labelw3 = tk.Label(sub_win2, text="8:00-9:00")
    labelw3.grid(row=2, column=0, padx=5, pady=5)
    txt3 = tk.Entry(sub_win2, width=20)
    txt3.grid(row=2, column=1, padx=5, pady=5)
    #label3
    labelw4 = tk.Label(sub_win2, text="9:00-10:00")
    labelw4.grid(row=3, column=0, padx=5, pady=5)
    txt4 = tk.Entry(sub_win2, width=20)
    txt4.grid(row=3, column=1, padx=5, pady=5)
    #label3
    labelw5 = tk.Label(sub_win2, text="10:00-11:00")
    labelw5.grid(row=4, column=0, padx=5, pady=5)
    txt5 = tk.Entry(sub_win2, width=20)
    txt5.grid(row=4, column=1, padx=5, pady=5)
    #label3
    labelw6 = tk.Label(sub_win2, text="11:00-12:00")
    labelw6.grid(row=5, column=0, padx=5, pady=5)
    txt6 = tk.Entry(sub_win2, width=20)
    txt6.grid(row=5, column=1, padx=5, pady=5)
    #label3
    labelw7 = tk.Label(sub_win2, text="12:00-13:00")
    labelw7.grid(row=6, column=0, padx=5, pady=5)
    txt7 = tk.Entry(sub_win2, width=20)
    txt7.grid(row=6, column=1, padx=5, pady=5)
    #label3
    labelw8 = tk.Label(sub_win2, text="13:00-14:00")
    labelw8.grid(row=7, column=0, padx=5, pady=5)
    txt8 = tk.Entry(sub_win2, width=20)
    txt8.grid(row=7, column=1, padx=5, pady=5)
    #label3
    labelw9 = tk.Label(sub_win2, text="14:00-15:00")
    labelw9.grid(row=8, column=0, padx=5, pady=5)
    txt9 = tk.Entry(sub_win2, width=20)
    txt9.grid(row=8, column=1, padx=5, pady=5)
    #label3
    labelw10 = tk.Label(sub_win2, text="15:00-16:00")
    labelw10.grid(row=9, column=0, padx=5, pady=5)
    txt10 = tk.Entry(sub_win2, width=20)
    txt10.grid(row=9, column=1, padx=5, pady=5)
    #label3
    labelw11 = tk.Label(sub_win2, text="16:00-17:00")
    labelw11.grid(row=10, column=0, padx=5, pady=5)
    txt11 = tk.Entry(sub_win2, width=20)
    txt11.grid(row=10, column=1, padx=5, pady=5)
    #label3
    labelw12 = tk.Label(sub_win2, text="17:00-18:00")
    labelw12.grid(row=11, column=0, padx=5, pady=5)
    txt12 = tk.Entry(sub_win2, width=20)
    txt12.grid(row=11, column=1, padx=5, pady=5)
    list_txt = [txt.get(), txt2.get(), txt3.get(), txt4.get(),
                txt5.get(), txt6.get(), txt7.get(), txt8.get(),
                txt9.get(), txt10.get(), txt11.get(), txt12.get()]
    button_plot = tk.Button(sub_win2, text="plot", command=plot_circle)
    button_plot.grid(row=12, column=0, padx=30)
    
def menufunc_2():
    #サブウィンドウ
    sub_win = tk.Toplevel()
    sub_win.geometry("220x400")
    #label1
    labelx = tk.Label(sub_win, text="18:00-19:00")
    labelx.grid(row=0, column=0, padx=5, pady=5)
    txtx = tk.Entry(sub_win, width=20)
    txtx.grid(row=0, column=1, padx=5, pady=5)
    #label2
    labelx2 = tk.Label(sub_win, text="19:00-20:00")
    labelx2.grid(row=1, column=0, padx=5, pady=5)
    txtx2 = tk.Entry(sub_win, width=20)
    txtx2.grid(row=1, column=1, padx=5, pady=5)
    #label3
    labelx3 = tk.Label(sub_win, text="20:00-21:00")
    labelx3.grid(row=2, column=0, padx=5, pady=5)
    txtx3 = tk.Entry(sub_win, width=20)
    txtx3.grid(row=2, column=1, padx=5, pady=5)
    #label3
    labelx4 = tk.Label(sub_win, text="21:00-22:00")
    labelx4.grid(row=3, column=0, padx=5, pady=5)
    txtx4 = tk.Entry(sub_win, width=20)
    txtx4.grid(row=3, column=1, padx=5, pady=5)
    #label3
    labelx5 = tk.Label(sub_win, text="22:00-23:00")
    labelx5.grid(row=4, column=0, padx=5, pady=5)
    txtx5 = tk.Entry(sub_win, width=20)
    txtx5.grid(row=4, column=1, padx=5, pady=5)
    #label3
    labelx6 = tk.Label(sub_win, text="23:00-0:00")
    labelx6.grid(row=5, column=0, padx=5, pady=5)
    txtx6 = tk.Entry(sub_win, width=20)
    txtx6.grid(row=5, column=1, padx=5, pady=5)
    #label3
    labelx7 = tk.Label(sub_win, text="0:00-1:00")
    labelx7.grid(row=6, column=0, padx=5, pady=5)
    txtx7 = tk.Entry(sub_win, width=20)
    txtx7.grid(row=6, column=1, padx=5, pady=5)
    #label3
    labelx8 = tk.Label(sub_win, text="1:00-2:00")
    labelx8.grid(row=7, column=0, padx=5, pady=5)
    txtx8 = tk.Entry(sub_win, width=20)
    txtx8.grid(row=7, column=1, padx=5, pady=5)
    #label3
    labelx9 = tk.Label(sub_win, text="2:00-3:00")
    labelx9.grid(row=8, column=0, padx=5, pady=5)
    txtx9 = tk.Entry(sub_win, width=20)
    txtx9.grid(row=8, column=1, padx=5, pady=5)
    #label3
    labelx10 = tk.Label(sub_win, text="3:00-4:00")
    labelx10.grid(row=9, column=0, padx=5, pady=5)
    txtx10 = tk.Entry(sub_win, width=20)
    txtx10.grid(row=9, column=1, padx=5, pady=5)
    #label3
    labelx11 = tk.Label(sub_win, text="4:00-5:00")
    labelx11.grid(row=10, column=0, padx=5, pady=5)
    txtx11 = tk.Entry(sub_win, width=20)
    txtx11.grid(row=10, column=1, padx=5, pady=5)
    #label3
    labelx12 = tk.Label(sub_win, text="5:00-6:00")
    labelx12.grid(row=11, column=0, padx=5, pady=5)
    txtx12 = tk.Entry(sub_win, width=20)
    txtx12.grid(row=11, column=1, padx=5, pady=5)
    
    list_txt2 = [txtx.get(), txtx2.get(), txtx3.get(), txtx4.get(),
                txtx5.get(), txtx6.get(), txtx7.get(), txtx8.get(),
                txtx9.get(), txtx10.get(), txtx11.get(), txtx12.get()]

def plot_circle(list_txt):
    values = [1,1,1,1,
              1,1,1,1,
              1,1,1,1]
    labels = list_txt
    plt.pie(x=values,
            labels=labels,
            autopct='%.2f%%')
    plt.axis('equal')
    plt.show()

root = tk.Tk()

#gazou = tk.PhotoImage(file=resource_path("images/.png"))
#label = tk.Label(image=gazou)
#label.pack()

#title画面
gazou = tk.PhotoImage(file=resource_path("images/title.png"))
label = tk.Label(image=gazou)
label.grid(row=0, column=0)
button = tk.Button(text="始める", command=title)
button.grid(row=1, column=0)

#基本画面
img = tk.PhotoImage(file=resource_path("images/kokuban.png"))
label2 = tk.Label(image=img)

root.mainloop()
