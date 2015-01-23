#Simuler en Python

_Ce document est librement inspiré [tutoriel NumPy de Nicolas Rougier](http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html) et est disponible sous licence Creative Commons Attribution 3.0 United States License (CC-by) http://creativecommons.org/licenses/by/3.0/us_


La simulation numérique (ou informatique) permet de représenter dans une machine (ordinateur) un phénomène écologique ou physique que l'on veut étudier à moindre coût et sans danger. On distingue généralement deux types de simulation: ``simulation continue`` et ``simulation discrète``. 

Le principe d'une ``simulation discrète`` d'un phénonème physique ou écologique consiste à représenter l'état initial de la simulation, puis ensuite de construire une fonction qui à partir d'un état précédent va déterminer l'état suivant de la simulation. 
L'application de cette fonction permet de passer du temps t0 au temps t1, puis t2, etc ... Généralement, on arrrête la simulation au bout d'un certain nombre d'application de la fonction (n) déterminé à l'avance. 

Au contraire une ``simulation continue`` permet de représenter de manière continue les changements d'un système physique ou biologique. Généralement on emploie pour cela, des [équations différentielles](http://fr.wikipedia.org/wiki/%C3%89quation_diff%C3%A9rentielle).

On ne va s'intéresser ici qu'à des simulations discrètes. Dans une simulation discrète, le temps est discrétisé en durée similaire. Chaque étape peut correspondre en fonction du phénomène considérée à une durée de 1 ms, 1s, 1 jour ou bien 1000 ans.

Nous allons illustrer ici ce principe au moyen d'une simulation sous la forme d'une simulation écologique appellée Jeu de la Vie représentant l'évolution de cellules qui naissent ou qui meurent au cours du temps.
##Phénomène à simuler: le Jeu de la Vie
Le [Jeu de la Vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) est un des premiers exemples d'automates cellulaires (voir figure ci-dessous) construit par John Conway en 1970. Ces automates cellulaires peuvent être considérés comme un tableau de cellules qui sont connectées les unes aux autres par la notion de voisinage.

Ce "jeu" est un fait un jeu à zéro joueur, car son évolution est déterminé uniquement par son état inital et ne nécessite pas d'entrées de joueurs humains. La seule façon d'interagir avec un Jeu de la Vie est de créer une configuration initiale et d'observer comment elle évolue au cours du temps.

L'univers (ou l'état) du Jeu de la Live est une grille à deux dimensions de taille infinie, composé de cellules carrées. Chaque cellule peut contenir l'un des deux états possibles: vivant ou mort, que l'on représente par les valeurs entières 0 ou 1.

![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/game-of-life.png)
Chaque cellule interagit avec ces 8 voisins, qui sont les cellules directement adjacentes horizontalement, verticalement et en diagonale. A chaque étape du temps, les règles suivantes vont s'appliquer : 

1. Une cellule vivante avec moins de deux voisines vivantes, meurt d'isolement,
2. Une cellule vivante avec plus de 3 cellules voisines vivantes, meurt d'étouffement,
3. Une cellule vivante avec 2 ou 3 cellules voisines vivantes, reste inchangée à la prochaine génération,
4. Une cellule morte avec exactement 3 cellules vivantes, devient une cellule vivante.L'état de départ est constitué par une forme initiale. La première génération est créér en appliquant les règles ci-dessus simultanément à toutes les cellules de l'état de départ: naissances et morts sont effectués simultanément, and le moment où cela se déroule est appellé tick (de simulation). Les règles continuent d'être appliquées pour créer les futures générations.

Pour commencer, nous allons utiliser un état de départ très simple, appellé "planeur" (glider) qui est connu pour se déplacer diagonalement au bout de 4 itérations comme indiqué ci-dessous : 

