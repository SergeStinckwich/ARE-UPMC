#Librarie MatPlotLib

Matplotlib est une bibliothèque du langage de programmation python qui, combinée avec les bibliothèques python de calcul scientifique numpy et scipy, constitue un puissant outil pour tracer et visualiser des données.
  
## Tracer une fonction

```
from pylab import *

x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(X)

plot(x,cosx)

show()
````

`x` est un tableau de 256 valeurs variant de $$$-\pi$$$ à $$$\pi$$$.
`cosx` est un tableau de 256 valeurs contenant le résultat de l'application de la fonction cosx() sur chacune des valeurs du tableau `x`.

### Modifier les réglages par défaut
Matplotlib est fournie avec un jeu de paramètres par défaut qui permet de personnaliser toute sorte de propriétés. Vous pouvez contrôler les réglages par défaut de (presque) toutes les propriétés : taille du graphique, résolution en points par pouce (dpi), épaisseur du trait, couleurs, styles, vues, repères, grilles, textes, polices de caractères, etc. Bien que les réglages par défaut répondent à la plupart des cas courants, vous pourriez être amenés à en modifier quelques-uns pour des cas plus spécifiques.

###Caractéristiques du trait
###Axes

