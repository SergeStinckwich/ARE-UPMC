#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright INRIA
# Contributors: Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
#
# DANA is a computing framework for the simulation of distributed,
# asynchronous, numerical and adaptive models.
#
# This software is governed by the CeCILL license under French law and abiding
# by the rules of distribution of free software. You can use, modify and/ or
# redistribute the software under the terms of the CeCILL license as circulated
# by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info/index.en.html.
#
# As a counterpart to the access to the source code and rights to copy, modify
# and redistribute granted by the license, users are provided only with a
# limited warranty and the software's author, the holder of the economic
# rights, and the successive licensors have only limited liability.
#
# In this respect, the user's attention is drawn to the risks associated with
# loading, using, modifying and/or developing or reproducing the software by
# the user in light of its specific status of free software, that may mean that
# it is complicated to manipulate, and that also therefore means that it is
# reserved for developers and experienced professionals having in-depth
# computer knowledge. Users are therefore encouraged to load and test the
# software's suitability as regards their requirements in conditions enabling
# the security of their systems and/or data to be ensured and, more generally,
# to use and operate it in the same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
# -----------------------------------------------------------------------------
import numpy as np

def iterate(cells):
    # Count neighbours
    n = np.zeros(cells.shape, int)
    n[1:-1,1:-1] += (cells[0:-2,0:-2] + cells[0:-2,1:-1] + cells[0:-2,2:] +
                     cells[1:-1,0:-2]                    + cells[1:-1,2:] +
                     cells[2:  ,0:-2] + cells[2:  ,1:-1] + cells[2:  ,2:])
    N_ = n.ravel()
    Z_ = cells.ravel()

    # Apply rules
    rule1 = np.argwhere( (Z_==1) & (N_ < 2) )
    rule2 = np.argwhere( (Z_==1) & (N_ > 3) )
    rule3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
    rule4 = np.argwhere( (Z_==0) & (N_==3) )

    # Set new values
    Z_[rule1] = 0
    Z_[rule2] = 0
    Z_[rule3] = Z_[rule3]
    Z_[rule4] = 1

    # Make sure borders stay null
    cells[0,:] = cells[-1,:] = cells[:,0] = cells[:,-1] = 0

cells = np.array([[0,0,0,0,0,0],
              [0,0,0,1,0,0],
              [0,1,0,1,0,0],
              [0,0,1,1,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0]])

print(cells)
print()
for i in range(4): iterate(cells)
print(cells)
