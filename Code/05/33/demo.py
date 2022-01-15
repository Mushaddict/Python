import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
fig = plt.figure()
axes3d = Axes3D(fig)
zs = [1, 5, 10, 15, 20]
for z in zs:
    x = np.arange(0, 10)
    y = np.random.randint(0, 30, size=10)
    axes3d.bar(x, y, zs=z, zdir='x', color=['r', 'green', 'yellow', 'c'])
plt.show()
