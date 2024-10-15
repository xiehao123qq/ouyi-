# -*- coding: utf-8 -*-
import time
from unittest import result

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import schedule
import wx
import wx.xrc
from ma import ma
import gettext
from tkinter import messagebox
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

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        #wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        # 创建 Panel
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.num1=0
        self.num2=0
        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"欢迎使用欧易交易监控程序"), wx.DefaultPosition, wx.Size( 500,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )
        self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"请输入要计算的差值的垂直距离，如，-6~6"), wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        self.m_staticText11.Wrap( -1 )

        fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self,wx.ID_ANY, _(u"开始运行"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_button2, 0, wx.ALL, 5 )


        fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.Size( 250,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText91.Wrap( -1 )

        bSizer5.Add( self.m_staticText91, 0, wx.ALL, 5 )


        fgSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

        fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        bSizer9.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, _(u"停止程序"), wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
        bSizer9.Add( self.m_button7, 0, wx.ALL, 5 )
        self.m_button7.Disable()

        fgSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )


        fgSizer1.Add( fgSizer5, 1, wx.EXPAND, 5 )


        bSizer3.Add( fgSizer1, 1, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, _(u"结果"), wx.DefaultPosition, wx.Size( 250,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText38.Wrap( -1 )

        fgSizer4.Add( self.m_staticText38, 0, wx.ALL, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        fgSizer4.Add( self.m_textCtrl8, 0, wx.ALL, 5 )


        bSizer7.Add( fgSizer4, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.find_square)
        self.m_button7.Bind( wx.EVT_BUTTON, self.start_func )

        # 线程控制变量
        self.running = False
        self.worker_thread = None
    def __del__( self ):
        pass
    def start(self):
        """每分钟计算一次 1 + 1，后台线程任务"""
        num1=self.num1
        num2=self.num2
        while self.running:
            # 进行计算
            a=ma(30)-ma(120)
            result=str(a)
            self.m_textCtrl8.SetValue(result)
            print(f"计算的结果: {result}")
            time1=datetime.now()
            print("现在的时间是"+str(time1))
            if int(a) <= num2 and int(a) >= num1:
                current_time = datetime.now()
                wx.MessageBox(f"符合预期，现在的时间是{current_time}", "提示", wx.OK | wx.ICON_INFORMATION)
            # 等待 60 秒，但每次只 sleep 1 秒，检查 stop 信号
            #for _ in range(60):
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
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        # 打印两个数字
        print(f"第一个数字: {num1}")
        print(f"第二个数字: {num2}")
        if num2 < num1:
            wx.MessageBox(f"设置有误请重新输入", "提示", wx.OK | wx.ICON_INFORMATION)
            event.Skip()
            return
        else:
            print(num2-num1)
        """点击 Start 按钮时启动 find_square 方法"""
        if not self.running:
            self.running = True
            self.worker_thread = threading.Thread(target=self.start)
            self.worker_thread.start()
            self.m_button2.Disable()  # 启动后禁用 Start 按钮
            self.m_button7.Enable()    # 启动后启用 Stop 按钮
            wx.MessageBox(f"程序已开始运行", "提示", wx.OK | wx.ICON_INFORMATION)

    def start_func(self, event):

        """点击 Stop 按钮时停止 find_square 方法"""
        if self.running:
            self.running = False
            self.worker_thread.join()    # 等待线程结束
            self.m_button2.Enable()   # 停止后启用 Start 按钮
            self.m_button7.Disable()   # 停止后禁用 Stop 按钮
            wx.MessageBox(f"程序已停止运行", "提示", wx.OK | wx.ICON_INFORMATION)
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()

