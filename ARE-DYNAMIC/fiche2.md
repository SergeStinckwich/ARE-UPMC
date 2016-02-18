#Visualiser avec Python

_Ce document est librement inspiré [tutoriel NumPy de Nicolas Rougier](http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html) et est disponible avec son autorisation sous licence Creative Commons Attribution 3.0 United States License (CC-by) http://creativecommons.org/licenses/by/3.0/us_

Lorsque l'on fait une simulation d'un phénomène physique, il est nécessaire de pouvoir visualiser graphiquement ce qui se passe. Une visualisation permet de comprendre et d'analyser plus facilement un phénomène.

[Matplotlib](http://matplotlib.org) est une bibliothèque du langage de programmation Python qui, combinée avec les bibliothèques de calcul scientifique ```NumPy``` et ```SciPy```, constitue un puissant outil pour tracer et visualiser des données issues de mesures ou bien de simulation.

## Utiliser Matplotlib pour tracer une fonction

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
plot(x, cosx)
plot(x, sinx)
show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_1.png)

La fonction ``linspace`` de la librairie ``NumPy`` (np) permet de générer un tableau de 256 valeurs réélles variant de -π à π (inclus).
`cosx` est un tableau de 256 valeurs contenant le résultat de l'application de la fonction ``cos(x)`` sur chacune des valeurs du tableau `x`.

## Valeurs d'affichage par défaut
La bibliothèque Matplotlib est fournie avec un jeu de paramètres par défaut qui permet de personnaliser toute sorte de propriétés. Vous pouvez contrôler les réglages par défaut de (presque) toutes les propriétés : taille du graphique, résolution en points par pouce (dpi), épaisseur du trait, couleurs, styles, vues, repères, grilles, textes, polices de caractères, etc. Bien que les réglages par défaut répondent à la plupart des cas courants, vous pourriez être amené à en modifier quelques-uns pour des cas plus spécifiques.

##Changer les caractéristiques du trait

Nous voulons changer la courbe du cosinus en bleu et le sin en rouge avec une ligne plus épaisse. Nous allons également modifier la taille de la figure pour la rendre un peu plus horizontale.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-")

show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_3.png)

La fonction ``plot()`` dispose d'un argument color qui permet de changer la couleur de la courbe. Changer par exemple la ligne ``plot(x,cosx)`` par ``plot(x, cosx, color="red")``.

L'argument ``linewidth`` permet de changer l'épaisseur du trait exprimé en pixels.

L'argument ``linestyle`` permet de changer le style d'affichage de la ligne de courbe.
Vous pouvez essayer les différents paramètres: '-', '--', '-.', ':' ou 'steps'.

##Fixer les limites de la figure

Les axes du repère sont les droites qui portent les marques de graduation et qui délimitent la zone de représentation du graphique. Ces axes peuvent être placés arbitrairement.

Il est possible de changer les axes du repères en utilisant les fonctions ``xlim()``, ``ylim()``.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-")

xmin ,xmax = x.min(), x.max()
ymin, ymax = cosx.min(), cosx.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

show()
```

Voir documentation sur les fonctions ``xlim()`` : http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlim et ``ylim()`` :
http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylim

## Définir des graduations

Les graduations de notre figure ne sont pas idéales car elles ne montre pas des valeurs intéressantes comme (+/-π,+/-π/2) pour sinus et cosinus. Nous les changeons pour montrer ces valeurs.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-")

xmin ,xmax = x.min(), x.max()
ymin, ymax = cosx.min(), cosx.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
yticks([-1, 0, +1])

show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_5.png)

## Définir le texte des graduations

Les graduations actuelles ne sont pas idéales : elles n'affichent pas sur l'axe des abscisses les valeurs (+/-π, +/-π/2) et sur l'axe des ordonnées les valeurs (-1, 0, +1) qui nous intéressent pour cosinus.

Les graduations sont bien placées, mais le contenu de leur texte n'est pas très explicite. Nous pourrions deviner que 3.142 correspond à π, mais ce serait beaucoup mieux de l'indiquer clairement. Lorsqu'on définit des valeurs pour les graduations, il est aussi possible de définir des étiquettes de texte correspondant à ces valeurs dans une liste fournie en second argument d'appel de fonction. Nous utiliserons pour les formules, la notation mathématique [LaTeX](https://fr.wikipedia.org/wiki/LaTeX) pour obtenir un meilleur rendu final.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-")

xmin ,xmax = x.min(), x.max()
ymin, ymax = cosx.min(), cosx.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_6.png)

## Modifier la position des bords

Les bords peuvent être placés arbitrairement et jusqu'à présent il se trouve en bas et en haut, à droite et à gauche de la figure. Nous allons changer leurs positions pour les placer au milieu. Il y en 4 (top/bottom/left/right). Nous allons effacer celui du haut (top) et de droite (right) en leur donnant une couleur vide (none). On déplace ensuite celui du bas et de gauche au coordonnées 0 en x et en y.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-")

xmin ,xmax = x.min(), x.max()
ymin, ymax = cosx.min(), cosx.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_7.png)

## Ajouter une légende

Ajoutons une légende dans le coin haut gauche. Il faut ajouter un paramètre nommé ``label`` qui sera utilisé dans la boîte de légende.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-", label="cosinus")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-", label="sinus")

xmin ,xmax = x.min(), x.max()
ymin, ymax = cosx.min(), cosx.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

legend(loc='upper left')

show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_8.png)

**Question: Que fait la fonction ``legend()``?**

## Ajouter des points particuliers

Ajoutons quelques points intéressants en utilisant la fonction ``annotate()``.
Nous choisissons la valeur 2π/3 et nous voulons annoter à la fois la courbe sinus et cosinus. Nous dessinons un marqueur sur la courbe ainsi qu'une ligne en trait pointillé. Puis nous utilisons la fonction ``annotate()``pour afficher du texte avec une flêche.

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-", label="cosinus")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-", label="sinus")

xmin ,xmax = x.min(), x.max()
ymin, ymax = cosx.min(), cosx.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

legend(loc='upper left')

t = 2*np.pi/3
plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='blue')
annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')
annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$', xy=(t, np.cos(t)), xycoords='data', xytext=(-90, -50), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

show()
```
![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_9.png)

