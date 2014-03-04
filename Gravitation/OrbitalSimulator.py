# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:50:18 2014

@author: vuilleum
"""

import numpy as np
from Gravitation import *

def get_forces(positions,masses):
    num_particles=len(masses)
    forces=np.zeros((num_particles,3))
    potential_energy=0.0
    for i in range(num_particles):
        for j in range(i+1,num_particles):
            vector=positions[i,:]-positions[j,:]
            distance=np.sqrt(sum(vector**2))
            potential_energy-=G*masses[i]*masses[j]/distance
            force_on_j=G*masses[i]*masses[j]/distance**3*vector
            forces[i,:]-=force_on_j
            forces[j,:]+=force_on_j
    return forces,potential_energy
    
def get_kinetic_energy(velocities,masses):
    num_particles=len(masses)
    kin_energy=0.0
    for i in range(num_particles):
        kin_energy+=0.5*masses[i]*sum(velocities[i,:]**2)
    return kin_energy
    
def propagate(positions,velocities,masses,dt):
    num_particles=len(masses)
    new_positions=positions+velocities*dt
    new_velocities=np.zeros((num_particles,3))
    forces,pot_energy=get_forces(new_positions,masses)
    for i in range(num_particles):
        new_velocities[i,:]=velocities[i,:]+forces[i,:]/masses[i]*dt
    kin_energy=get_kinetic_energy((velocities+new_velocities)/2.0,masses)
    total_energy=pot_energy+kin_energy
    return new_positions,new_velocities,pot_energy,kin_energy,total_energy
    
def trajectory(positions,velocities,masses,dt,tmax):
    numsteps=int(tmax/dt)
    nprint=max(int(numsteps/10),1)
    
    num_particles=len(masses)
    traj_pos=np.zeros((numsteps,num_particles,3))
    traj_vel=np.zeros((numsteps,num_particles,3))
    traj_pe=np.zeros(numsteps)
    traj_ke=np.zeros(numsteps)
    traj_te=np.zeros(numsteps)
    time=np.zeros(numsteps)
    for step in range(numsteps):
        positions,velocities,pe,ke,te=propagate(positions,
                                                velocities,masses,dt)
        traj_pos[step,:,:]=positions
        traj_vel[step,:,:]=velocities
        traj_pe[step]=pe
        traj_ke[step]=ke
        traj_te[step]=te
        time[step]=step*dt
        
        if step%nprint==0:
            print(str(step/numsteps*100)+"%",time[step]/day,'days',
                    pe,ke,te)
        
    return time,traj_pos,traj_vel,traj_pe,traj_ke,traj_te

def velocity_from_position_period(position,period):
    velocity=np.zeros(3)
    velocity[1]=position[0]*2*np.pi/period
    velocity[0]=-position[1]*2*np.pi/period
    return velocity
    
def center_of_mass(positions,masses):
    vector=np.zeros(3)
    mass=0.0
    num_particles=len(masses)
    for i in range(num_particles):
        vector=vector+positions[i,:]*masses[i]
        mass=mass+masses[i]
    return vector/mass
    
def vitesse_radiale(position1,position2,vitesse1,vitesse2):
    vector=position1-position2
    distance=sqrt(sum(vector**2))
    vector=vector/distance
    vradiale=sum(vector*(vitesse1-vitesse2))
    return vradiale
    
