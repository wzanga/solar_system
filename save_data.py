#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:03:45 2018

@author: zangawilliams
"""

# -*- coding: utf-8 -*-
from PIL import Image
import glob, os
import numpy


# Function to read in data from a file in the format defined by Duncan
def ReadFile(filename):
    f = open(filename);
    # the first line contains the number of variables. the function int converts a
    # string to an integer
    noVariables = int(f.readline())
    # the second line contains the number of root nodes
    noRoots = int(f.readline());
    # the third line contains the number of states of each variable
    # this command extracts a list of integers. The split method breaks the line into a list of substrings
    # The map function applies a function (int) to a list (the substrings) to produce a list of integers.
    noStates = map(int,((f.readline()).split()))
    # the fourth line contains a single integer the number of data points
    noDataPoints = int(f.readline())
    # all the subsequent lines of the file are data points. Each line is extracted as a list of integers which is 
    # appended to the list datain.
    datain = []
    for x in range(noDataPoints):
        datain.append(map(int,((f.readline()).split())))
    f.close()
    return [noVariables, noRoots, noStates, noDataPoints, datain]

#------------------------------------------------------------------------------
# Function to write an array to a results file
# the array is assumed to be either of proababilities of dependencies
def AppendArray(filename, anArray):
    f = open(filename, 'a')
    for row in range(anArray.shape[0]):
        for col in range(anArray.shape[1]):
            f.write( '%6.3f ' % (anArray[row,col]))
        f.write('\n')
    f.write('\n\n')
    f.close()
#------------------------------------------------------------------------------
#Function to write a list to a results file
def AppendList(filename, aList):
    f = open(filename, 'a')
    for row in range(aList.shape[0]):
        f.write( '%6.3f ' % (aList[row]))
    f.write('\n\n')
    f.close()
#------------------------------------------------------------------------------

#Function to write a string to a results file
def AppendString(filename, aString):
    f = open(filename, 'a')
    f.write('%s\n' % (aString))
    f.close()
#------------------------------------------------------------------------------
