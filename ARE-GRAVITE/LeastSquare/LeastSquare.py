# -*- coding: utf-8 -*-
"""
Projet LeastSquare

Created on Tue Feb 25 10:44:17 2014

@author: vuilleum
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

def sinusoide(param,x):
    V0,T,phi,Vm=param
    return Vm+V0*np.sin(2*np.pi/T*x+phi)

num_parameters=4

def sinusoide_with_noise(parameters,days,sigma):
    velocities=sinusoide(parameters,days)+np.random.normal(0.0,sigma,len(days))
    return velocities

def get_errors(parameters,days,velocities):
    y=velocities-sinusoide(parameters,days)
    return y

def residual(parameters,days,velocities):
    y=get_errors(parameters,days,velocities)
    r=sum(y**2)
    return r
    
def rms_error(parameters,days,velocities):
    res=residual(parameters,days,velocities)
    sample_size=len(days)
    sigma=np.sqrt(res/(sample_size-num_parameters))
    return sigma

def correlation(signal,prediction):
    sample_size=len(signal)
    mean=sum(signal)/sample_size
    S_res=sum((signal-prediction)**2)
    S_tot=sum((signal-mean)**2)
    return 1.0-S_res/S_tot

def least_square_fit(init,days,velocities):
    parameters,jacobian=opt.leastsq(get_errors,init,args=(days,velocities))
    return parameters

def bootstrap_parametric(opt_param,days,sigma,num_samples):
    parameters=np.zeros((num_samples,num_parameters))
    for sample in range(num_samples):
        velocities=sinusoide_with_noise(opt_param,days,sigma)
        parameters[sample,:]=least_square_fit(opt_param,days,velocities)
    return parameters

def bootstrap_nonparametric(opt_param,days,errors,num_samples):
    parameters=np.zeros((num_samples,num_parameters))
    sample_size=len(days)
    for sample in range(num_samples):
        indexes=np.random.randint(sample_size,size=sample_size)
        velocities=sinusoide(opt_param,days)+errors[indexes]
        parameters[sample,:]=least_square_fit(opt_param,days,velocities)
    return parameters

def confidence_interval(values,alpha):
    values=np.sort(values)
    num_values=len(values)
    mean=sum(values)/num_values
    inf=values[int(alpha*num_values)]
    sup=values[int((1-alpha)*num_values)]
    return inf,mean,sup    

def plot_scatter(x,y,xlabel,ylabel,title):
    fig=plt.figure()
    plt.title(title,figure=fig)
    plt.xlabel(xlabel,figure=fig)
    plt.ylabel(ylabel,figure=fig)
    plt.plot(x,y,'ro',figure=fig)

def plot_signal(days,velocities):
    fig_signal=plot_scatter(days,velocities,'Days',
                            'Velocities','Radial Velocity')
    return fig_signal

def plot_residual(days,errors):
    fig_residual=plot_scatter(days,errors,'Days','Errors','Residuals')
    return fig_residual

def plot_correlation(signal,prediction):
    r_square=correlation(signal,prediction)
    title="Correlation, R^2="+str(r_square)
    fig_corr=plot_scatter(prediction,signal,'Prediction','Signal',title)
    plt.plot(prediction,prediction,'b-')
    return fig_corr

if __name__ == '__main__' :
    
    sample_size=100    
    
    days=np.linspace(0,2*np.pi,sample_size)
    velocities=sinusoide([1,1,0,0],days)+np.random.normal(0.0,0.1,len(days))
    
    
    V0,T,phi,Vm=least_square_fit([1,1,0,0],days,velocities)
    
    print("V0=",V0,", T=",T,", phi=",phi,", Vm=",Vm)
    
    res=residual([V0,T,phi,Vm],days,velocities)
    sigma=rms_error([V0,T,phi,Vm],days,velocities)
    errors=get_errors([V0,T,phi,Vm],days,velocities)

    print("res=",res,", sigma=",sigma) 
    
    
    fig_signal=plot_signal(days,velocities)
    x=np.linspace(0,2*np.pi,200)
    y=sinusoide([V0,T,phi,Vm],x)
    plt.plot(x,y,'b-',figure=fig_signal)

    fig_res=plot_residual(days,errors)

        
    boot_param=bootstrap_parametric([V0,T,phi,Vm],days,sigma,1000)
    
    boot_nonparam=bootstrap_nonparametric([V0,T,phi,Vm],days,errors,1000)
    
    fig_bp=plot_scatter(boot_param[:,0],boot_param[:,1],
                        'V0','T','Bootstrap Parametric')
    plt.plot(V0,T,'bo',figure=fig_bp)

    fig_bnp=plot_scatter(boot_nonparam[:,0],boot_nonparam[:,1],
                        'V0','T','Bootstrap Non Parametric')
    plt.plot(V0,T,'bo',figure=fig_bnp)

    print()
    print('Bootstrap parametric')
    print('V0 :',confidence_interval(boot_param[:,0],0.1))
    print('T :',confidence_interval(boot_param[:,1],0.1))
    print('phi :',confidence_interval(boot_param[:,2],0.1))
    print('Vm :',confidence_interval(boot_param[:,3],0.1))
    
    print()
    print('Bootstrap non-parametric')
    print('V0 :',confidence_interval(boot_nonparam[:,0],0.1))
    print('T :',confidence_interval(boot_nonparam[:,1],0.1))
    print('phi :',confidence_interval(boot_nonparam[:,2],0.1))
    print('Vm :',confidence_interval(boot_nonparam[:,3],0.1))
