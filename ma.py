import threading
from tkinter import Tk, Button, Label

import requests
import pandas as pd
import wx
import os
os.environ["http_proxy"] = "http://127.0.0.1:7897"
os.environ["https_proxy"] = "http://127.0.0.1:7897"
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

def ma(zhouqi,parent=None):
    base_url = 'https://www.okx.com/api/v5/market/candles'
    params = {
    'instId': 'BTC-USDT-SWAP',  # 产品ID，如 BTC-USDT
    'bar': '1m',           # 时间粒度（1天K线）
    'limit': '500'    # 获取100条数据（确保覆盖30天）

            }
    try:
        response = requests.get(base_url, params=params,timeout=10)
            # 获取数据并转换为DataFrame
        if response.status_code == 200:
            data = response.json()['data']
           # print(data)
        # 将数据转换为DataFrame
            df = pd.DataFrame(data,
            columns=['ts', 'open', 'high', 'low', 'close', 'volume', 'volCcy', 'volCcyQuote', 'confirm'])

        # 转换时间戳
            df['ts'] = pd.to_numeric(df['ts'], errors='coerce')
            df['ts'] = pd.to_datetime(df['ts'], unit='ms')
            df['ts'] = df['ts'].dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')

        # 将 'close' 列转换为数值类型
            df['close'] = pd.to_numeric(df['close'], errors='coerce')

        # 检查数据长度和日期范围
           # print(f"数据长度: {len(df)}")
            #print(f"日期范围: {df['ts'].min()} 到 {df['ts'].max()}")
            df.sort_values(by='ts', ascending=True, inplace=True)

        # 打印完整数据以检查
          #  print(df[['ts', 'close']])
        # 计算MA
            df['MA'] = df['close'].rolling(window=zhouqi).mean()

        # 输出时间、收盘价和MA30
           # print(df[['ts', 'close', 'MA']].tail(1))
            ma=df['MA'].tail(1).values[0]
           # print(ma)
            return ma

        else:
            print(f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        mes="请求超时，"+"\n\n\n"+"请检查网络连接"+"\n\n"+"或代理是否正常配置"
        #wx.MessageBox("请求超时，请检查网络连接或代理是否正常配置。", "网络错误", wx.OK | wx.ICON_ERROR, parent)
        threading.Thread(target=show_custom_message1, args=(mes,)).start()
        print(e)
        return None
#aaa=ma(120)