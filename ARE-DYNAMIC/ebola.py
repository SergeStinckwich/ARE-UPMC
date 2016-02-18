from pylab import *

def plot_ebola(countryNumber, countryName):
    x, y = np.loadtxt('ebola.csv', delimiter=',', converters = {countryNumber: lambda s: float(s.strip() or 0)}, skiprows = 1, usecols=(1, countryNumber), unpack=True)
    for i in range(1, len(x)-1):
        if (y[i] == 0):
            y[i]=y[i-1]
    plot(x,y, label=countryName)

plot_ebola(2, "Guinée")
plot_ebola(3, "Libéria")
plot_ebola(4, "Sierra Leone")
legend(loc='upper left')
show()
