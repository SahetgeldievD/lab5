import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_tetrahedron(ax, shift, scale):
    vertices = np.array([[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]]) * scale + shift
    faces = [[vertices[j] for j in [0, 1, 2]], [vertices[j] for j in [0, 1, 3]], 
             [vertices[j] for j in [0, 2, 3]], [vertices[j] for j in [1, 2, 3]]]
    poly3d = Poly3DCollection(faces, edgecolors='r', linewidths=1, alpha=0.5)
    ax.add_collection3d(poly3d)

def plot_octahedron(ax, shift, scale):
    vertices = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]) * scale + shift
    faces = [[vertices[j] for j in [0, 2, 4]], [vertices[j] for j in [0, 3, 4]], 
             [vertices[j] for j in [1, 2, 4]], [vertices[j] for j in [1, 3, 4]], 
             [vertices[j] for j in [0, 2, 5]], [vertices[j] for j in [0, 3, 5]], 
             [vertices[j] for j in [1, 2, 5]], [vertices[j] for j in [1, 3, 5]]]
    poly3d = Poly3DCollection(faces, edgecolors='b', linewidths=1, alpha=0.5)
    ax.add_collection3d(poly3d)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_tetrahedron(ax, np.array([2, 0, 0]), 2)
plot_octahedron(ax, np.array([-2, 0, 0]), 2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_title('Тетраэдр и октаэдр')
plt.show()
