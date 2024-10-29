import matplotlib.pyplot as plt
import numpy as np

# 각도 (theta)와 반경 (r) 값 생성
theta = np.linspace(0, 2 * np.pi, 100)  # 0에서 2π 사이의 각도 값
r = 1 + np.sin(3 * theta)               # 반경 값은 특정 함수로 정의

# Polar plot 생성
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)       # polar=True 옵션으로 polar plot 생성
ax.plot(theta, r)

# 플롯 설정
ax.set_title("Polar Plot Example", va='bottom')
plt.show()