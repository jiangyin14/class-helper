# 导库
try:
    import tkinter as tk
except:
    import Tkinter as tk

# 导入必要的库
import tkinter as tk
from tkinter import Button
import time
import datetime
import pyautogui as pg
import keyboard
import tkinter.messagebox
import tkinter.ttk as ttk

class_=[
    [
        "语文",
        "信息",
        "数学",
        "科学",
        "英语",
        "美术",
    ],[
        "数学",
        "语文",
        "科学",
        "语文",
        "体育",
        "音乐",
    ],[
        "数学",
        "英语",
        "语文",
        "语文",
        "语文",
        "美术",
    ],[
        "语文",
        "数学",
        "英语",
        "书法",
        "科学",
        "体育",
    ],[
        "语文",
        "数学",
        "音乐",
        "语文",
        "快乐周末",
        "快乐周末",
    ],
]

class_time=[
    ["00:00","07:29","放学"],
    ["07:30","08:19","早自习"],
    ["08:20","08:59","大课间"],
    ["09:00","09:39","1"],
    ["09:40","09:49","课间"],
    ["09:50","10:34","2"],
    ["10:35","10:44","课间"],
    ["10:45","11:24","3"],
    ["11:25","11:44","午饭"],
    ["11:45","12:39","自习"],
    ["12:40","13:19","4"],
    ["13:20","13:29","课间"],
    ["13:40","14:25","5"],
    ["14:35","14:44","课间"],
    ["14:45","15:25","6"],
    ["15:35","15:59","自习"],
    ["16:00","17:29","托管"],
    ["17:30","23:59","放学"]
]

_class_time=[
    ["00:00","07:29","放学"],
    ["07:30","08:19","早自习"],
    ["08:20","08:59","大课间"],
    ["09:00","09:39","1"],
    ["09:40","09:49","课间"],
    ["09:50","10:34","2"],
    ["10:35","10:44","课间"],
    ["10:45","11:24","3"],
    ["11:25","11:44","午饭"],
    ["11:45","12:39","自习"],
    ["12:40","13:19","4"],
    ["13:20","13:29","课间"],
    ["13:40","14:09","5"],
    ["14:10","15:39","6"],
    ["15:40","15:49","自习"],
    ["15:50","23:59","放学"]
]

begin=["07:30","07:30","07:30","07:30","07:30"]
end_=["17:30","17:30","17:30","17:30","15:50"]
class_status=False


# 窗口创建
root = tk.Tk()

# 窗口大小
root.geometry("415x300+10+10")

# 窗口设置
root.overrideredirect(True)
root.lift()
root.attributes("-topmost", True)
root.attributes("-toolwindow", True)
root.attributes("-alpha", 0.95)
root.configure(background='#D8D8D8')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = tk.Canvas(root, highlightthickness=0)

# 隐藏窗口
def hide_window():
    root.withdraw() # 隐藏页面
    tk.messagebox.showinfo("提示", "您可以按下Ctrl+Alt+T快捷键重新显示窗口")

# 显示窗口
def show_window():
    root.deiconify() # 显示窗口

def move(event):
    """窗口移动事件"""
    new_x = (event.x - root.x) + root.winfo_x()
    new_y = (event.y - root.y) + root.winfo_y()

    if(new_x<0):
        new_x=0
    elif(new_x>screen_width-415):
        new_x=screen_width-415
    if(new_y<0):
        new_y=0
    elif(new_y>screen_height-300):
        new_y=screen_height-300
    s = f"415x300+{new_x}+{new_y}"
    root.geometry(s)

def get_point(event):
    """获取当前窗口位置并保存"""
    root.x, root.y = event.x, event.y

# 创建一个函数，用于关闭窗口
def close_window():
    root.destroy()  # 关闭窗口

# 创建关闭按钮，将其文本设置为"X"，并指定点击时调用close_window函数
close_button = Button(root, text="X", command=close_window, relief=tk.FLAT, bg="#FF0000", width=6, height=1)

# 将关闭按钮放置在窗口的右上角
close_button.place(x=360, y=0)


# 标题栏
mainTitle = tk.Label(root, text="课堂小助手", font=('微软雅黑 10'), background='#D8D8D8')
mainTitle.place(x=0,y=0)
mainTitle = tk.Label(root, text="v0.0.1", font=('微软雅黑 6'), background='#D8D8D8')
mainTitle.place(x=147,y=20)

# 时间栏
mainTitle = tk.Label(root, text="", font=('微软雅黑 10'), background='#EFEFEF')
mainTitle.place(x=250,y=0)

# 进度条

# 样式对象
style = ttk.Style()


# style.configure(thickness=20)
# 创建一个进度条对象
bar_1 = ttk.Progressbar(root, length=330)
# 设置进度条的方向和模式
bar_1["orient"] = tk.HORIZONTAL
# 将进度条放置在窗口上
bar_1.place(x=5, y=100)

# 距离下课时间
time_label1=tk.Label(root, text="", font=('微软雅黑 9'), background='#D8D8D8')
time_label1.place(x=5,y=60)

time_label1_=tk.Label(root, text="", font=('微软雅黑 9'), background='#D8D8D8')
time_label1_.place(x=340, y=90)


bar_2 = ttk.Progressbar(root, length=330)
# 设置进度条的方向和模式
bar_2["orient"] = tk.HORIZONTAL
# 将进度条放置在窗口上
bar_2.place(x=5, y=180)

