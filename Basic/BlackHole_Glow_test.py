import matplotlib.pyplot as plt, numpy as np
plt.style.use("dark_background")
O = np.linspace(0, 10*np.pi, 2000)
r = 1/(1+0.2*O)
x, y = r*np.cos(O), r*np.sin(O)
plt.scatter(x, y, c=O, cmap="magma", s=3)
plt.axis("equal");
plt.show()
