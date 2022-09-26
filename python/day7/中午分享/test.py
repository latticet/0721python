"""
钟永佳
"""
import copy
list=[(1,2),[3,4]]
list1=copy.deepcopy(list)
print(id(list[0]), id(list1[0]))
