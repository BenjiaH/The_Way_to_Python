# -*- coding: utf-8 -*-

import os
import stat

# 将os_chmod.py文件改为只读
os.chmod("11.OS_chmod.py", stat.S_IREAD)
# 判断是否可写
ret = os.access("11.OS_chmod.py", os.W_OK)
print("os.W_OK - 返回值:", ret)