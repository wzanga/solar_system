#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:22:13 2018

@author: zangawilliams
"""
from body import body
import numpy as np
from integration_methods import euler_explicit, stormer_verlet

class nbp :
    def __init__(self,L):
        self.body=[]
        [self.t_inf, self.t_sup, self.t_step, self.n_iter ] = [0,0,0,0]
        for name in L :
            self.body.append( body(name) )
        return
    
    def set_param(self,t_inf,t_sup,t_step):
        self.t_inf = t_inf
        self.t_sup = t_sup
        self.t_step = t_step
        self.n_iter = int((t_sup - t_inf)/t_step)
        return
    
    def set_state(self,X):
        # X is an Nx6 array containing the initial condition of the bodies
        # in the same order as in self.body
        # X[i] = [px,py,pz,vx,vy,vz]
        if len(X)!=len(self.body):
            print("NOT ENOUGH INITIAL CONDITIONS")
        else:
            for i in range(len(X)):
                self.body[i].initialize(X[i,:3],X[i,3:6])
        return
            
    def get_state(self):
        #Create the current state vector of the system
        N = len(self.body)
        X = np.zeros( (N,6), float)
        for i in range(N) :
            b = self.body[i]
            X[i] = np.array([b.px,b.py,b.pz,b.vx,b.vy,b.vz],float)
        return X
    
    def state_deriv(self,X):
        #Derive the state vector X
        N = len(self.body)
        dX = np.zeros_like(X)
        dX[:,0:3] = X[:,3:6]
        for i in range(N):
            for j in range(N):
                if i==j: continue
                r = X[i,0:3] - X[j,0:3]
                nr = np.linalg.norm(r)
                
                #check for any collision
                if nr <= self.body[i].Req + self.body[j].Req :
                    print("collision between ",self.body[i].name," and ",self.body[j].name)
                    
                #compute the acceleration
                dX[i,3:6] = dX[i,3:6] - self.body[j].GM * r/(nr**3)            
        return dX 
    
    def orbit_computation(self,method,c1,c2,c3):
        #method 1 : euler_explicit
        #method 2 : stormer_verlet
        L0,L1,L2=[],[],[]
        for i in range(self.n_iter):
            x = self.get_state()
            if method == 1 :
                x = euler_explicit(x,self.t_step,self.state_deriv)
            elif method ==2 :
                x = stormer_verlet(x,self.t_step,self.state_deriv)
            else:
                print('CHOOSE A CORRECT INTEGRATION METHOD')
                print('1 : Euler_explicit ')
                print('2 : Stormer_Verlet ')
                break
            self.set_state(x) 
            L0.append(list(x[c1,0:3]))
            L1.append(list(x[c2,0:3]))
            L2.append(list(x[c3,0:3]))
        return [np.array(L0), np.array(L1), np.array(L2)]
