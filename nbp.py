#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:22:13 2018

@author: zangawilliams
"""
from body import body
import numpy as np
import integration_methods as IM
import save_data as SD

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
    
    def save_state(self,X,header=False):
        #save the sate with the titles
        for j in range(len(self.body)):
            if header:
                open("./data/"+self.body[j].name + ".txt", 'w').close()
                SD.AppendString("./data/"+self.body[j].name + ".txt","x[km] y[km] z[km] vx[km] vy[km] vz[km]")
            else : 
                SD.AppendArray("./data/"+self.body[j].name + ".txt",X[j].reshape(1,6))
        return
    
    def orbit_computation(self,method):
        #method 1 : euler_explicit
        #method 2 : stormer_verlet
        
        #add the header to the files
        self.save_state(self.get_state(),True)
        
        for i in range(self.n_iter):
            X = self.get_state()
            if method == 1 :
                X = IM.euler_explicit(X,self.t_step,self.state_deriv)
            elif method ==2 :
                X = IM.stormer_verlet(X,self.t_step,self.state_deriv)
            else:
                print('CHOOSE A CORRECT INTEGRATION METHOD')
                print('1 : Euler_explicit ')
                print('2 : Stormer_Verlet ')
                break
            self.set_state(X)
            
            #save the states in txt files
            self.save_state(X,False)
        
    def get_results(self,name):
        data = SD.ReadFile("./data/"+name+ ".txt")
        return data
    
    def get_results_all(self):
        M=[]
        for i in range(len(self.body)):
            M.append( self.get_results(self.body[i].name ) )
        return M
