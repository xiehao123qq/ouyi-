import requests
import pandas as pd

def ma(zhouqi):
    base_url = 'https://www.okx.com/api/v5/market/candles'
    params = {
    'instId': 'BTC-USDT',  # 产品ID，如 BTC-USDT
    'bar': '1Dutc',           # 时间粒度（1天K线）
    'limit': '500'    # 获取100条数据（确保覆盖30天）

            }
    response = requests.get(base_url, params=params)
        # 获取数据并转换为DataFrame
    if response.status_code == 200:
        data = response.json()['data']
        print(data)
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
        print(f"数据长度: {len(df)}")
        print(f"日期范围: {df['ts'].min()} 到 {df['ts'].max()}")
        df.sort_values(by='ts', ascending=True, inplace=True)

    # 打印完整数据以检查
        print(df[['ts', 'close']])
    # 计算MA30
        df['MA'] = df['close'].rolling(window=zhouqi).mean()

    # 输出时间、收盘价和MA30
        print(df[['ts', 'close', 'MA']].tail(10))
        return 1

    else:
        print(f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}")

aaa=ma(5)