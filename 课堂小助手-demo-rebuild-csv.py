import tkinter as tk
from tkinter import Button
import csv

# 创建一个函数，用于关闭窗口
def close_window():
    root.destroy()  # 关闭窗口

# 读取课程表数据
def read_class_schedule(file_name):
    class_schedule = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            class_schedule.append(row)
    return class_schedule

# 读取课程表数据从class.csv文件
class_schedule = read_class_schedule('class.csv')

# 窗口创建
root = tk.Tk()

# 窗口大小和其他属性设置
root.geometry("415x300+10+10")
root.overrideredirect(True)
root.lift()
root.attributes("-topmost", True)
root.attributes("-toolwindow", True)
root.attributes("-alpha", 0.95)
root.configure(background='#D8D8D8')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 创建关闭按钮，将其文本设置为"X"，并指定点击时调用close_window函数
close_button = Button(root, text="X", command=close_window, relief=tk.FLAT, bg="#FF0000", width=6, height=1)

# 将关闭按钮放置在窗口的右上角
close_button.place(x=385, y=0)

# 输出课程表数据
for row in class_schedule:
    print(', '.join(row))

# 进入消息循环
root.mainloop()