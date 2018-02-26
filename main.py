#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:14:45 2018

@author: zangawilliams
"""

from nbp import nbp
import matplotlib.pyplot as plt
import numpy as np

nbp = nbp(['SUN','MERCURY','VENUS','EARTH','MARS','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO'])

t_inf = 0
t_sup = 0.95*nbp.body[3].T
t_step = 3600*24

#Proto-stable-initial-conditions
x0=[]
for i in range(len(nbp.body)):
    x0.append([nbp.body[i].a,0,0,0,nbp.body[i].V,0])

nbp.set_param(t_inf,t_sup,t_step)
nbp.set_state(np.array(x0))
nbp.orbit_computation(2)
L0 = nbp.get_results('EARTH')
L1 = nbp.get_results('MARS')
L2 = nbp.get_results('SATURN')
#

plt.figure()
plt.clf()
plt.plot(L0[:,0],L0[:,1])
plt.plot(L1[:,0],L1[:,1])
plt.plot(L2[:,0],L2[:,1])
#
plt.plot(0,0,'o')
plt.title('Body orbit around the Sun')
plt.axis('equal')
plt.xlabel('x [km]')
plt.ylabel('y [km]')
plt.show()
