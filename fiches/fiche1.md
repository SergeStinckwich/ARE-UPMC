#Librairie MatPlotLib

Matplotlib est une bibliothèque du langage de programmation Python qui, combinée avec les bibliothèques python de calcul scientifique numpy et scipy, constitue un puissant outil pour tracer et visualiser des données.


## Utiliser Matplotlib pour tracer une fonction

```
from pylab import *

x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(X)

plot(x,cosx)

show()
````

La fonction linspace de la librairie numpy (np) permet de générer un tableau de 256 valeurs réélles variant de $$$-\pi$$$ à $$$\pi$$$.
`cosx` est un tableau de 256 valeurs contenant le résultat de l'application de la fonction cosx() sur chacune des valeurs du tableau `x`.

Matplotlib est fournie avec un jeu de paramètres par défaut qui permet de personnaliser toute sorte de propriétés. Vous pouvez contrôler les réglages par défaut de (presque) toutes les propriétés : taille du graphique, résolution en points par pouce (dpi), épaisseur du trait, couleurs, styles, vues, repères, grilles, textes, polices de caractères, etc. Bien que les réglages par défaut répondent à la plupart des cas courants, vous pourriez être amenés à en modifier quelques-uns pour des cas plus spécifiques.

###Caractéristiques du trait

Il est possible de modifier quelques caractéristiques du trait utiliser pour faire les courbes.
#### color
La fonction plot() dispose d'un argument color qui permet de changer la couleur de la courbe. Changer par exemple la ligne plot(x,cosx) par plot(x, cosx, color="blue").
#### linewidth
L'argument linewidth permet de changer l'épaisseur du trait exprimé en pixels.
#### linestyle
L'argument linestyle permet de changer le style d'affichage de la ligne de courbe.
Vous pouvez essayer les différents paramètres: '-', '--', '-.', ':' ou 'steps'.

###Axes
Les axes du repère sont les droites qui portent les marques de graduation et qui délimitent la zone de représentation du graphique. Ces axes peuvent être placés arbitrairement.

Il est possible de changer les axes du repères en utilisant les fonctions xlim(), ylim().

### Définir le texte des graduations

Les graduations actuelles ne sont pas idéales : elles n'affichent pas sur l'axe des abscisses les valeurs (+/-π, +/-π/2) et sur l'axe des ordonnées les valeurs (-1, 0, +1) qui nous intéressent pour cosinus. Modifions-les pour qu'elles correspondent à ces valeurs :

```
xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
yticks([-1, 0, +1])
```

Les graduations sont bien placées, mais le contenu de leur texte n'est pas très explicite. Nous pourrions deviner que 3.142 correspond à π, mais ce serait beaucoup mieux de l'indiquer clairement. Lorsqu'on définit des valeurs pour les graduations, il est aussi possible de définir des étiquettes de texte correspondant à ces valeurs dans une liste fournie en second argument d'appel de fonction. Nous utiliserons une notation LaTeX pour obtenir un meilleur rendu final.

```
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
```

### Ajouter une légende

### Sauvegarder une figure Matplotlib

On peut générer un fichier image (que l'on pourra réutiliser ensuite sur le web ou dans un rapport) à partir d'une figure Matplotlib (par exemple ici en résolution de 72 points par pouce[^1].)

[^1]: 1 pouce = 2.54 cm

```
savefig("nom_image.png", dpi=72)
```

## Utiliser Matplotlib pour afficher des mesures

## Utiliser Matplotlib pour dessiner une grille 2D

## Faire des animations avec Matplotlib
Il est possible d'utiliser Matplotlib pour animer des images en utilisant le module animation.

```
from matplotlib import animation
````

Il faut dans un premier temps créer la figure à animée. Pour cela deux fonctions peuvent être utilisées : 

1. init() qui définit l'image de base, qui restera présente par défaut en arrière-plan,
2. animate() qui définit l'évolution de l'image et qui sera appellé périodiquement.



