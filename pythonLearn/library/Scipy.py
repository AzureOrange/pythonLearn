# -*- coding:utf-8 -*-

# 是一种使用Numpy 来做高等数据、信号处理、优化、统计的扩展包

import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]])

# 计算矩阵的行列式
print(linalg.det(A))
