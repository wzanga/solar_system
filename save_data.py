#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:03:45 2018

@author: zangawilliams
"""

# -*- coding: utf-8 -*-
import numpy as np

# Function to read in data from a file in the format [x,y,z,vx,vy,vz]
def ReadFile(filename):
    f = open(filename)
    f.readline()
    data = [[float(x) for x in line.split()] for line in f]
    f.close()
    return np.array(data)

#------------------------------------------------------------------------------
# Function to write an array to a results file
def AppendArray(filename, anArray):
    f = open(filename, 'a')
    for row in range(anArray.shape[0]):
        for col in range(anArray.shape[1]):
            f.write( '%6.3f ' % (anArray[row,col]))
        f.write('\n')
    #f.write('\n\n')
    f.close()
#------------------------------------------------------------------------------
#Function to write a list to a results file
def AppendList(filename, aList):
    f = open(filename, 'a')
    for row in range(aList.shape[0]):
        f.write( '%6.3f ' % (aList[row]))
    #f.write('\n\n')
    f.close()
#------------------------------------------------------------------------------

#Function to write a string to a results file
def AppendString(filename, aString):
    f = open(filename, 'a')
    f.write('%s\n' % (aString))
    f.close()
#------------------------------------------------------------------------------
