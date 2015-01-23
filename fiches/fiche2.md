#Faire une simulation en Python

Le principe de toute ``simulation informatique`` d'un phénonème physique ou écologique consiste à représenter l'état initial de la simulation, puis ensuite de construire une fonction qui à partir d'un état précédent va déterminer l'état suivant de la simulation. L'application de cette fonction permet de passer du temps t0 au temps t1, puis t2, etc ... Généralement, on arrrête la simulation au bout d'un certain nombre d'application de la fonction (n) détermniné à l'avance.

Chaque étape peut correspondre en fonction du phénomène considérée à une durée de 1 ms, 1s, 1 jour ou bien 1000 ans.

Nous allons illustrer ici ce principe au moyen d'une simulation sous la forme d'un jeu (appellé Jeu de la Vie) représentant des cellules qui naissent ou qui meurent au cours du temps.
##Phénomène à simuler: le Jeu de la Vie
Le Jeu de la Vie est un des premiers exemples d'automates cellulaires (voir figure ci-dessous) construit par John Conway en 1970. Ces automates cellulaires peuvent être considérés comme un tableau de cellules qui sont connectées les unes aux autres par la notion de voisinage.

Ce "jeu" est un fait un jeu à zéro joueur, car son évolution est déterminé uniquement par son état inital et ne nécessite pas d'entrées de joueurs humains. La seule façon d'interagir avec un Jeu de la Vie est de créer une configuration initiale et d'observer comment elle évolue au cours du temps.
L'univers (ou l'état) du Jeu de la Live est une grille à deux dimensions de taille infini, composé de cellules carrées. Chaque cellule peut contenir l'un des deux états possibles: vivant ou mort, que l'on représente par les valeurs entières 0 ou 1.
Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if by needs caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed – births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.

We'll first use a very simple setup and more precisely, we'll use the glider pattern that is known to move one step diagonally in 4 iterations as illustrated below:

Cette propriété va nous permettre de débogguer plus facilement nos programmes.

La première question à se poser pour faire cette simulation est comment représenter un état, ici l'ensemble des cellules à un instant donné. En Python, il est possible d'utiliser le type list ou array pour représenter des tableaux a une ou plusieurs dimensions.

La bibliothèse scientifique ``NumPy`` est une alternative qui permet de manipuler très efficacemment des tableaux de grande taille en Python: http://www.numpy.org/
La première chose à faire est de créer un tableau NumPy afin de contenir les cellules (``cells``). Ceci peut être fait facilement de la façon suivante :

```python
>>> import numpy as np
>>> cells = np.array([[0,0,0,0,0,0],
              [0,0,0,1,0,0],
              [0,1,0,1,0,0],
              [0,0,1,1,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0]])
```

Il existe de nombreuses autres façons de créer un tableau NumPy : http://docs.scipy.org/doc/numpy/reference/routines.array-creation.html

Notez que nous n'avons pas spécifié le type des données contenues dans le tableau, NumPy a choisi pour nous. Comme tous les éléments sont des entiers, NumPy a choisi le type entier (integer). Ceci peut se vérifier facilement :

```python
>>> print(cells.dtype)
int64```

On peut facilement vérifier la taille d'un tableau, ici par exemple 6x6 :

```python
>>> print(cells.shape)
(6, 6)
```
Chaque élément de ``cells`` peut être accédé en utilisant un index de ligne et de colonne (en suivant cet ordre) :

```python
>>> print cells[0,5]
0
```

Il est également possible d'accéder à une sous-partie d'un tableau, en utilsant la notation dite slice :

```python
>>> print Z[1:5,1:5]
[[0 0 1 0]
 [1 0 1 0]
 [0 1 1 0]
 [0 0 0 0]]
```

Dans l'exemple ci-dessous, nous avons extrait une sous-partie de ``cells`` de la ligne 1 à 5 et de la collonne 1 à 5. Il est important de bien comprendre qu'il s'agit vraiment d'une sous-ensemble de ``cells`` dans le sens où chaque modification de la sous-partie va avoir un impact direct sur ``cells`` :

```python
>>> a = cells[1:5,1:5]
>>> a[0,0] = 9
>>> print(a)
[[9 0 1 0]
 [1 0 1 0]
 [0 1 1 0]
 [0 0 0 0]]

>>> print(cells)
[[0 0 0 0 0 0]
 [0 9 0 1 0 0]
 [0 1 0 1 0 0]
 [0 0 1 1 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]]
```