![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/glider-00.png)
![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/glider-01.png)
![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/glider-02.png)
![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/glider-03.png)
![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/glider-04.png)
![image](http://www.labri.fr/perso/nrougier/teaching/numpy/figures/glider-05.png)

Cette propriété va nous permettre de débogguer visuellement plus facilement nos programmes.

La première question à se poser pour faire cette simulation est comment représenter un état, ici l'ensemble des cellules à un instant donné. En Python, il est possible d'utiliser le type list ou array pour représenter des tableaux a une ou plusieurs dimensions.

La bibliothèque scientifique ``NumPy`` est une alternative qui permet de manipuler très efficacemment des tableaux de grande taille en Python: http://www.numpy.org/
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
>>> print cells[1:5,1:5]
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

```python
>>> print(cells.base)
None
>>> print(a.base is cells)
True
```

N'oublions pas de remettre la valeur de a[0,0] à 0 :

```python
>>> a[0,0] = 0
```

### Compter les voisins
Nous avons besoin d'une fonction pour compter les voisins d'une cellule. Nous pourrions utiliser des tableaux ou listes Python, mais du fait des boucles imbriquées nécessaires, le programme serait plutôt lent (vous pouvez refaire le code en utilisant des tableaux Python standard pour faire la comparaison). Nous allons utiliser des opérations qui portent sur l'ensemble du tableau, plutôt que faire des itérations, ce que l'on appelle la **vectorisation**.

Avec NumPy, il est possible de manipuler ``cells`` comme un scalaire normal sans manipuler chacun des éléments du tableau :

```python
>>> print (1+(2*cells+3))
[[4 4 4 4 4 4]
 [4 4 4 6 4 4]
 [4 6 4 6 4 4]
 [4 4 6 6 4 4]
 [4 4 4 4 4 4]
 [4 4 4 4 4 4]]
```

Si vous regardez attentivement la sortie, vous réaliserez qu'elle correspond à l'application de la forme sur chacun des éléments du tableau pris séparemment.

Construisons un tableau ``neighbours`` de même taille que le tableau ``cells`` contenant à la position [i,j] le nombre de voisins vivants de la case [i,j] dans ``cells`` :


```python
>>> neighbours = np.zeros(cells.shape, dtype=int)
>>> neighbours[1:-1,1:-1] += (cells[ :-2, :-2] + cells[ :-2,1:-1] + cells[ :-2,2:] +
                              cells[1:-1, :-2]                    + cells[1:-1,2:] +
                              cells[2:  , :-2] + cells[2:  ,1:-1] + cells[2:  ,2:])
>>> neighbours
array([[0, 0, 0, 0, 0, 0],
       [0, 1, 3, 1, 2, 0],
       [0, 1, 5, 3, 3, 0],
       [0, 2, 3, 2, 2, 0],
       [0, 1, 2, 2, 1, 0],
       [0, 0, 0, 0, 0, 0]])
```

**Question: Que fait la fonction ``np.zeros()`` ?**
                     
###Faire des itérations

Construisons la fonction ``iterate`` qui permet d'application les règles sur ``cells`` pour produire une nouvell génération.

Pour cela, on va utiliser la fonction ``np.ravel()`` qui permet d'aplatir un tableau multi-dimensionnels en tableau à une dimension :

```python
>>> np.ravel(cells)
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```

Voir la documentation ici : http://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html?highlight=ravel#numpy.ravel


et la fonction ``np.argwhere()`` (voir documentation ici : http://docs.scipy.org/doc/numpy/reference/generated/numpy.argwhere.html) :

```python
>>> def iterate(cells):
    	# Iterate the game of life
    	# Count neighbours
    	neighbours = np.zeros(cells.shape, dtype=int)
    	n[1:-1,1:-1] += (cells[0:-2,0:-2] + cells[0:-2,1:-1] + cells[0:-2,2:] +
                         cells[1:-1,0:-2]                    + cells[1:-1,2:] +
                         cells[2:  ,0:-2] + cells[2:  ,1:-1] + cells[2:  ,2:])
    	n1 = n.ravel()
    	Z_ = cells.ravel()
    	# Apply rules
    	rule1 = np.argwhere( (Z_==1) & (n1 < 2) )
    	rule2 = np.argwhere( (Z_==1) & (n1 > 3) )
    	rule3 = np.argwhere( (Z_==1) & ((n1==2) | (n1==3)) )
    	rule4 = np.argwhere( (Z_==0) & (n1==3) )
    	
    	# Set new values
    	Z_[rule1] = 0
    	Z_[rule2] = 0
    	Z_[rule3] = Z_[rule3]
    	Z_[rule4] = 1

    	# Make sure borders stay null
    	cells[0,:] = cells[-1,:] = cells[:,0] = cells[:,-1] = 0
```


**Question: pourquoi on fait en sorte à la fin de la fonction de mettre les bords de l'automate à zéro ?**

## Lancer une simulation
Essayons de lancer le Jeu de la Vie sur une grille beaucoup plus grande.
Pour cela générons une grille rempli de 0 et 1 placée de manière aléatoire.

La bibliothèque ``random`` permet de générer des nombres aléatoires.
Voir documentation ici: https://docs.python.org/3/library/random.html

Quelques unes des fonctions les plus utiles:

* ``random.seed()`` : permet d'initialiser le générateur de nombres aléatoires
* ``random.random()`` : retourne un nombre réél aléatoire dans l'intervalle [0, 1]
* ``random.randrange(a,b)``: retourne un nombre entier compris entre a et b (inclus).

**Question: Pourquoi les nombres générés par cette bibliothèque sont des nombres pseudo-aléatoires ?**

La bibliothèque NumPy complète la bibliothèque ``random`` par des fonctions comme la fonction ``np.random.randint`` (voir documentation ici : http://docs.scipy.org/doc/numpy/reference/routines.random.html) :

```python
>>> cells = np.random.randint(0, 2, (256,512))
```

Effectuons 100 itérations :

```python
>>> for i in range(100): iterate(cells)
```

et affichons les résultats : 

```python
>>> size = np.array(cells.shape)
>>> dpi = 72.0
>>> figsize= size[1]/float(dpi),size[0]/float(dpi)
>>> fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
>>> fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
>>> plt.imshow(cells,interpolation='nearest', cmap=plt.cm.gray_r)
>>> plt.xticks([]), plt.yticks([])
>>> plt.show()
```

## Exercice: Estimation de pi
Imaginons une cible représentée par un disque de rayon r (donc de surface π*r^2). Cette cible est incluse dans un carré de côté 2r (donc de surface (2r)^2). Pour estimer nous allons jeter au hasard des fléchettes dans ce carré. La probabilité qu’une fléchette tombe sur la cible est donc π. En jetant un grand nombre de fléchettes nous aurons donc une estimation de π!Ecrire le script Python qui permet de réaliser cette estimation.
