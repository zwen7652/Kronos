import qlib
from qlib.data import D
import pandas as pd

# 假设你的 qlib 数据目录默认在 ~/.qlib/qlib_data/cn_data
qlib.init(provider_uri="~/.qlib/qlib_data/cn_data", region="cn")

# 随便挑一只股票，比如上证指数或者平安银行
symbols = ["SH600000"]

# 获取它所有的收盘价日期
df = D.features(symbols, ['$close'])
if not df.empty:
    print(f"股票 {symbols[0]} 的起始日期: {df.index.get_level_values('datetime').min()}")
    print(f"股票 {symbols[0]} 的结束日期: {df.index.get_level_values('datetime').max()}")
else:
    print("没有获取到数据，可能是 provider_uri 路径不对，请检查。")

