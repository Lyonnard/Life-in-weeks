import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 52, 52+1)
y = np.linspace(0, 90, 90+1)

X, Y = np.meshgrid(x, y)
QP = plt.scatter(X, Y,marker='s',markerstyle='none') #FIXME fill style is broken 
plt.grid()
plt.show()