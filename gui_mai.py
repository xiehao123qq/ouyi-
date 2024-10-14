import wx
import threading
import time


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # 创建 Panel
        panel = wx.Panel(self)

        # 创建 Start 和 Stop 按钮
        self.start_button = wx.Button(panel, label="Start", pos=(10, 10))
        self.stop_button = wx.Button(panel, label="Stop", pos=(100, 10))
        self.stop_button.Disable()  # 初始状态下停止按钮不可用

        # 绑定按钮事件
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start)
        self.stop_button.Bind(wx.EVT_BUTTON, self.on_stop)

        # 线程控制变量
        self.running = False
        self.worker_thread = None

    def find_square(self):
        """需要后台运行的方法"""
        while self.running:
            print("Running find_square method...")
            time.sleep(1)  # 模拟需要持续运行的工作

    def on_start(self, event):
        """点击 Start 按钮时启动 find_square 方法"""
        if not self.running:
            self.running = True
            self.worker_thread = threading.Thread(target=self.find_square)
            self.worker_thread.start()
            self.start_button.Disable()  # 启动后禁用 Start 按钮
            self.stop_button.Enable()  # 启动后启用 Stop 按钮

    def on_stop(self, event):
        """点击 Stop 按钮时停止 find_square 方法"""
        if self.running:
            self.running = False
            self.worker_thread.join()  # 等待线程结束
            self.start_button.Enable()  # 停止后启用 Start 按钮
            self.stop_button.Disable()  # 停止后禁用 Stop 按钮


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Start and Stop Example", size=(300, 100))
        frame.Show()
        return True


# 启动应用程序
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
