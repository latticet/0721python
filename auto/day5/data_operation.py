"""
数据操作类
    读取列表格式数据的方法：  [['xx','xx'],['xx','xx'],['xx','xx']]
    读取字典格式数据的方法:   [{'key1':'value1', 'kye2':'value2'},{'key1':'value1', 'kye2':'value2'},...]
"""
import pandas as pd
import os
from pprint import pprint


class DataOperation:
    def __init__(self, filename, sheet_name=0):
        # 获取操作文件的绝对路径
        file_path = os.path.join(os.path.abspath('data'), filename)

        # 获取文件名的后缀
        _, extension = os.path.splitext(filename)  # (文件名, 后缀)
        # 根据不同后缀进行不同处理
        if extension == '.csv':
            # 处理csv数据的方式: txt csv tsv
            self.data = pd.read_csv(file_path)
        else:
            # 处理excel数据的方式
            self.data = pd.read_excel(file_path, sheet_name)

    def get_data_to_list(self):
        """读取列表格式数据的方法"""
        return self.data.values.tolist()

    def get_data_to_dict(self):
        """读取字典格式数据的方法"""
        return [self.data.iloc[i].to_dict() for i in self.data.index.values]


if __name__ == '__main__':
    data_operation = DataOperation('lj_data.csv')
    # pprint(data_operation.get_data_to_list())
    pprint(data_operation.get_data_to_dict())
