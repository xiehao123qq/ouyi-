import subprocess
import threading
from tkinter import Tk, Label, Button
import wx.xrc
from ma import ma
import gettext
from datetime import datetime
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

# class Funct():
#     def __init__(self):

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################
import threading
import time
# 主线程结束，守护线程自动退出
def show_custom_message1(message):
    root = Tk()
    root.title("提醒")

    # 设置窗口的大小为 600x600
    root.geometry("600x600")

    # 设置标签背景，并通过 grid() 布局填充整个窗口
    label = Label(root, text=message, font=("Arial", 30, "bold"), fg="blue", bg="lightyellow")
    label.grid(row=0, column=0, sticky="nsew")  # 让标签充满整个窗口区域

    # 配置行和列的权重，使它们可以自动扩展
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # OK按钮
    ok_button = Button(root, text="OK", command=root.destroy)
    ok_button.grid(row=1, column=0, pady=20)

    root.mainloop()

def show_custom_message2(message):
    root = Tk()
    root.title("信息")

    # 设置窗口的大小为 600x600
    root.geometry("600x600")

    # 设置标签背景，并通过 grid() 布局填充整个窗口
    label = Label(root, text=message, font=("Arial", 30, "bold"), fg="blue", bg="lightyellow")
    label.grid(row=0, column=0, sticky="nsew")  # 让标签充满整个窗口区域

    # 配置行和列的权重，使它们可以自动扩展
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # OK按钮
    ok_button = Button(root, text="OK", command=root.destroy)
    ok_button.grid(row=1, column=0, pady=20)

    root.mainloop()
