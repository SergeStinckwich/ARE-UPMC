# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:01:36 2017

@author: nicolas
"""

import numpy as np
import random
import copy

from matplotlib import pyplot as plt

# GLOBAL PARAMETERS FOR EXPERIMENTS
neighb = 4          # size of neighbourhood
threshold = 0.5     # threshold of satisfaction
size = 70           # size of the line
maxIterations = 5   # max number of iteration for convergence

###############################################################################
# PRINTING FUNCTIONS
###############################################################################

def str_state(state):
    '''
    return the state as a string
    '''
    result = ""
    for i in state:
        result += str(i)
    return result

def str_unhappy(state):
    '''
    returns the string marking unhappy individuals with a 'X'
    '''
    result = ""
    for i in range(size):
        if is_happy(i, state):
            result += " "
        else:
            result += "X"
    return result

###############################################################################
# INDIVIDUAL SATISFACTION
###############################################################################

def homogeneinity_level(c, state):
    '''
    for a given individual c and state
    returns the ratio of individuals of same type in neighbourhood
    '''
    my_color = state[c]
    count = 0
    nb_neighb = 0
    for i in range(1, neighb+1):
        if c+i < size:
            nb_neighb += 1
            if state[c+i] == my_color:
                count += 1
        if c-i >= 0:
            nb_neighb += 1
            if state[c-i] == my_color:
                count += 1
    return float(count / nb_neighb)

def is_happy(c, s, verbose = False):
    '''
    returns whether individual c is satisfied in a given state
    '''
    h = homogeneinity_level(c, s)
    if verbose:
        print(s)
    return h >= threshold

###############################################################################
# MOVING TO OTHER LOCATIONS
###############################################################################
# gives priority to the right move in case of ties
# I didn't find this specification in Schelling's paper

def move_to(c, p, s):
    '''
    moves individual c to position p, shifting other individuals
    and returns the resulting list
    '''
    new_s = copy.copy(s) # new list for result
    my_color = new_s[c]
    if p > c: # moving to the right
        for i in range(c, p):
            new_s[i] = s[i+1]
            new_s[i+1] = my_color
    else:   # moving to the left
        for i in range(p, c):
            new_s[i+1] = s[i]
            new_s[p] = my_color
    return new_s

def move_to_nearest_satisfying(c,s,verbose=False):
    '''
    will move individual c to nearest satisfying location
    simulate the move and check whether satisfying
    returns a tuple new state, and boolean satisfied
    note: very inefficient but simple solution
    '''

    move_limit = max(size-c, c)
    move_distance = 0
    new_s = []
    satisfied = False
    while move_distance < move_limit and not(satisfied):
        move_distance += 1
        new_s = copy.copy(s) # used to simulate the move
        if c+move_distance < size:
            new_s = move_to(c, c+move_distance, new_s)
            if is_happy(c+move_distance, new_s):
                satisfied = True
                if verbose:
                    print (c, "moved to:", c+move_distance)
        else: # trying to move left
            if c-move_distance >= 0:
                new_s = copy.copy(s)
                new_s = move_to(c, c-move_distance, new_s)
                satisfied = is_happy(c-move_distance, new_s)
                if verbose and satisfied:
                    print (c, " moved to:", c-move_distance)
    return new_s, satisfied

###############################################################################
# GLOBAL DYNAMICS
###############################################################################
# Note: departs a little bit from Schelling's specification here
# Interesting problem of non convergence here when no maxIterations condition
# the penultimate individual moves to the last position, and so on


def dynamics(s, verbose = False, stepwise = False):
    '''
    departs a little bit from Schelling's specification here
    '''
    one_has_moved = True
    iterations = 0
    while one_has_moved and iterations < maxIterations:
        one_has_moved = False
        for i in range(size):
            if not (is_happy(i, s)): # i wants to move
                s, moved = move_to_nearest_satisfying(i, s)
                one_has_moved = moved or one_has_moved
        if verbose:
            print ("Tour ", iterations)
            print(str_state(s))
            print(str_unhappy(s))
        if stepwise:
            input("Press Enter to continue...")
        iterations += 1
    return s

###############################################################################
# METRICS: A FAIRE
# count_unhappy(), average_homogeneity(), average_cluster_size()
###############################################################################


###############################################################################
#  SIMULATIONS: A FAIRE
###############################################################################


###############################################################################
# TESTING
###############################################################################


# Schelling original list

cells = [0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0]


# Printing the list and some metrics

print(str_state(cells))
print(str_unhappy(cells))
#print("number of 0/1 unsatisfied:", count_unhappy(cells))
#print("average level of satisfaction:", average_homogeneity(cells))
#print("average cluster size:", average_cluster_size(cells))

# Testing moving agent 1 in the initial Schelling list


new_cells,_ = move_to_nearest_satisfying(1, cells, True)
print(str_state(new_cells))


# Testing the dynamics
# verbose mode will show all the states
# stepwise mode will wait the user to press a key

final_state = dynamics(cells,True)
print(str_state(final_state))


# Testing simulations, for neighbourhood from 1 to 8

#sample_size = 100

#rslt = simulations([1, 2, 3, 4, 5, 6, 7, 8], 0.5, sample_size)
#draw_simulations(rslt, sample_size)