# 距离放学时间
time_label2=tk.Label(root, text="", font=('微软雅黑 9'), background='#D8D8D8')
time_label2.place(x=5,y=140)

time_label2_=tk.Label(root, text="", font=('微软雅黑 9'), background='#D8D8D8')
time_label2_.place(x=340, y=170)

# 隐藏按钮
hide_button = tk.Button(root, text="隐 藏", command=hide_window, relief=tk.FLAT,bg="#FFFFFF",width=6, height=1)

label3=tk.Label(root, text="", font=('微软雅黑 9'), background='#D8D8D8')
label3.place(x=200, y=250)

# 将按钮放置在左下角
hide_button.place(x=5, y=240)

# 更新时间
def update_time():
    # 获取当前的时间，格式为XX:XX
    current_time = datetime.datetime.now().strftime("%H:%M")
    # 当前时间
    n_time = datetime.datetime.now()
    # 当前周
    n_week=n_time.weekday()

    start=""
    end=""
    class_num=-1
    now_class=""
    # 判断当前课程
    if(n_week<=3):
        for i in class_time:
            d_time = datetime.datetime.strptime(str(n_time.date()) + i[0], '%Y-%m-%d%H:%M')
            d_n_time = datetime.datetime.strptime(str(n_time.date()) + i[1], '%Y-%m-%d%H:%M')

            # 判断当前时间是否在范围时间内
            if n_time > d_time and n_time < d_n_time:
                now_class = i[2]
                start = i[0]
                end = i[1]
                
                break
            class_num+=1
    elif(n_week==4):
        for i in _class_time:
            d_time = datetime.datetime.strptime(str(n_time.date()) + i[0], '%Y-%m-%d%H:%M')
            d_n_time = datetime.datetime.strptime(str(n_time.date()) + i[1], '%Y-%m-%d%H:%M')

            # 判断当前时间是否在范围时间内
            if n_time > d_time and n_time < d_n_time:
                now_class = i[2]
                start = i[0]
                end = i[1]
                break
            class_num+=1
    else:
        now_class="周末"
        start = "00:00"
        end = "23:59"
    
    try:
        now_class=class_[n_week][int(now_class)-1]
        class_status=True
    except:
        if(now_class=="托管"):
            class_status=True
        else:
            class_status=False
        pass
    
    # 更新Label组件的文本
    mainTitle.config(text="%s|%s"%(current_time,now_class))

    if(now_class=="周末"):
        now_class="今天"
    if(class_status==True and now_class!="托管"):
        now_class+="课"

    time1=datetime.datetime.strptime(n_time.strftime("%H:%M:%S"), "%H:%M:%S")
    time2=datetime.datetime.strptime(end, "%H:%M")
    time3=datetime.datetime.strptime(start, "%H:%M")
    h1=int((time2-time1).total_seconds()//60//60)
    m1=int(((time2-time1).total_seconds()-h1*60*60)//60)
    s1=int((time2-time1).total_seconds()-h1*60*60-m1*60)
    time_label1.config(text="距离%s结束还有%s小时%s分钟%s秒"%(str(now_class),h1,m1,s1))

    bar_1["maximum"] = (time2-time3).total_seconds()
    bar_1["value"] = bar_1["maximum"]-(time2-time1).total_seconds()
    # print(bar_1["maximum"],bar_1["value"])
    # print(int(bar_1["value"]/bar_1["maximum"]*100))
    time_label1_.config(text="{}%".format(round(bar_1["value"]/bar_1["maximum"]*100,1)))
    
    if(n_week<=4):
        time1=datetime.datetime.strptime(n_time.strftime("%H:%M:%S"), "%H:%M:%S")
        time2=datetime.datetime.strptime(end_[n_week], "%H:%M")
        time3=datetime.datetime.strptime(begin[n_week], "%H:%M")
        h1=int((time2-time1).total_seconds()//60//60)
        m1=int(((time2-time1).total_seconds()-h1*60*60)//60)
        s1=int((time2-time1).total_seconds()-h1*60*60-m1*60)
        time_label2.config(text="距离放学还有%s小时%s分钟%s秒"%(h1,m1,s1))

        bar_2["maximum"] = (time2-time3).total_seconds()
        bar_2["value"] = bar_2["maximum"]-(time2-time1).total_seconds()
        # print(bar_1["maximum"],bar_1["value"])
        # print(int(bar_1["value"]/bar_1["maximum"]*100))
        time_label2_.config(text="{}%".format(round(bar_2["value"]/bar_2["maximum"]*100,1)))
        # print(class_num)
        # label3.config(text="下一节：%s课"%class_time[class_num+1][-1])
        try:
            next_class=class_time[class_num+2][-1]
            try:
                next_class=class_[n_week][int(next_class)-1]+"课"
                
            except:
                if(next_class=="自习"):
                    next_class+="课"
            label3.config(text="下一节：%s"%next_class)
        except:
            pass

    
    root.update()

    # 每隔0.5秒调用一次自己，实现动态更新
    root.after(500, update_time)

# 调用函数
update_time()

# 绑定快捷键ctrl+alt+t和重新显示窗口的函数
keyboard.add_hotkey('ctrl+alt+t', show_window)

# 窗口移动事件
root.bind("<B1-Motion>", move)
# 单击事件
root.bind("<Button-1>", get_point)


# 进入消息循环
root.mainloop()