import numpy as np
import random
import matplotlib
import matplotlib.pyplot as pyplot


def generate_forest(n, m, density):
    number_of_trees = int(n*m*density)
    forest_list = []
    forest = np.zeros([n, m])
    if number_of_trees != 0 :
        for i in range(forest.shape[0]):
            for j in range(forest.shape[1]):
                forest_list.append([i, j])
        arbre_feu = random.randint(0, number_of_trees-1)
        for i in range(number_of_trees):
            tirageListe = random.randint(0, len(forest_list)-1)
            position =  forest_list[tirageListe]
            forest_list.remove(position)
            if i == arbre_feu:
                forest[position[0],position[1]] = 2
            else:
                forest[position[0],position[1]] = 1
    return forest

def iterate(cells):
    n = cells.shape[0]
    m = cells.shape[1]
    cellsNew = np.copy(cells)
    for i in range(n):
        for j in range(m):
            if cells[i,j] == 1:
                if(cells[(i-1) % n,j]==2 or cells[(i+1)%n,j]==2 or cells[i,(j-1)%m]==2 or cells[i,(j+1)%m]==2):
                    cellsNew[i,j] = 2
            if cells[i,j] == 2:
                cellsNew[i,j] = 3
    return cellsNew

def simulation(n, m, d):
    forest = generate_forest(n, m, d)
    while 2 in forest:
        forest = iterate(forest)
    return forest

def burn_trees_ratio(forest):
    ashes_number = 0
    trees_number = 0
    n = forest.shape[0]
    m = forest.shape[1]
    for i in range(n):
        for j in range(m):
            if forest[i,j] == 3:
                ashes_number = ashes_number + 1
            if forest[i,j] == 1:
                trees_number = trees_number + 1
    if trees_number+ashes_number == 0 :
        return 0

    return ashes_number/(trees_number+ashes_number)

def n_simulation(number_simulations, n, m, d):
    results = np.zeros([number_simulations])
    for i in range(number_simulations):
        forest = simulation(n,m,d)
        results[i]= burn_trees_ratio(forest)
    return results

x = np.linspace(0, 1, 10)
y = [np.mean(n_simulation(10, 30, 30, d)) for d in x]
pyplot.plot(x,y)
pyplot.suptitle('Pourcentage arbres brulés en fonction de la densité')
pyplot.xlabel('Densité')
pyplot.ylabel('Pourcentage des arbres brulés')
pyplot.show()