class MyFrame1 ( wx.Frame ):
    def __init__( self, parent ):

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.num1 = None
        self.num2 = None
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, _(u"欢迎使用易欧交易监控程序"), wx.DefaultPosition,
                                           wx.Size(500, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(
            wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.m_staticText5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, -1), 0)
        self.m_staticText9.Wrap(-1)

        bSizer3.Add(self.m_staticText9, 0, wx.ALL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, _(u"请输入要计算的差值的垂直距离，如，-6~6"),
                                            wx.DefaultPosition, wx.Size(250, -1), 0)
        self.m_staticText11.Wrap(-1)

        fgSizer1.Add(self.m_staticText11, 0, wx.ALL, 5)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.m_textCtrl7, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, _(u"开始运行"), wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.m_button2, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer3, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer5.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_staticText91 = wx.StaticText(self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.Size(250, -1),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText91.Wrap(-1)

        bSizer5.Add(self.m_staticText91, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        fgSizer5 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        bSizer9.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, _(u"停止程序"), wx.DefaultPosition, wx.Size(125, -1), 0)
        bSizer9.Add(self.m_button7, 0, wx.ALL, 5)

        fgSizer5.Add(bSizer9, 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer5, 1, wx.EXPAND, 5)

        bSizer3.Add(fgSizer1, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText38 = wx.StaticText(self, wx.ID_ANY, _(u"结果"), wx.DefaultPosition, wx.Size(250, -1),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText38.Wrap(-1)

        fgSizer4.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        fgSizer4.Add(self.m_textCtrl8, 0, wx.ALL, 5)

        bSizer7.Add(fgSizer4, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        fgSizer51 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer51.SetFlexibleDirection(wx.BOTH)
        fgSizer51.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText81 = wx.StaticText(self, wx.ID_ANY, _(u"QQ机器人"), wx.DefaultPosition, wx.Size(250, -1),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText81.Wrap(-1)

        fgSizer51.Add(self.m_staticText81, 0, wx.ALL, 5)

        fgSizer8 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button6 = wx.Button(self, wx.ID_ANY, _(u"启动"), wx.DefaultPosition, wx.Size(100, -1), 0)
        fgSizer8.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_button71 = wx.Button(self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.Size(100, -1), 0)
        fgSizer8.Add(self.m_button71, 0, wx.ALL, 5)

        fgSizer51.Add(fgSizer8, 1, wx.EXPAND, 5)

        bSizer6.Add(fgSizer51, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.find_square)
        self.m_button7.Bind(wx.EVT_BUTTON, self.start_func)
        self.m_button6.Bind(wx.EVT_BUTTON, self.qqStarting)
        self.m_button71.Bind(wx.EVT_BUTTON, self.stopqq)
        self.m_button2.Bind( wx.EVT_BUTTON, self.find_square)
        self.m_button7.Bind( wx.EVT_BUTTON, self.start_func )

        # 线程控制变量
        self.running = False
        self.worker_thread = None
        self.running1 = False
        self.worker_thread1 = None

    def __del__( self ):
        pass
    def start(self):
        """每分钟计算一次 1 + 1，后台线程任务"""
        num1=self.num1
        num2=self.num2
        while self.running:
            # 进行计算
            a=ma(30)
            b=ma(120)
            if a is not None and b is not None:
                c=a-b
                result=str(c)
                self.m_textCtrl8.SetValue(result)
                print(f"计算的结果: {result}")
                time1=datetime.now()
                print("现在的时间是"+str(time1))
                if int(c) <= num2 and int(c) >= num1:
                    current_time = str(datetime.now())
                    formatted_time = current_time[:10] + "\n\n" + current_time[10:19]+"\n\n"+result+"\n"  # 手动换行
                    message2=f"符合预期，\n\n现在的时间是\n\n{formatted_time}"
                    threading.Thread(target=show_custom_message2, args=(message2,)).start()
                    # wx.MessageBox(f"符合预期，现在的时间是{current_time}", "提示", wx.OK | wx.ICON_INFORMATION)
                # 等待 60 秒，但每次只 sleep 1 秒，检查 stop 信号
                for _ in range(10):
                    if not self.running:
                        print("任务提前停止")
                        return
                    time.sleep(1)
            else:
                print("计算失败，可能是数据获取或计算错误")
                for _ in range(10):
                     if not self.running:
                         print("任务提前停止")
                         return
                     time.sleep(1)

        print("任务完成")

    # Virtual event handlers, override them in your derived class
    def find_square(self, event):
        str1 = str(self.m_textCtrl7.GetValue())  # 获取输入的数字数值
        # 使用 ~ 作为分隔符分割字符串
        numbers = str1.split("~")
        # 将分割后的字符串转换为整数
        self.num1 = int(numbers[0])
        self.num2 = int(numbers[1])

        # 打印两个数字
        print(f"第一个数字: {self.num1}")
        print(f"第二个数字: {self.num2}")
        if self.num2 < self.num1:
            message_err="设置有误请重新输入"+"\n\n\n\n\n\n"
            show_custom_message1(message=message_err)
            event.Skip()
        else:
            print(self.num2-self.num1)
        """点击 Start 按钮时启动 find_square 方法"""
        if not self.running:
            self.running = True
            self.worker_thread = threading.Thread(target=self.start)
            self.worker_thread.start()
            self.m_button2.Disable()  # 启动后禁用 Start 按钮
            self.m_button7.Enable()    # 启动后启用 Stop 按钮
            message="程序开始运行"+"\n\n\n\n\n\n"
            show_custom_message1(message=message)

    def start_func(self, event):
        if self.running:
            self.running = False
            self.worker_thread.join()    # 等待线程结束
            self.m_button2.Enable()   # 停止后启用 Start 按钮
            self.m_button7.Disable()   # 停止后禁用 Stop 按钮
            message = "程序停止运行" + "\n\n\n\n\n\n"
            show_custom_message1(message=message)
    def qqStarting( self, event ):
        if not self.running1:
            self.running1 = True
            self.worker_thread1 = threading.Thread(target=self.startqq)
            self.worker_thread1.start()
            self.m_button6.Disable()  # 启动后禁用 Start 按钮
            self.m_button71.Enable()    # 启动后启用 Stop 按钮



    def stopqq(self,event):
        if  self.running1:
            self.running1 = False
            self.worker_thread1.join()  # 等待线程结束
            self.m_button6.Enable()  # 停止后启用 Start 按钮
            self.m_button71.Disable()  # 停止后禁用 Stop 按钮
            if self.process.poll() is None:
                print("test.py 仍在运行，终止它...")
                # 使用 terminate() 来优雅地终止
                self.process.terminate()
                # 等待进程退出
                self.process.wait()
                print("test.py 已成功终止")
            else:
                print("test.py 已经结束")
            # 清理进程对象
            self.process = None
            wx.MessageBox(f"qq已经停止", "提示", wx.OK | wx.ICON_INFORMATION)

    def startqq(self):
        if self.running1:
            try:
                self.process = subprocess.Popen([r'.\venv\Scripts\python.exe', './test.py'],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                encoding='utf-8',
                                                text=True)
                # 等待一段时间，让进程运行（例如5秒）
                time.sleep(2)
                wx.MessageBox(f"qq已经启动", "提示", wx.OK | wx.ICON_INFORMATION)
            except(Exception) as e:
                print("发生错误：", e)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()

