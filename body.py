#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:37:43 2018

@author: zangawilliams
"""
import numpy as np

class body :
    def __init__(self,name):
        [self.px, self.py, self.pz ] = [0,0,0] #km
        [self.vx, self.vy, self.vz ] = [0,0,0] #km/s
        self.name = name
        days = 86400;

        if name =='SUN' :
            #Physical parameters
            self.Req = 696342;                #[km]
            self.Rm =  696342;                #[km]
            self.M  = 1988544e24;             #[kg]
            self.GM = 1.3271244004193938e11;  #[km^3.s^-2]

            #Orbital parameters
            self.a = 0;    #[km]
            self.T = 0;    #[s]
            self.V = 0; #[km.s^-1]

        elif name =='MERCURY':
            #Physical parameters
            self.Req = 2439.7;        #[km]
            self.Rm = 2439.7;         #[km]
            self.M = 0.330104e24;     #[kg]
            self.GM = 22032;          #[km^3.s^-2]

            #Orbital parameters
            self.a = 57.91e6;         #[km]
            self.T = 87.9691*days;    #[s]
            self.V = 2*np.pi*self.a/self.T #[km.s^-1]

        elif name =='VENUS':
            #Physical parameters
            self.Req = 6051.8;       #[km]
            self.Rm = 6501.8;        #[km]
            self.M = 4.86732e24;     #[kg]
            self.GM = 324858.63;     #[km^3.s^-2]

            #Orbital parameters
            self.a = 108.21e6;        #[km]
            self.T = 224.701*days;    #[s]
            self.V = 2*np.pi*self.a/self.T #[km.s^-1]

        elif name=='EARTH' :
            #Physical parameters
            self.Req = 6378.14;         #[km]
            self.Rm  = 6371.00;         #[km]
            self.M   = 5.97219e24;      #[kg]
            self.GM  = 398600.440;      #[km^3.s^-2]

            #Orbital parameters
            self.a = 149.60e6;          #[km]
            self.T = 365.25636*days;     #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='MOON' :
            #Physical parameters
            self.Req = 1737.5;                     #[km]
            self.Rm  = 1737.5;                     #[km]
            self.M   = 0.07345814120628661e24;     #[kg] TO BE CONSISTENT WITH HARD CODED VALUE OF mu(Earth-Moon)=0.012150581623434
            self.GM  = 4902.801;                   #[km^3.s^-2]

            #Orbital parameters
            self.a = 384400;           #[km]
            self.T = 27.321582*days;    #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='MARS':
            #Physical parameters
            self.Req = 3396.19;       #[km]
            self.Rm = 3389.50;        #[km]
            self.M = 0.641693e24;     #[kg]
            self.GM = 42828.3;        #[km^3.s^-2]

            #Orbital parameters
            self.a = 227.92e6;       #[kg]
            self.T = 686.98*days;     #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='JUPITER':
            #Physical parameters
            self.Req =  71492;      #[km]
            self.Rm = 69911;        #[km]
            self.M = 1898.13e24;     #[kg]
            self.GM = 126686511;       #[km^3.s^-2]

            #Orbital parameters
            self.a = 778.57e6;       #[km]
            self.T = 4332.589*days;     #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='SATURN':
            #Physical parameters
            self.Req =  60268;    #[km]
            self.Rm = 58232;       #[km]
            self.M = 568.319e24;     #[kg]
            self.GM = 37931207.8;      #[km^3.s^-2]

            #Orbital parameters
            self.a = 1433.53e6;       #[kg]
            self.T = 10759.22*days;     #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='URANUS':
            #Physical parameters
            self.Req = 25559;      #[km]
            self.Rm = 25362;        #[km]
            self.M =  86.8103e24;    #[kg]
            self.GM =  5793966;      #[km^3.s^-2]

            #Orbital parameters
            self.a =  2872.46e6;      #[km]
            self.T =  30685.4*days;   #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='NEPTUNE':
            #Physical parameters
            self.Req = 24764;      #[km]
            self.Rm = 24622;        #[km]
            self.M = 102.410e24;     #[kg]
            self.GM =  6835107;      #[km^3.s^-2]

            #Orbital parameters
            self.a =  4495.06e6;      #[km]
            self.T =  60189*days;    #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='PLUTO':
            #Physical parameters
            self.Req =  1195;     #[km]
            self.Rm =  1195;       #[km]
            self.M = .01309e24;     #[kg]
            self.GM =  872.4;      #[km^3.s^-2]

            #Orbital parameters
            self.a =  5906.38e6;      #[km]
            self.T =  90465*days;    #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]

        elif name=='EARTH_AND_MOON':
            #Equivalent mass of the Earth+Moon system based at the center of mass
            #additionnal physical properties are those of the Earth for consistency)

            #Physical parameters
            self.Req = 6378.14;        #[km]
            self.Rm = 6371.00;         #[km]
            self.M = 5.97219e24+0.07342e24;       #[km]
            self.GM = 398600.440+4902.801;      #[km^3.s^-2]

            #Orbital parameters
            self.a = 149.60e6;          #[km]
            self.T = 365.25636*days;     #[s]
            self.V = 2*np.pi*self.a/self.T; #[km.s^-1]
        else:
            print("CHOOSE A PRE-EXISTING BODY")
        return


    def initialize(self,position,velocity):
        [self.px, self.py, self.pz ] = position  #km
        [self.vx, self.vy, self.vz ] = velocity #km/s
        return

    def get_position(self):
        return np.array([self.px, self.py, self.pz],float)

    def get_velocity(self):
        return np.array([self.vx, self.vy, self.vz],float)
