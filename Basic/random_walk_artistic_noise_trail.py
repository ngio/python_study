"""
랜덤 워크(Random Walk)를 사용하여 **아트적인 노이즈 트레일(Artistic Noise Trail)**을 만드는 것은 제너레이티브 아트(Generative Art)에서 매우 흔하고 흥미로운 기법입니다. 이는 각 단계에서 **무작위성(Stochasticity)**을 이용해 경로를 결정함으로써 예측 불가능하면서도 유기적인 움직임을 만들어냅니다.

파이썬에서는 주로 turtle 또는 **matplotlib**을 사용하여 시각화할 수 있지만, 여기서는 제너레이티브 아트에 자주 사용되는 접근 방식인 랜덤 증분을 이용해 구현해 보겠습니다.

"""


import numpy as np
import matplotlib.pyplot as plt

def generate_random_walk_trail(steps, noise_strength=1):
    """
    주어진 단계 수만큼 랜덤 워크 트레일 데이터를 생성합니다.
    
    :param steps: 랜덤 워크를 진행할 단계 수
    :param noise_strength: 노이즈/이동 강도 (클수록 경로가 거칠어짐)
    :return: x, y 좌표 배열
    """
    # 각 단계에서의 x, y 변화량 (랜덤 증분)을 생성합니다.
    # -noise_strength부터 +noise_strength 사이의 균일 분포 난수
    dx = np.random.uniform(-noise_strength, noise_strength, steps)
    dy = np.random.uniform(-noise_strength, noise_strength, steps)

    # 누적합을 계산하여 경로(트레일)를 만듭니다.
    # 각 지점은 이전 지점에서의 변화량을 누적한 결과입니다.
    x_trail = np.cumsum(dx)
    y_trail = np.cumsum(dy)
    
    return x_trail, y_trail

# --- 시각화 설정 ---
STEPS = 5000  # 경로 길이
NOISE_LEVEL = 1.5 # 노이즈 강도 조절

x_coords, y_coords = generate_random_walk_trail(STEPS, NOISE_LEVEL)

# Matplotlib으로 트레일 시각화
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x_coords, y_coords, 
        color='white',      # 선 색상
        linewidth=0.5,      # 선 두께
        alpha=0.8)          # 투명도

# 배경 및 축 설정
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title(f"Random Walk Artistic Noise Trail ({STEPS} steps)", color='white')

# 축 비율을 같게 설정하여 왜곡 방지
ax.set_aspect('equal', adjustable='box')

plt.show()
