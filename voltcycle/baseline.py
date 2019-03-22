"""This module consists of all the functions requried
to calculate the baselines."""

# This module is to fit baseline to calculate peak current
# values from cyclic voltammetry data.
# If you wish to choose best fitted baseline,
# checkout branch baseline_old method2.
# If have any questions contact sabiha3@uw.edu

import pandas as pd
import numpy as np


#split forward and backward sweping data, to make it easier for processing.
def split(vector):
    """
    This function takes an array and splits it into equal two half.
    ----------
    Parameters
    ----------
    vector : Can be in any form of that can be turned into numpy array.
    Normally, for the use of this function, it expects pandas DataFrame column.
    For example, df['potentials'] could be input as the column of x data.
    -------
    Returns
    -------
    This function returns two equally splited vector.
    The output then can be used to ease the implementation of peak detection and baseline finding.
    """
    assert isinstance(vector, pd.core.series.Series), "Input should be pandas series"
    split_top = int(len(vector)/2)
    end = int(len(vector))
    vector1 = np.array(vector)[0:split]
    vector2 = np.array(vector)[split_top:end]
    return vector1, vector2


def critical_idx(arr_x, arr_y): ## Finds index where data set is no longer linear
    """
    This function takes x and y values callculate the derrivative of x and y,
    and calculate moving average of 5 and 15 points. Finds intercepts of different
    moving average curves and return the indexs of the first intercepts.
    ----------
    Parameters
    ----------
    x : Numpy array.
    y : Numpy array.
    Normally, for the use of this function, it expects numpy array
    that came out from split function. For example, output of
    split.df['potentials'] could be input for this function as x.
    -------
    Returns
    -------
    This function returns 5th index of the intercepts of different moving average curves.
    User can change this function according to baseline
    branch method 2 to get various indexes..
    """
    assert isinstance(arr_x, np.ndarray), "Input should be numpy array"
    assert isinstance(arr_y == np.ndarray), "Input should be numpy array"
    if arr_x.shape[0] != arr_y.shape[0]:
        raise ValueError("x and y must have same first dimension, but "
                         "have shapes {} and {}".format(arr_x.shape, arr_y.shape))
    k_val = np.diff(arr_y)/(np.diff(arr_x)) #calculated slops of x and y
    ## Calculate moving average for 10 and 15 points.
    ## This two arbitrary number can be tuned to get better fitting.
    ave10 = []
    ave15 = []
    for i in range(len(k_val)-10):
	# The reason to minus 10 is to prevent j from running out of index.
        a_val = 0
        for j in range(0, 5):
            a_val = a_val + k_val[i+j]
        ave10.append(round(a_val/10, 5))
	# keeping 5 desimal points for more accuracy
	# This numbers affect how sensitive to noise.
    for i in range(len(k_val)-15):
        b_val = 0
        for j in range(0, 15):
            b_val = b_val + k_val[i+j]
        ave15.append(round(b_val/15, 5))
    ave10i = np.asarray(ave10)
    ave15i = np.asarray(ave15)
    ## Find intercepts of different moving average curves
    #reshape into one row.
    idx = np.argwhere(np.diff(np.sign(ave15i - ave10i[:len(ave15i)]) != 0)).reshape(-1)+0
    return idx[5]
# This is based on the method 1 where user can't choose the baseline.
# If wanted to add that, choose method2.


def sum_mean(vector):
    """
    This function returns the mean and sum of the given vector.
    ----------
    Parameters
    ----------
    vector : Can be in any form of that can be turned into numpy array.
    Normally, for the use of this function, it expects pandas DataFrame column.
    For example, df['potentials'] could be input as the column of x data.
    """
    assert isinstance(vector == np.ndarray), "Input should be numpy array"
    a_val = 0
    for i in vector:
        a_val = a_val + i
    return [a_val, a_val/len(vector)]


def multiplica(vector_x, vector_y):
    """
    This function returns the sum of the multilica of two given vector.
    ----------
    Parameters
    ----------
    vector_x, vector_y : Output of the split vector function.
    Two inputs can be the same vector or different vector with same length.
    -------
    Returns
    -------
    This function returns a number that is the sum of multiplicity of given two vector.
    """
    assert isinstance(vector_x == np.ndarray), "Input should be numpy array"
    assert isinstance(vector_y == np.ndarray), "Input should be numpy array"
    a_val = 0
    for vec_x, vec_y in zip(vector_x, vector_y):
        a_val = a_val + (vec_x * vec_y)
    return a_val

def linear_coeff(vec_x, vec_y):
    """
    This function returns the inclination coeffecient and y axis interception coeffecient m and b.
    ----------
    Parameters
    ----------
    x : Output of the split vector function.
    y : Output of the split vector function.
    -------
    Returns
    -------
    float number of m and b.
    """
    m_val = ((multiplica(vec_x, vec_y) - sum_mean(vec_x)[0] * sum_mean(vec_y)[1])/
             (multiplica(vec_x, vec_x) - sum_mean(vec_x)[0] * sum_mean(vec_x)[1]))
    b_val = sum_mean(vec_y)[1] - m_val * sum_mean(vec_x)[1]
    return m_val, b_val


def y_fitted_line(m_val, b_val, vec_x):
    """
    This function returns the fitted baseline constructed by coeffecient m and b and x values.
    ----------
    Parameters
    ----------
    x : Output of the split vector function. x value of the input.
    m : inclination of the baseline.
    b : y intercept of the baseline.
    -------
    Returns
    -------
    List of constructed y_labels.
    """
    y_base = []
    for i in vec_x:
        y_val = m_val * i + b_val
        y_base.append(y_val)
    return y_base


def linear_background(vec_x, vec_y):
    """
    This function is wrapping function for calculating linear fitted line.
    It takes x and y values of the cv data, returns the fitted baseline.
    ----------
    Parameters
    ----------
    x : Output of the split vector function. x value of the cyclic voltammetry data.
    y : Output of the split vector function. y value of the cyclic voltammetry data.
    -------
    Returns
    -------
    List of constructed y_labels.
    """
    assert isinstance(vec_x, np.ndarray), "Input of the function should be numpy array"
    assert isinstance(vec_y, np.ndarray), "Input of the function should be numpy array"
    idx = critical_idx(vec_x, vec_y) + 5 #this is also arbitrary number we can play with.
    m_val, b_val = (linear_coeff(vec_x[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))],
                                 vec_y[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))]))
    y_base = y_fitted_line(m_val, b_val, vec_x)
    return y_base
