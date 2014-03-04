# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:47:21 2014

@author: vuilleum
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

from SolarSystem import *
from Gravitation import *
from OrbitalSimulator import *

list_objects=["Sun","Mercury","Venus","Earth","Moon","Mars","Jupiter","Saturn",
              "Uranus","Neptune"]

num_particles=len(list_objects)

positions=np.zeros((num_particles,3))
velocities=np.zeros((num_particles,3))
masses=np.zeros(num_particles)
periods=np.zeros(num_particles)

for i in range(num_particles):
    masses[i]=object_masses[list_objects[i]]

for i in range(num_particles):
    positions[i,:]=object_position_1erJanv2014[list_objects[i]]

vector=center_of_mass(positions,masses)
for i in range(num_particles):
    positions[i,:]=positions[i,:]-vector

for i in range(num_particles):
    velocities[i,:]=object_velocities_1erJanv2014[list_objects[i]]

vector=center_of_mass(velocities,masses)
for i in range(num_particles):
    velocities[i,:]=velocities[i,:]-vector

positions=positions*AU
velocities=velocities*AU/day

num_years=2
dt=1*day
time,orbits,orbits_vel,orbits_pe,orbits_ke,orbits_te=trajectory(
                   positions,velocities,masses,
                   dt,num_years*year)

for i in range(num_particles):
    periods[i]=object_period[list_objects[i]]

object_colors={
    "Sun": "y",
    "Venus": "c",
    "Mercury": "m",
    "Earth": "b",
    "Moon": "b",
    "Mars": "r",
    "Jupiter": "g",
    "Saturn": "r",
    "Uranus": "r",
    "Neptune": "k"
}

object_symbols={
    "Sun": "o",
    "Venus": "o",
    "Mercury": "o",
    "Earth": "o",
    "Moon": "d",
    "Mars": "o",
    "Jupiter": "o",
    "Saturn": "s",
    "Uranus": "d",
    "Neptune": "o"
}

nplots=6

fig=plt.figure(figsize=(14,7),tight_layout=True)

ax_orbits=fig.add_subplot(121,projection="3d")

for p in range(1,nplots): 
    iplot=min(int(periods[p]/dt)+1,len(time))
    color=object_colors[list_objects[p]]
    ax_orbits.plot(orbits[0:iplot,p,0]/AU,
            orbits[0:iplot,p,1]/AU,
            orbits[0:iplot,p,2]/AU,
            color+'-')

color=object_colors["Sun"]
symbol=object_symbols["Sun"]
obj_orbits=ax_orbits.plot([positions[0,0]/AU],
                          [positions[0,1]/AU],
                          [positions[0,2]/AU],
                          color+symbol)
for p in range(1,nplots): 
    color=object_colors[list_objects[p]]
    symbol=object_symbols[list_objects[p]]
    obj_orbits+=ax_orbits.plot([positions[p,0]/AU],
                               [positions[p,1]/AU],
                               [positions[p,2]/AU],
                               color+symbol)
                          
ax_orbits.axis('equal')
ax_orbits.set_zlim(ax_orbits.get_xlim())

ax_sky=fig.add_subplot(222)
ax_sky.set_xlim(-180,180)
ax_sky.set_ylim(-90,90)
ax_sky.invert_xaxis()

def ascension_declinaison(position,position_ref):
    vector=position-position_ref
    distance=np.sqrt(sum(vector**2))
    vector=vector/distance
    omega=earth_inclination_deg*np.pi/180
    x=vector[0]
    y=np.cos(omega)*vector[1]-np.sin(omega)*vector[2]
    z=np.sin(omega)*vector[1]+np.cos(omega)*vector[2]
    theta=np.arcsin(z)
    phi=np.arctan2(y,x)
    declinaison=theta*180/(np.pi)
    ascension=phi*180/(np.pi)
    return ascension,declinaison

phi=np.linspace(-np.pi,np.pi,200)
ecliptique_decl=np.zeros(200)
ecliptique_asc=np.zeros(200)
for i in range(200):
    vector1=np.array([np.cos(phi[i]),np.sin(phi[i]),0.0])
    vector2=np.zeros(3)
    ecliptique_asc[i],ecliptique_decl[i]=ascension_declinaison(vector1,vector2)

ax_sky.plot(ecliptique_asc,ecliptique_decl,'b--')

color=object_colors["Sun"]
symbol=object_symbols["Sun"]
asc,decl=ascension_declinaison(positions[0,:],positions[3,:])
obj_sky=ax_sky.plot(asc,decl,color+symbol)
for p in range(1,num_particles): 
    if not list_objects[p]=="Earth":
        color=object_colors[list_objects[p]]
        symbol=object_symbols[list_objects[p]]
        asc,decl=ascension_declinaison(positions[p,:],positions[3,:])
        obj_sky+=ax_sky.plot(asc,decl,color+symbol)

fig.canvas.draw()

def init():
    return
    
def step():
    global positions
    global velocities
    
    positions,velocities,pe,ke,te=propagate(positions,velocities,masses,dt)
    return
    
Running=False
def toggle_state():
    global Running
    Running=not Running
    
def update(*args):
    if not Running:
        return obj_orbits+obj_sky

    step()    

    for p in range(0,nplots):   
        obj_orbits[p].set_xdata(positions[p,0]/AU)
        obj_orbits[p].set_ydata(positions[p,1]/AU)
        obj_orbits[p].set_3d_properties(positions[p,2]/AU)

    asc,decl=ascension_declinaison(positions[0,:],positions[3,:])
    obj_sky[0].set_xdata(asc)
    obj_sky[0].set_ydata(decl)
    i=1
    for p in range(1,num_particles): 
        if not list_objects[p]=="Earth":
            asc,decl=ascension_declinaison(positions[p,:],positions[3,:])
            obj_sky[i].set_xdata(asc)
            obj_sky[i].set_ydata(decl)
            i+=1
    
    return obj_orbits+obj_sky

init()

ani=animation.FuncAnimation(fig,update,interval=25)

def onkey(event):
    if (event.key==" "):
        toggle_state()
                                
cid = fig.canvas.mpl_connect('key_press_event',onkey)
