import pandas as pd

# 读取数据csv数据
# data = pd.read_excel('资源路径', 'sheet名称')
data = pd.read_excel('data/sales.xlsx', '2018')

# data.head(n) 查看前n行, 默认查看前5行
print(data.head(3))

# 查看数据的形状，返回（行、列）
print(data.shape)

# 查看字段名
print(data.columns)

# 查看索引
print(data.index)







