"""
랜덤 워크(Random Walk)를 사용하여 **아트적인 노이즈 트레일(Artistic Noise Trail)**을 만드는 것은 제너레이티브 아트(Generative Art)에서 매우 흔하고 흥미로운 기법입니다. 이는 각 단계에서 **무작위성(Stochasticity)**을 이용해 경로를 결정함으로써 예측 불가능하면서도 유기적인 움직임을 만들어냅니다.

파이썬에서는 주로 turtle 또는 **matplotlib**을 사용하여 시각화할 수 있지만, 여기서는 제너레이티브 아트에 자주 사용되는 접근 방식인 랜덤 증분을 이용해 구현해 보겠습니다.

"""


import numpy as np
import matplotlib.pyplot as plt

steps = np.random.choice([1, -1], size=(2,1000))
pos = np.cumsum(steps, axis=1)
plt.plot(pos[0], pos[1], color='lime')
plt.axis('off')
plt.title("Random walk path", color='green')
plt.show()
