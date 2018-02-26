#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:29:36 2018

@author: zangawilliams
"""

import matplotlib.pyplot as plt

def disp1_xy(S,name):
    #Si=[Xi1,......,XiN]
    #Xij=[x,y,z,vx,vy,vz]
    plt.figure()
    plt.title(name+'orbit around the Sun')
    plt.axis('equal')
    plt.xlabel('x [km]')
    plt.ylabel('y [km]')
    
    plt.plot(S[:,0],S[:,1])
    plt.plot(0,0,'o')
    plt.show()
    return
    
def disp1_xz(S,name):
    #Si=[Xi1,......,XiN]
    #Xij=[x,y,z,vx,vy,vz]
    plt.figure()
    plt.title(name+'orbit around the Sun')
    plt.axis('equal')
    plt.xlabel('x [km]')
    plt.ylabel('z [km]')
    
    plt.plot(S[:,0],S[:,2])
    plt.plot(0,0,'o')
    plt.show()
    return

def disp1_yz(S,name):
    #Si=[Xi1,......,XiN]
    #Xij=[x,y,z,vx,vy,vz]
    plt.figure()
    plt.title(name+'orbit around the Sun')
    plt.axis('equal')
    plt.xlabel('x [km]')
    plt.ylabel('z [km]')
    
    plt.plot(S[:,1],S[:,2])
    plt.plot(0,0,'o')
    plt.show()
    return


def dispN_xy(M):
    #M is a list of the states of each body | M=[SB1,....SBN]
    #BSi=[Xi1,......,XiN] and Xij=[x,y,z,vx,vy,vz]
    plt.figure()
    plt.title('Orbits of all the bodies around the Sun')
    plt.axis('equal')
    plt.xlabel('x [km]')
    plt.ylabel('y [km]')

    for i in range(len(M)):
        plt.plot(M[i][:,0],M[i][:,1])
    plt.plot(0,0,'o')
    plt.show()
    return
