#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 18:19:00 2018

@author: zangawilliams
"""

def stormer_verlet(X,h,f):
    # q_{n+1} = q_{n} + v_{n}*h + a_{n}*(h^2)/2
    # v_{n+1} = v_{n} + (a_{n} + a_{n+1})*h/2
    #
    X_next = X.copy()
    #position
    dX = f(X)
    X_next[:,0:3] = X[:,0:3] + dX[:,0:3]*h + dX[:,3:6]*(h**2)/2.0
    #velocity
    dX_next = f(X_next)
    X_next[:,3:6] = X[:,3:6] + ( dX[:,3:6] + dX_next[:,3:6] )*h/2.0
    return X_next

def euler_explicit(X,h,f):
    # X := X + h*f(X)
    return X + h*f(X)

def RK4(X,h,f):
    #RUNGE KUTTA 4
    return
