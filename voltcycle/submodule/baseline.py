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
    ave10 = []
    ave15 = []
    for i in range(len(k)-10):  # The reason to minus 5 is to prevent j from running out of index.
        a = 0 
        for j in range(0,5):
            a = a + k[i+j]
        ave10.append(round(a/5, 5)) # keeping 9 desimal points for more accuracy
    
    for i in range(len(k)-15): 
        b = 0 
        for j in range(0,10):
            b = b + k[i+j]
        ave15.append(round(b/10, 5))
    ave10i = np.asarray(ave5)
    print(ave10i)
    ave15i = np.asarray(ave15)
    print(ave15i)
    ## Find intercepts of different moving average curves
    idx = np.argwhere(np.diff(np.sign(ave15i - ave10i[:len(ave15i)])!= 0)).reshape(-1)+0 #reshape into one row.
    return idx[1]

# This is based on the method 1 where user can't choose the baseline.
# If wanted to add that, choose method2.
def sum_mean(vector):
    """
    This function returns the mean values.
    """
    a = 0
    for i in vector:
        a = a + i
    return [a,a/len(vector)]


def multiplica(vetor_x, vetor_y):
    a = 0
    for x,y in zip(vetor_x, vetor_y):
        a = a + (x * y)
    return a


def linear_coeff(x, y):
    """
    This function returns the inclination coeffecient and y axis interception coeffecient m and b. 
    """
    m = (multiplica(x,y) - sum_mean(x)[0] * sum_mean(y)[1]) / (multiplica(x,x) - sum_mean(x)[0] * sum_mean(x)[1])  
    b = sum_mean(y)[1] - m * sum_mean(x)[1]
    return m, b


def y_fitted_line(m, b, x):
    y_base = []
    for i in x:
        y = m * i + b
        y_base.append(y)
    return y_base


def linear_background(x, y):
    idx = critical_idx(x, y) + 5 #this is also arbitrary number we can play with.
    m, b = linear_coeff(x[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))], y[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))])
    y_base = y_fitted_line(m, b, x)
    return y_base
