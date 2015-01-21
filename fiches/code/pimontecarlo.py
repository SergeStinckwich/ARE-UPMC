import random
import matplotlib.pyplot as plt
import math

nbSimus = 1000000
reussi = 0

for essai in range(nbSimus):
    x = random.random()
    y = random.random()
    d = math.sqrt(x**2 + y**2)
    if d < 1 :
        reussi += 1
        if essai%1000000==0:
            plt.plot(x,y,'ro') # on marque les jets reussis par des cercles rouges
    else:
        if essai%1000000==0:
            plt.plot(x,y,'bo') # on marque les jets rates par des cercles bleus
    titre = "Estimation de $\pi$ =" + str(4*reussi/nbSimus)
    titre += " (" + str(nbSimus) + " simulations)"
    plt.title(titre)
    if essai%100000==0 :
        print(essai)
plt.show()
