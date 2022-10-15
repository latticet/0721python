import pandas as pd

# 读取数据csv数据
data = pd.read_csv('data/lj_data.csv')

# TODO data.loc
"""
print(data.head())
# 单行单列
# 广安门
print(data.loc[2, '区域'])
# 望京价格
print(data.loc[1, '价格'])
print(data.loc[1, ['区域', '价格']].values)

# 多行多列
# df.loc[[行标签1， 行标签2， ...], [列标签1， 列标签2, ...]]
print(data.loc[[2, 3, 4], ['区域', '价格']].values)
"""

# TODO data.iloc
# 单行单列
# 广安门
print(data.iloc[2, 0])
# 望京价格
print(data.iloc[1, 5])
# 望京：区域，价格
print(data.iloc[1, [0, 5]].values)

# 多行多列
# df.loc[[行标签1， 行标签2， ...], [列标签1， 列标签2, ...]]
# print(data.loc[[2, 3, 4], ['区域', '价格']].values)
print(data.iloc[[2, 3, 4], [0, 5]].values)


# 根据索引取整行数据
print(data.iloc[1].values)
