# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:07:06 2014

@author: vuilleum
"""

solar_objects=[
    "Sun",
    "Mercury", 
    "Venus", 
    "Earth", 
    "Mars", 
    "Jupiter", 
    "Saturn", 
    "Uranus", 
    "Neptune",
    "Moon"
]

object_diameters={
    "Sun" : 1.391e9,
    "Mercury": 4.8794e6, 
    "Venus": 1.2104e7, 
    "Earth": 1.27349e7, 
    "Mars": 6.772e6, 
    "Jupiter": 1.3835e8, 
    "Saturn": 1.1463e8, 
    "Uranus": 5.0532e7, 
    "Neptune": 4.9105e7,
    "Moon": 3.4750e6
}

object_masses={
    "Sun" : 1.988435e30,
    "Mercury": 3.3022e23, 
    "Venus": 4.8690e24, 
    "Earth": 5.9721986e24, 
    "Mars": 6.4191e23, 
    "Jupiter": 1.8988e27, 
    "Saturn": 5.6850e26, 
    "Uranus": 8.6625e25, 
    "Neptune": 1.0278e26,
    "Moon": 7.3459e22
}

object_semimajor_axis={
    "Sun" : 0,
    "Mercury": 5.7909176e10, 
    "Venus": 1.0820893e11, 
    "Earth": 1.49597887e11, 
    "Mars": 2.27936637e11, 
    "Jupiter": 7.78412027e11, 
    "Saturn": 1.42672541e12, 
    "Uranus": 2.870972220e12, 
    "Neptune": 4.498252910e12,
    "Moon": 3.844e8
}

object_period={
    "Sun" : 0,
    "Mercury": 7.600544e6, 
    "Venus": 1.9414149e7, 
    "Earth": 3.1558149e7, 
    "Mars": 5.9355036e7, 
    "Jupiter": 3.7435566e8, 
    "Saturn": 9.2929236e8, 
    "Uranus": 2.6513700e9, 
    "Neptune": 5.2004186e9,
    "Moon": 2.3606e6
}

import numpy as np

"""
Jour Julien: 2456658.50000000000
Positions: AU
Vitesses: AU/j
"""

object_position_1erJanv2014={
    "Sun": np.array([0,0,0]),
    "Mercury": np.array([0.1197436323963,-0.4342540322410,-0.0464678909032]),
    "Venus": np.array([-0.0498977342279,0.7176031661874,0.0127127484708]),
    "Earth": np.array([-0.1756044565231,0.9675509401260,-0.0000319971739]),
    "Mars": np.array([-1.5124429025286,0.6968064744565,0.0517239802142]),
    "Jupiter": np.array([-1.3308046028723,5.0187246693602,0.0089353778633]),
    "Saturn": np.array([-6.8851880232283,-7.0754805034021,0.3971352847239]),
    "Uranus": np.array([19.6450107458292,3.9226085861038,-0.2398660541991]),
    "Neptune": np.array([27.0634723294521,-12.8918847633380,-0.3580999366748]),
    "Moon": np.array([-0.1754548042885,0.9651713564058,0.0001472329448])
}

object_velocities_1erJanv2014={
    "Sun": np.array([0,0,0]),
    "Mercury": np.array([0.0214817132408,0.0089129970425,-0.0012426836375]),
    "Venus": np.array([-0.0202464552364,-0.0015119133378,0.0011477498649]),
    "Earth": np.array([-0.0172155561068,-0.0031373928011,-0.0000002336261 ]),
    "Mars": np.array([-0.0053308596891,-0.0115145723428,-0.0001104084128]),
    "Jupiter": np.array([-0.0073919246201,-0.0015782667777,0.0001719645084]),
    "Saturn": np.array([0.0036892093642,-0.0039064444416,-0.0000790330655]),
    "Uranus": np.array([-0.0008044799796,0.0036714017994,0.0000241322220]),
    "Neptune": np.array([0.0013232364549,0.0028502274345,-0.0000892382644]),
    "Moon": np.array([-0.0165827545203,-0.0030837183612,0.0000282468573])
}
