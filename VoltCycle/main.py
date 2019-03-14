# main functions we have used so far

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
import peakutils
import copy
from matplotlib import rcParams



def read_cycle(data):
    """This function reads a segment of datafile (corresponding a cycle)
    and generates a dataframe with columns 'Potential' and 'Current'

    Parameters
    __________
    data: segment of data file

    Returns
    _______
    A dataframe with potential and current columns  
    """     

    current = []
    potential = []
    for i in data[3:]:
        current.append(float(i.split("\t")[4]))
        potential.append(float(i.split("\t")[3]))
    zippedList = list(zip(potential, current))
    df = pd.DataFrame(zippedList, columns = ['Potential' , 'Current'])
    return df


def read_file(file):
    """This function reads the raw data file, gets the scanrate and stepsize
    and then reads the lines according to cycle number. Once it reads the data
    for one cycle, it calls read_cycle function to generate a dataframe. It 
    does the same thing for all the cycles and finally returns a dictionary,
    the keys of which are the cycle numbers and the values are the 
    corresponding dataframes.

    Parameters
    __________
    file: raw data file

    Returns:
    ________
    dict_of_df: dictionary of dataframes with keys = cycle numbers and
    values = dataframes for each cycle
    n_cycle: number of cycles in the raw file  
    """   
    dict_of_df = {} 
    h = 0
    l = 0
    n_cycle = 0
    #a = []
    with open(file, 'rt') as f:
        print(file + ' Opened')
        for line in f:
            record = 0
            if not (h and l):
                if line.startswith('SCANRATE'):
                    scan_rate = float(line.split()[2])
                    h = 1
                if line.startswith('STEPSIZE'):
                    step_size = float(line.split()[2])
                    l = 1
            if line.startswith('CURVE'):
                n_cycle += 1
                if n_cycle > 1:
                    number = n_cycle - 1
                    df = read_cycle(a)
                    key_name = 'cycle_' + str(number)
                    #key_name = number
                    dict_of_df[key_name] = copy.deepcopy(df)
                a = []
            if n_cycle:
                a.append(line)
    return dict_of_df, number


#df = pd.DataFrame(list(dict1['df_1'].items()))
#list1, list2 = list(dict1['df_1'].items())
#list1, list2 = list(dict1.get('df_'+str(1)))

def data_frame(dict_cycle, n):
    """Reads the dictionary of dataframes and returns dataframes for each cycle

    Parameters
    __________
    dict_cycle: Dictionary of dataframes
    n: cycle number

    Returns:
    _______
    Dataframe correcponding to the cycle number 
    """
    list1, list2 = (list(dict_cycle.get('cycle_'+str(n)).items()))
    zippedList = list(zip(list1[1], list2[1]))
    data  = pd.DataFrame(zippedList, columns = ['Potential' , 'Current'])
    return data


def plot_fig(dict_cycle, n):
    """For basic plotting of the cycle data
  
    Parameters
    __________
    dict: dictionary of dataframes for all the cycles
    n: number of cycles

    Saves the plot in a file called cycle.png 
    """

    for i in range(n):
        print(i+1)
        df = data_frame(dict_cycle, i+1)
        plt.plot(df.Potential, df.Current, label = "Cycle{}".format(i+1))
        
    #print(df.head())
    plt.xlabel('Voltage')
    plt.ylabel('Current')
    plt.legend()
    plt.savefig('cycle.png')
    print('executed')

#dict_cycle, n_cycle  = read_file('test.txt')
#rcParams.update({'figure.autolayout': True})
#plot(dict_cycle, n_cycle)


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
    for i in range(len(x)-5):  # The reason to minus 5 is to prevent j from running out of index.
        a = 0 
        for j in range(0,5):
            a = a + k[i+j]
        ave5.append(round(a/5, 5)) # keeping 9 desimal points for more accuracy
    ave5 = np.asarray(ave5)
    for i in range(len(x)-15): 
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
    m, b = linear_coeff(x[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))], y[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))])
    y_base = y_fitted_line(m, b, x)
    return y_base


def peak_detection_fxn(data_y):
    """The function takes an input of the column containing the y variables in the dataframe,
    associated with the current. The function calls the split function, which splits the
    column into two arrays, one of the positive and one of the negative values.
    This is because cyclic voltammetry delivers negative peaks, but the peakutils function works
    better with positive peaks. The function also runs on the middle 80% of data to eliminate
    unnecessary noise and messy values associated with pseudo-peaks.The vectors are then imported
    into the peakutils.indexes function to determine the significant peak for each array.
    The values are stored in a list, with the first index corresponding to the top peak and the
    second corresponding to the bottom peak.
    Parameters
    ______________
    y column: must be a column from a pandas dataframe

    Returns
    _____________
    A list with the index of the peaks from the top curve and bottom curve.
    """

    # initialize storage list
    index_list = []

    # split data into above and below the baseline
    col_y1, col_y2 = main.split(data_y)

    # detemine length of data and what 10% of the data is
    len_y = len(col_y1)
    ten_percent = int(np.around(0.1*len_y))

    # adjust both input columns to be the middle 80% of data
    # (take of the first and last 10% of data)
    # this avoid detecting peaks from electrolysis
    # (from water splitting and not the molecule itself,
    # which can form random "peaks")
    mod_col_y2 = col_y2[ten_percent:len_y-ten_percent]
    mod_col_y1 = col_y1[ten_percent:len_y-ten_percent]

    # run peakutils package to detect the peaks for both top and bottom
    peak_top = peakutils.indexes(mod_col_y2, thres=0.99, min_dist=20)
    peak_bottom = peakutils.indexes(abs(mod_col_y1), thres=0.99, min_dist=20)

    # detemine length of both halves of data
    len_top = len(peak_top)
    len_bot = len(peak_bottom)

    # append the values to the storage list
    # manipulate values by adding the ten_percent value back
    # (as the indecies have moved)
    # to detect the actual peaks and not the modified values
    index_list.append(peak_top[int(len_top/2)]+ten_percent)
    index_list.append(peak_bottom[int(len_bot/2)]+ten_percent)

    # return storage list
    # first value is the top, second value is the bottom
    return index_list


