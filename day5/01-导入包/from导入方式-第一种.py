# 第一种
# from 包[.包.n] import 模块1 [as 别名], 模块2 [as 别名], ...

from package1 import module1, module2 as m2
from package2.package_a import module_a1
from package2.package_b import module_b1


# print(module1.name)
# print(m2.name)


print(module_a1.name)
print(module_b1.name)

import sys
import pprint
pprint.pprint(sys.path)
