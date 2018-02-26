#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:14:45 2018

@author: zangawilliams
"""

from nbp import nbp
import matplotlib.pyplot as plt
import numpy as np
import plot_results as PR

#nbp = nbp(['SUN','MERCURY','VENUS','EARTH','MARS','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO'])
#nbp = nbp(['SUN','MERCURY','VENUS','EARTH','MARS'])
nbp = nbp(['SUN','EARTH','MARS'])

t_inf = 0
t_sup = 1*nbp.body[1].T
t_step = 3600*24

#INITIAL CONDITIONS
x0=[]
for i in range(len(nbp.body)):
    x0.append([nbp.body[i].a,0,0,0,nbp.body[i].V,0])

#SIMULATION
nbp.set_param(t_inf,t_sup,t_step)
nbp.set_state(np.array(x0,float))
nbp.orbit_computation(2)

#DISP RESULTS
M=nbp.get_results_all()
PR.dispN_xy(M)