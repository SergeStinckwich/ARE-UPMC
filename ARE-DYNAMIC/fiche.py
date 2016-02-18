from pylab import *
d,v=np.loadtxt("vitesses.txt",skiprows=2,usecols=(0,1),unpack=True)

## Model retourne un tableau vitesse a partir de distance
## et d'une valeur pour H0
def model(d, H0):
	return(d*H0)

## residus calcule la distance entre le modele et la vitesse
## determinee experimentalement
def residus(d, v, H0):
	return(v-model(d,H0))

## Calcul du Chi2
def chi2(d, v, H0):
	r = residus(d,v,H0)
	r2 = r*r
	somme = 0.0
	for i in range(0, len(r)):
		somme = somme + r2[i]
	return(somme)


#Determination du minimum de la fonction chi2
def minimise(d, v, min, max, precision):
    val = np.linspace(max, min, (max-min)/precision)
    result = np.zeros((max-min)/precision, dtype=float)
    minimum =chi2(d, v, val[0])
    valMin = val[0]
    for i in range(0, len(val)):
        result[i] = chi2(d, v, val[i])
        if (result[i]<minimum):
            minimum = result[i]
            valMin = val[i]
    return valMin


def R2(d, v, H0):
    SSignal = np.sum((v-np.mean(v))**2)
    SResidus = np.sum(residus(d, v, H0)**2)
    return 1.0-SResidus/SSignal

def chi2weighted(d, v, H):
    r = residus(d,v,H)
    r = r/d
    return sum(r**2)

#Determination du minimum de la fonction chi2
def minimise2(d, v, min, max, precision):
    val = np.linspace(max, min, (max-min)/precision)
    result = np.zeros((max-min)/precision, dtype=float)
    minimum =chi2weighted(d, v, val[0])
    valMin = val[0]
    for i in range(0, len(val)):
        result[i] = chi2weighted(d, v, val[i])
        if (result[i]<minimum):
            minimum = result[i]
            valMin = val[i]
    return valMin


# Valeur optimale de H0 a 10E-2
H0Opt =minimise2(d,v,60,80, 0.001)

# Figure 1 - Affichage graphique du chi2 entre 60 et 80
intervalle = np.linspace(60, 80, 100)
result = np.zeros(100, dtype=float)
for i in range(0, len(intervalle)):
    result[i] = chi2(d,v, intervalle[i])

## Affichage d'une fleche rouge
annotate('Chi2 min = '+str(chi2(d,v, H0Opt)),
        xy = (H0Opt, chi2(d,v, H0Opt)),
        xytext=(10, 30),
        textcoords='offset points',
        fontsize=16,
        arrowprops = dict(facecolor='red'))
title('Graphe du Chi2')
text(2, 10, 'Hello')
xlabel('distance (km/s)')
ylabel('Chi2 ')
plot(intervalle, result)
show()