Nous avons modifié la valeur de ``a[0,0]`` à 9 et nous voyons un changement immédiat dans ``cells[1,1]`` parce que ``a[0,0]`` correspond à ``cells[1,1]``. Ceci peut paraître trivial avec des tableaux si simples, mais les choses peuvent devenir plus complexe comme nous le verrons plus tard. En cas de doute, il possible de vérifier rapidement, si un tableau est une partie d'un autre :

```print
>>> print(cells.base is None)
True
>>> print(a.base is cells)
True
```

### Compter les voisins
Nous avons besoin d'une fonction pour compter les voisins d'une cellule. Nous pourrions utiliser des tableaux ou listes Python, mais du fait des boucles imbriquées nécessaires, le programme serait plutôt lent (vous pouvez refaire le code en utilisant des tableaux Python standard pour faire la comparaison). Nous allons utiliser des opérations qui portent sur l'ensemble du tableau, plutôt que faire des itérations, ce que l'on appelle la **vectorisation**.

Avec NumPy, il est possible de manipuler ``cells`` comme un scalaire normal sans manipuler chacun des éléments du tableau :

```print
>>> print (1+(2*cells+3))
[[4 4 4 4 4 4]
 [4 4 4 6 4 4]
 [4 6 4 6 4 4]
 [4 4 6 6 4 4]
 [4 4 4 4 4 4]
 [4 4 4 4 4 4]]
```

If you look carefully at the output, you may realize that the ouptut corresponds to the formula above applied individually to each element. Said differently, we have ``(1+(2*z+3))[i,j] == (1+(2*z[i,j]+3))`` for any i,j.

Ok, so far, so good. Now what happens if we add z with one of its subpart, let's say z[-1:1,-1:1] ?

```
>>> z + z[-1:1,-1:1]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>

ValueError: operands could not be broadcast together with shapes (6,6) (4,4)
```

This raises a Value Error, but more interestingly, numpy complains about the impossibility of broadcasting the two arrays together. Broadcasting is a very powerful feature of numpy and most of the time, it saves you a lot of hassle. Let's consider for example the following code:

```
>>> print(z+1)
[[1 1 1 1 1 1]
 [1 1 1 2 1 1]
 [1 2 1 2 1 1]
 [1 1 2 2 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]]
```

###Faire des itérations

```
def iterate(cells):
    # Iterate the game of life : naive version
    # Count neighbours
    N = np.zeros(cells.shape, int)
    N[1:-1,1:-1] += (cells[0:-2,0:-2] + cells[0:-2,1:-1] + cells[0:-2,2:] +
                     cells[1:-1,0:-2]                + cells[1:-1,2:] +
                     cells[2:  ,0:-2] + cells[2:  ,1:-1] + cells[2:  ,2:])
    N_ = N.ravel()
    Z_ = cells.ravel()

    # Apply rules
    R1 = np.argwhere( (Z_==1) & (N_ < 2) )
    R2 = np.argwhere( (Z_==1) & (N_ > 3) )
    R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
    R4 = np.argwhere( (Z_==0) & (N_==3) )

    # Set new values
    Z_[R1] = 0
    Z_[R2] = 0
    Z_[R3] = Z_[R3]
    Z_[R4] = 1

    # Make sure borders stay null
    cells[0,:] = cells[-1,:] = cells[:,0] = cells[:,-1] = 0
```


Pourquoi on fait en sorte à la fin de la fonction de mettre les bords de l'automate à zéro ?




## Tirage de nombre aléatoire
La bibliothèque ``random`` permet de générer des nombres aléatoires.
Voir documentation ici: https://docs.python.org/3/library/random.html

Quelques unes des fonctions les plus utiles:

* ``random.seed()`` : permet d'initialiser le générateur de nombres aléatoires
* ``random.random()`` : retourne un nombre réél aléatoire dans l'intervalle [0, 1]
* ``random.randrange(a,b)``: retourne un nombre entier compris entre a et b (inclus).

Pourquoi les nombres générés par cette bibliothèque sont des nombres pseudo-aléatoires ?

## Exercice: Estimation de pi
Imaginons une cible représentée par un disque de rayon r (donc de surface π*r^2). Cette cible est incluse dans un carré de côté 2r (donc de surface (2r)^2). Pour estimer nous allons jeter au hasard des fléchettes dans ce carré. La probabilité qu’une fléchette tombe sur la cible est donc π. En jetant un grand nombre de fléchettes nous aurons donc une estimation de π!Ecrire le script Python qui permet de réaliser cette estimation.
