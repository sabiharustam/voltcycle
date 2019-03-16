## FileName : baseline.py
## Calculate peak current from cyclic voltametry data
## Detect and remove value of capacitive current (background) from cyclic voltametry data 
#Still need some edits.

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook

#split forward and backward sweping data, to make it easier for processing.
def split(vector):
    """
    This function takes an array and splits it into two half.
    """
    split = int(len(vector)/2)
    end = int(len(vector))
    vector1 = np.array(vector)[0:split]
    vector2 = np.array(vector)[split:end]
    return vector1, vector2

def critical_idx(x, y): ## Finds index where data set is no longer linear 
    """
    This function takes x and y values callculate the derrivative of x and y, and calculate moving average of 5 and 15 points.
    Finds intercepts of different moving average curves and return the indexs of the first intercepts.
    """
    k = np.diff(y)/(np.diff(x)) #calculated slops of x and y

    ## Calculate moving average for 5 and 15 points.
    ## This two arbitrary number can be tuned to get better fitting.
    ave5 = []
    ave15 = []
    for i in range(len(k)-5):  # The reason to minus 5 is to prevent j from running out of index.
        a = 0 
        for j in range(0,5):
            a = a + k[i+j]
        ave5.append(round(a/5, 4)) # keeping 9 desimal points for more accuracy
    ave5 = np.asarray(ave5)
    for i in range(len(k)-15): 
        b = 0 
        for j in range(0,15):
            b = b + k[i+j]
        ave15.append(round(b/15, 5))
    ave15 = np.asarray(ave15)
    ## Find intercepts of different moving average curves
    idx = np.argwhere(np.diff(np.sign(ave15 - ave5[:len(ave15)])!= 0)).reshape(-1) #reshape into one row.
    return int(idx[0])

def mean(vector):
    """
    This function returns the mean values.
    """
    a = 0
    for i in vector:
        a = a + i
    return a/len(vector)
      
def linear_coeff(x, y):
    """
    This function returns the inclination coeffecient and y axis interception coeffecient m and b. 
    """
    m = (y-mean(y)) / (x - mean(x))    
    b = mean(y) - m * mean(x)
    return m, b

def y_fitted_line(m, b, x):
    y_base = []
    for i in x:
        y = m * i + b
        y_base.append(y)
    return y_base    

def linear_background(x, y):
    idx = critical_idx(x, y) + 3 #this is also arbitrary number we can play with.
    x_fit = np.array(x[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))])
    y_fit = np.array(y[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))])
    m, b = linear_coeff(x_fit,y_fit)
    y_base = y_fitted_line(m, b, x)
    return y_base

def main():
    ## Read from Chowdhury's function to get x and y
  ##### Really need to work on how to catch data from different way. We have to capture different cycles.
    try:
        x = pd.to_numeric(data[x_label]) 
        y = pd.to_numeric(data[y_label])
        ## Split vectors
        x1, x2 = split(x)
        y1, y2 = split(y)
        ## Finds linear background 	
        y_base1 = linear_background(x1,y1)
        y_base2 = linear_background(x2,y2)
        #cathodic peak current and potential
        max_pos = y2.argmax()
        max_pot = x2[max_pos]
        max_cur = y2[max_pos] - y_base2[max_pos]
        #Anodic peak current and potential
        min_pos = y1.argmin()
        min_pot = x1[min_pos]
        min_cur = y1[min_pos] - y_base1[min_pos]
        f"For this CV data, the 'Ipc' is {max_cur}, Vpc is {max_pot}, Ipa is {min_cur}, Vpa is {min_pot}"
    except:
        print('Data set could not be processed')
    
    ## Plot all data 
    plt.plot(x1, y1, 'dodgerblue',linewidth=1) ##darkgrey
    plt.plot(x2, y2, 'dodgerblue', linewidth=1) ##dodgerblue  
    plt.plot(x1, y_base1, color = "orangered", linestyle=':',linewidth=2) 
    plt.plot(x2, y_base2, color = "orangered", linestyle=':',linewidth=2) 



