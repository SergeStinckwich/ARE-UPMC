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
    positions[i,:]=object_position_1erJanv2014[list_objects[i]]
    velocities[i,:]=object_velocities_1erJanv2014[list_objects[i]]
    periods[i]=object_period[list_objects[i]]

vector=center_of_mass(positions,masses)
for i in range(num_particles):
    positions[i,:]=positions[i,:]-vector

vector=center_of_mass(velocities,masses)
for i in range(num_particles):
    velocities[i,:]=velocities[i,:]-vector

positions=positions*AU
velocities=velocities*AU/day

time,traj_pos,traj_vel,traj_pe,traj_ke,traj_te=trajectory(positions,
                                                              velocities,
                                                              masses,
                                                              1*day,
                                                              3*year)

nplots=6

fig=plt.figure()
ax=p3.Axes3D(fig)
planets=ax.plot([traj_pos[0,0,0]/AU],
                   [traj_pos[0,0,1]/AU],
                   [traj_pos[0,0,2]/AU],'go')
for i in range(1,nplots): 
    planets=planets+ax.plot([traj_pos[0,i,0]/AU],
                                [traj_pos[0,i,1]/AU],
                                [traj_pos[0,i,2]/AU],'ro')
    iplot=min(int(periods[i]/day),len(time))
    planets=planets+ax.plot(traj_pos[0:iplot,i,0]/AU,
                             traj_pos[0:iplot,i,1]/AU,
                             traj_pos[0:iplot,i,2]/AU,'r-')

ax.axis('equal')
ax.set_zlim(ax.get_xlim())
fig.canvas.draw()
 
fig_e=plt.figure()
ax_e=plt.subplot(111)
e_curves=plt.plot(time/year,traj_ke/1e33,'r-')
e_curves=e_curves+plt.plot(time/year,-traj_te/1e33,'g-') 

"""
def long_lat_orbit(orbit,orbit_ref):
    num_steps=orbit.shape[0]
    theta=np.zeros(num_steps)
    phi=np.zeros(num_steps)
    for s in range(num_steps):
        theta[s],phi[s]=longitude_latitude(orbit[s,:],orbit_ref[s,:])
    return theta,phi
"""

fig_view=plt.figure()
ax_view=plt.subplot()
ax_view.set_xlim(-180,180)
ax_view.set_ylim(-90,90)
ax_view.invert_xaxis()
theta,phi=longitude_latitude(traj_pos[0,0,:],traj_pos[0,3,:])
view_art=plt.plot(theta,phi,'go')
for p in range(1,num_particles):
    if not p==3:
        color='r'        
        if list_objects[p]=='Moon':
            color='b'
        theta,phi=longitude_latitude(traj_pos[0,p,:],traj_pos[0,3,:])
        view_art=view_art+plt.plot(theta,phi,color+'o')

Running=False
def animate(arg):
    if not Running:
        return planets
        
    global traj_pos
    global traj_vel
    global traj_te
    global traj_ke
    positions=traj_pos[-1,:,:]
    velocities=traj_vel[-1,:,:]
    for s in range(1):
        positions,velocities,pe,ke,te=propagate(positions,velocities,
                                                        masses,1*day)
        traj_pos=np.roll(traj_pos,-1,0)
        traj_pos[-1,:,:]=positions
        traj_vel=np.roll(traj_vel,-1,0)
        traj_vel[-1,:,:]=velocities
        traj_ke=np.roll(traj_ke,-1)
        traj_ke[-1]=ke
        traj_te=np.roll(traj_te,-1)
        traj_te[-1]=te
        
    e_curves[0].set_ydata(traj_ke/1e33)    
    e_curves[1].set_ydata(-traj_te/1e33) 
    ymin,ymax=ax_e.get_ylim()
    if ke/1e33<ymin:
        ax_e.set_ylim(ke/1e33,ymax)
    if ke/1e33>ymax:
        ax_e.set_ylim(ymin,ke/1e33)
    fig_e.canvas.draw()
    
    theta,phi=longitude_latitude(traj_pos[0,0,:],traj_pos[0,3,:])
#    ax_view.plot(theta,phi,'go')
    view_art[0].set_xdata(theta)
    view_art[0].set_ydata(phi)
    i=1
    for p in range(1,num_particles):
        if not p==3:
            color='r'        
            if list_objects[p]=='Moon':
                color='b'
            theta,phi=longitude_latitude(traj_pos[0,p,:],traj_pos[0,3,:])
#            ax_view.plot(theta,phi,color+'o')
            view_art[i].set_xdata(theta)
            view_art[i].set_ydata(phi)  
            i=i+1
    fig_view.canvas.draw()
    
    
    planets[0].set_xdata(traj_pos[-1,0,0]/AU)
    planets[0].set_ydata(traj_pos[-1,0,1]/AU)
    planets[0].set_3d_properties(traj_pos[-1,0,2]/AU)
    for p in range(1,nplots):
        planets[2*p-1].set_xdata(traj_pos[0,p,0]/AU)
        planets[2*p-1].set_ydata(traj_pos[0,p,1]/AU)
        planets[2*p-1].set_3d_properties(traj_pos[0,p,2]/AU)
        iplot=min(int(periods[p]/day),len(time))
        planets[2*p].set_xdata(traj_pos[0:iplot,p,0]/AU)
        planets[2*p].set_ydata(traj_pos[0:iplot,p,1]/AU)
        planets[2*p].set_3d_properties(traj_pos[0:iplot,p,2]/AU)
    return planets
  
ani=animation.FuncAnimation(fig,animate,interval=25)

def onkey(event):
    global Running
    if (event.key==" "):
        Running = not Running
                                
cid = fig.canvas.mpl_connect('key_press_event',onkey)
cid_view = fig_view.canvas.mpl_connect('key_press_event',onkey)

plt.show()

