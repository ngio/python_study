import matplotlib.pyplot as plt
import numpy as np

# 임의의 데이터
theta = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])  # 각도 데이터
r = np.array([1, 2, 3, 4, 5])                              # 반경 데이터

# Polar plot 생성
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, marker='o')

# 플롯 설정
ax.set_title("Custom Data Polar Plot", va='bottom')
plt.show()