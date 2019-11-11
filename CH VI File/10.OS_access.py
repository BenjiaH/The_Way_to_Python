# -*- coding: utf-8 -*-

import os
import sys

ret = os.access(".", os.F_OK | os.R_OK | os.W_OK | os.X_OK)
print("os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值:", ret)
ret = os.access("10.OS_access.py", os.F_OK | os.R_OK | os.W_OK)
print("os.F_OK|os.R_OK|os.W_OK - 返回值:", ret)
