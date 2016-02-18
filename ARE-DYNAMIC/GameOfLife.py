import numpy as np

cells = np.random.randint(0, 2, (512,1024))

def iterate(cells):
    # Itérer le jeu de la vie
    # Compter les voisins
    n = np.zeros(cells.shape, dtype=int)
    n[1:-1,1:-1] += (cells[0:-2,0:-2] + cells[0:-2,1:-1] + cells[0:-2,2:] +
                     cells[1:-1,0:-2]                    + cells[1:-1,2:] +
                     cells[2:  ,0:-2] + cells[2:  ,1:-1] + cells[2:  ,2:])
    n1 = n.ravel()
    cells1 = cells.ravel()
    # Appliquer les règles
    rule1 = np.argwhere( (cells1==1) & (n1 < 2) )
    rule2 = np.argwhere( (cells1==1) & (n1 > 3) )
    rule3 = np.argwhere( (cells1==1) & ((n1==2) | (n1==3)) )
    rule4 = np.argwhere( (cells1==0) & (n1==3) )

    # Modifier les cellules
    cells1[rule1] = 0
    cells1[rule2] = 0
    cells1[rule3] = cells1[rule3]
    cells1[rule4] = 1

    # Faire en sorte que les bords soient nuls
    cells[0,:] = cells[-1,:] = cells[:,0] = cells[:,-1] = 0

import matplotlib.pyplot as plt
size = np.array(cells.shape)
dpi = 72.0
figsize= size[1]/float(dpi),size[0]/float(dpi)
fig = plt.figure(figsize = figsize, dpi = dpi, facecolor = "white")
fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon = False)
im=plt.imshow(cells, interpolation = 'nearest', cmap = plt.cm.gray_r)
plt.xticks([]), plt.yticks([])

for i in range(100):
    iterate(cells)

plt.show()

# import matplotlib.animation as animation
#
# def update(*args):
#     iterate(cells)
#     im.set_array(cells)
#     return im,
#
# ani = animation.FuncAnimation(fig, update, frames=range(20), interval=50)
# plt.show()
