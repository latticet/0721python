"""
语法：
from 包[.包.n].模块 import 资源1 [as 别名], 资源2 [as 别名], .
"""
from package1.module1 import name, fn1
from package2.package_a.module_a1 import name as a1_name

print(name)
print(a1_name)
fn1()


