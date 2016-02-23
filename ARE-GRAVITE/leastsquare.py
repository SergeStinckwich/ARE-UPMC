import numpy
import matplotlib.pyplot as plt

d = numpy.array([0.028,0.076,0.108,0.136,0.153,0.226,0.283,0.359,0.363,0.408,0.438,0.472,0.476,0.476,0.493,0.556,0.639])
v = numpy.array([2.7,4.2,10.5,14.1,10.5,13.2,19.8,28.2,20.7,29.4,31.8,44.4,32.1,37.2,33,34.5,46.5])

def model(H0, d):
    return(d*H0)

def residus(H0, d, v):
    return(v-model(H0,d))
 
from scipy.optimize import leastsq

x0 = numpy.zeros(1)
result = leastsq(residus, x0, args=(d, v))

print(result[0])
