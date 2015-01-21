#Calcul scientifique en Python

## Tirage de nombre aléatoire
La bibliothèque ``random`` permet de générer des nombres aléatoires. Voir documentation ici: https://docs.python.org/3/library/random.html

Quelques unes des fonctions les plus utiles:

* random.seed() : permet d'initialiser le générateur de nombres aléatoires
* random.random() : retourne un nombre réél aléatoire dans l'intervalle [0, 1]
* random.randrange(a,b): retourne un nombre entier compris entre a et b (inclus).

Pourquoi les nombres générés par cette bibliothèque sont des nombres pseudo-aléatoires ?

## Exercice: Estimation de pi
Imaginons une cible représentée par un disque de rayon r (donc de surface π*r2). Cette cible est incluse dans un carré de côté 2r (donc de surface (2r)2). Pour estimer nous allons jeter au hasard des fléchettes dans ce carré. La probabilité qu’une fléchette tombe sur la cible est donc π. En jetant un grand nombre de fléchettes nous aurons donc une 4estimation de π! Ecrivez le script Python qui permet de réaliser cette estimation.
## Bibliothèque numpy
Voir http://www.numpy.org/