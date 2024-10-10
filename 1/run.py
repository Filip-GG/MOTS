import numpy as np
import matplotlib.pyplot as plt

x, y = [np.arange(-10, 10, 0.3), np.arange(-10, 10, 0.3)] # два вектора для точек
x, y = np.meshgrid(x, y) # превратим векторы в плоскоть

iter = lambda item:[
                        np.max(data)
                        for data in list(zip(item[0], item[1]))
                    ]

z = np.matrix(
    [
        iter(data)
        for data in list(zip(np.abs(x), np.abs(y)))
    ]
) # Вычислим z по функции f

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='coolwarm')
fig.show()

print('Определитель Матрицы Z:', np.linalg.det(z))

input()