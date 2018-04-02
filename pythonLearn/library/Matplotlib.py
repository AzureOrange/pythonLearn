# -*- coding:utf-8 -*-

# 绘图库

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.plot([1, 2, 3])

plt.ylabel("some numbers")

plt.show()

sns.set(color_codes=True)
x = np.random.normal(size=100)
sns.distplot(x)