def peak_values(DataFrame_x, DataFrame_y):
    """Outputs x (potentials) and y (currents) values from data indices
        given by peak_detection function.

       ----------
       Parameters
       ----------
       DataFrame_x : should be in the form of a pandas DataFrame column.
         For example, df['potentials'] could be input as the column of x
         data.

        DataFrame_y : should be in the form of a pandas DataFrame column.
          For example, df['currents'] could be input as the column of y
          data.

       Returns
       -------
       Result : numpy array of coordinates at peaks in the following order:
         potential of peak on top curve, current of peak on top curve,
         potential of peak on bottom curve, current of peak on bottom curve"""
    index = peak_detection_fxn(DataFrame_y)
    potential1, potential2 = split(DataFrame_x)
    current1, current2 = split(DataFrame_y)
    Peak_values = []
    Peak_values.append(potential2[(index[0])])  # TOPX (bottom part of curve is
    # the first part of DataFrame)
    Peak_values.append(current2[(index[0])])  # TOPY
    Peak_values.append(potential1[(index[1])])  # BOTTOMX
    Peak_values.append(current1[(index[1])])  # BOTTOMY
    Peak_array = np.array(Peak_values)
    return Peak_array


def del_potential(DataFrame_x, DataFrame_y):
    """Outputs the difference in potentials between anoidc and
       cathodic peaks in cyclic voltammetry data.

       Parameters
       ----------
       DataFrame_x : should be in the form of a pandas DataFrame column.
         For example, df['potentials'] could be input as the column of x
         data.

        DataFrame_y : should be in the form of a pandas DataFrame column.
          For example, df['currents'] could be input as the column of y
          data.

        Returns
        -------
        Results: difference in peak potentials in the form of a numpy array."""
    del_potentials = (peak_values(DataFrame_x, DataFrame_y)[0] -
                      peak_values(DataFrame_x, DataFrame_y)[2])
    return del_potentials


def half_wave_potential(DataFrame_x, DataFrame_y):
    """Outputs the half wave potential(redox potential) from cyclic
       voltammetry data.

       Parameters
       ----------
       DataFrame_x : should be in the form of a pandas DataFrame column.
         For example, df['potentials'] could be input as the column of x
         data.

        DataFrame_y : should be in the form of a pandas DataFrame column.
          For example, df['currents'] could be input as the column of y
          data.

       Returns
       -------
       Results : the half wave potential in the form of a
         floating point number."""
    half_wave_potential = (del_potential(DataFrame_x, DataFrame_y))/2
    return half_wave_potential


def peak_heights(DataFrame_x, DataFrame_y):
    """Outputs heights of minimum peak and maximum
         peak from cyclic voltammetry data.

       Parameters
       ----------
       DataFrame_x : should be in the form of a pandas DataFrame column.
         For example, df['potentials'] could be input as the column of x
         data.

        DataFrame_y : should be in the form of a pandas DataFrame column.
          For example, df['currents'] could be input as the column of y
          data.

        Returns
        -------
        Results: height of maximum peak, height of minimum peak
          in that order in the form of a list."""
    current_max = peak_values(DataFrame_x, DataFrame_y)[1]
    current_min = peak_values(DataFrame_x, DataFrame_y)[3]
    x1, x2 = split(DataFrame_x)
    y1, y2 = split(DataFrame_y)
    line_at_min = linear_background(x1, y1)[peak_detection_fxn(DataFrame_y)[1]]
    line_at_max = linear_background(x2, y2)[peak_detection_fxn(DataFrame_y)[0]]
    height_of_max = current_max - line_at_max
    height_of_min = abs(current_min - line_at_min)
    return [height_of_max, height_of_min]


def peak_ratio(DataFrame_x, DataFrame_y):
    """Outputs the peak ratios from cyclic voltammetry data.

       Parameters
       ----------
       DataFrame_x : should be in the form of a pandas DataFrame column.
         For example, df['potentials'] could be input as the column of x
         data.

        DataFrame_y : should be in the form of a pandas DataFrame column.
          For example, df['currents'] could be input as the column of y
          data.

       Returns
       -------
       Result : returns a floating point number, the peak ratio."""
    ratio = (peak_heights(DataFrame_x, DataFrame_y)[0] /
             peak_heights(DataFrame_x, DataFrame_y)[1])
    return ratio
