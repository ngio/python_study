"""
파이썬을 사용하여 제너레이티브 지오메트리(generative geometry)를 위한 
 보로노이 다이어그램(Voronoi diagram)을 생성하는 것은 널리 사용되는 강력한 기법입니다. 
이 과정은 일련의 무작위 점을 생성한 다음, SciPy와 같은 라이브러리를 사용하여 
 이 점들에 대한 근접성에 따라 평면을 분할하는 보로노이 다이어그램을 계산하는 것을 포함합니다.
이렇게 분할된 공간은 복잡하고 유기적으로 보이는 디자인을 만드는 데 사용될 수 있습니다.
"""

import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# 1. Generate 20 random 2D points
points = np.random.rand(20, 2)

# 2. Compute the Voronoi diagram
vor = Voronoi(points)

# 3. Plot the diagram
fig = voronoi_plot_2d(vor)
plt.show()
