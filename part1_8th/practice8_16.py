# 8-16 导入：
# 选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它：

import printing_functions
from printing_functions import print_info
from printing_functions import print_info as pi
import printing_functions as pf
from printing_functions import *

printing_functions.print_info([1,2,3])
print_info([1,2,3])
pi([1,2,3])
pf.print_info([1,2,3])