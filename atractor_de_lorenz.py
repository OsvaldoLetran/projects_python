import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D


rho = 28.0     # desde rho = 25 hasta rho = 90
sigma = 10.0
beta = 8.0 / 3.0


def f(state, t):
    x, y, z = state  # Desempaqueta el vector de estado
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivadas

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

# odeint() resuelve EDOs de primer orden. syntax: odeint(func, valor_inicial, t)
# devuelve una matriz
states = odeint(f, state0, t)

fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
ax = plt.axes(projection = '3d')
ax.plot(states[:, 0], states[:, 1], states[:, 2])
# states[:,0] selecciona todas las filas de la 1er columna de states
plt.show()
