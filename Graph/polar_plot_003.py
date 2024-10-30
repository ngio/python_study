import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (예: Windows에서는 'Malgun Gothic', MacOS에서는 'AppleGothic')
plt.rcParams['font.family'] = 'Malgun Gothic'  # 또는 'AppleGothic' (Mac)
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 기호 깨짐 방지

# 데이터 준비
angles = np.linspace(0, 2 * np.pi, 100)  # 각도 (0에서 2π까지)
radii = 1 + np.sin(angles)  # 반지름

# Polar Plot 생성
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(angles, radii, color='blue', linewidth=2)

# 플롯 설정
ax.set_title("예제 Polar Plot", va='bottom')
#plt.show()


# 예시: 다중 polar plot
for i in range(1, 4):
    radii = i + np.sin(angles * i)
    ax.plot(angles, radii, label=f'Plot {i}')

ax.legend(loc='upper right')
plt.show()