## Sauvegarder une figure Matplotlib

On peut générer un fichier image (que l'on pourra réutiliser ensuite sur le web ou dans un rapport) à partir d'une figure Matplotlib (par exemple ici en résolution de 72 points par pouce (1 pouce : 2.54 cm).)

```python
savefig("nom_image.png", dpi=72)
```

## Utiliser Matplotlib pour afficher des mesures

Il est possible également d'utiliser Matplotlib pour afficher des mesures à l'écran. Le plus facile est d'utiliser des fichiers de mesures au format CSV (https://fr.wikipedia.org/wiki/Comma-separated_values).
Utilisons des données provenant du dépôt de code github : https://github.com/cmrivers/ebola de l'épidémiologiste [Caitlin Rivers](http://www.caitlinrivers.com/). Ce dépôt de données contient des données de mortalité sur l'épidémie Ebola en Afrique de l'Ouest.

Télécharger le fichier : https://github.com/cmrivers/ebola/blob/master/country_timeseries.csv
(cliquer sur le bouton raw for avoir accès au fichier csv) et le nommer ``ebola.csv``.

Affichons le nombre de cas cumulés d'Ebola en [Guinée-Conakry](https://fr.wikipedia.org/wiki/Guin%C3%A9e) :
```python
x, y = np.loadtxt('ebola.csv', delimiter=',', converters = {2: lambda s: float(s.strip() or 0)}, skiprows = 1, usecols=(1, 2), unpack=True)
plot(x,y)
show()
```

On remarquera qu'il y comme il y a des données manquantes qui sont remplacées par la valeur 0 (paramètre ``converters``).

**Question: comment pallier au problème des valeurs manquantes ?**

**Question: Utiliser les fonctionnalités de Matplotlib pour présenter de la meilleure manière possible les données Ebola: couleur différentes en fonction du pays, légende des courbes avec le nom du pays.**

Voir la documentation pour ``np.loadtxt()`` ici: http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
## Utiliser Matplotlib pour afficher le contenu d'une grille à deux dimensions
Matplotlib peut afficher des images. Pour cela, il faut utiliser la commande:

```python
plt.imshow(m, cmap= ... , interpolation= ... )
```

 * Le premier paramètre est une matrice (array de numpy). Chaque élément de cette matrice est l’information sur un pixel, par exemple il peut s’agir d’une liste de triplets encodant les composantes R (rouge), G (verte), B (bleue) de chaque pixel.
 * Le deuxième paramètre est la “carte de couleur” de l’image, elle associe couleurs aux valeurs.
 * Le troisième paramètre est la manière dont les valeurs sont interpolées.

Pour les détails, voir: http://matplotlib.org/users/image_tutorial.html

## Faire des animations avec Matplotlib
Il est possible d'utiliser Matplotlib pour animer des images en utilisant le module animation.

```python
from matplotlib import animation
```

Il faut dans un premier temps créer la figure à animée. Pour cela deux fonctions peuvent être utilisées :

1. ``init()`` qui définit l'image de base, qui restera présente par défaut en arrière-plan,
2. ``animate()`` qui définit l'évolution de l'image et qui sera appellé périodiquement.

Il suffit alors d’appeler la fonction d’animation du module:

```python
ani = animation.FuncAnimation(fig, animate, init, blit=True, interval = 20)
```
Le paramètre ``init ``n’est utile que lorsque ``blit=True``, ``fig`` est la figure créée, ``interval`` est le délai entre deux affichages.

Ci-dessous, on trouvera une version revisée du Jeu de la Vie où l'on fait une animation:
```python
import numpy as np

cells = np.random.randint(0, 2, (256,512))

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

import matplotlib.animation as animation

def update(*args):
   iterate(cells)
   im.set_array(cells)
   return im,

ani = animation.FuncAnimation(fig, update, frames=range(20), interval=50)
plt.show()
```  
