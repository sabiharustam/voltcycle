"""This module consists of all the functions utilized."""
# This is a tool to automate cyclic voltametry analysis.
# Current Version = 1

import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import peakutils


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
<<<<<<< HEAD
    zippedList = list(zip(potential, current))
    df = pd.DataFrame(zippedList, columns=['Potential', 'Current'])
    return df
=======
    zipped_list = list(zip(potential, current))
    dataframe = pd.DataFrame(zipped_list, columns=['Potential', 'Current'])
    return dataframe
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be


def read_file_dash(lines):
    """This function is exactly similar to read_file, but it is for dash

    Parameters
    __________
    file: lines from dash input file

    Returns:
    ________
    dict_of_df: dictionary of dataframes with keys = cycle numbers and
    values = dataframes for each cycle
    n_cycle: number of cycles in the raw file
    """
    dict_of_df = {}
<<<<<<< HEAD
    h = 0
    j = 0
=======
    h_val = 0
    l_val = 0
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    n_cycle = 0
    number = 0
    # a = []
    # with open(file, 'rt') as f:
    #    print(file + ' Opened')
    for line in lines:
        record = 0
<<<<<<< HEAD
        if not (h and j):
=======
        if not (h_val and l_val):
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
            if line.startswith('SCANRATE'):
                scan_rate = float(line.split()[2])
                h_val = 1
            if line.startswith('STEPSIZE'):
                step_size = float(line.split()[2])
<<<<<<< HEAD
                j = 1
=======
                l_val = 1
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
        if line.startswith('CURVE'):
            n_cycle += 1
            if n_cycle > 1:
                number = n_cycle - 1
                data = read_cycle(a_val)
                key_name = 'cycle_' + str(number)
<<<<<<< HEAD
                # key_name = number
                dict_of_df[key_name] = copy.deepcopy(df)
            a = []
=======
                #key_name = number
                dict_of_df[key_name] = copy.deepcopy(data)
            a_val = []
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
        if n_cycle:
            a_val.append(line)
    return dict_of_df, number


def read_file(file):
    """This function reads the raw data file, gets the scanrate and stepsize
    and then reads the lines according to cycle number. Once it reads the data
<<<<<<< HEAD
    for one cycle, it calls read_cycle function to generate a dataframe. It
=======
    for one cycle, it calls read_cycle function to denerate a dataframe. It
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
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
<<<<<<< HEAD
    h = 0
    j = 0
    n_cycle = 0
    # a = []
    with open(file, 'rt') as f:
=======
    h_val = 0
    l_val = 0
    n_cycle = 0
    #a = []
    with open(file, 'rt') as f_val:
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
        print(file + ' Opened')
        for line in f_val:
            record = 0
            if not (h_val and l_val):
                if line.startswith('SCANRATE'):
                    scan_rate = float(line.split()[2])
                    h_val = 1
                if line.startswith('STEPSIZE'):
                    step_size = float(line.split()[2])
<<<<<<< HEAD
                    j = 1
=======
                    l_val = 1
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
            if line.startswith('CURVE'):
                n_cycle += 1
                if n_cycle > 1:
                    number = n_cycle - 1
                    data = read_cycle(a_val)
                    key_name = 'cycle_' + str(number)
<<<<<<< HEAD
                    # key_name = number
                    dict_of_df[key_name] = copy.deepcopy(df)
                a = []
=======
                    #key_name = number
                    dict_of_df[key_name] = copy.deepcopy(data)
                a_val = []
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
            if n_cycle:
                a_val.append(line)
    return dict_of_df, number
# df = pd.DataFrame(list(dict1['df_1'].items()))
# list1, list2 = list(dict1['df_1'].items())
# list1, list2 = list(dict1.get('df_'+str(1)))

<<<<<<< HEAD

def data_frame(dict_cycle, n):
=======
#df = pd.DataFrame(list(dict1['df_1'].items()))
#list1, list2 = list(dict1['df_1'].items())
#list1, list2 = list(dict1.get('df_'+str(1)))


def data_frame(dict_cycle, number):
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    """Reads the dictionary of dataframes and returns dataframes for each cycle

    Parameters
    __________
    dict_cycle: Dictionary of dataframes
    n: cycle number

    Returns:
    _______
    Dataframe correcponding to the cycle number
    """
<<<<<<< HEAD
    list1, list2 = (list(dict_cycle.get('cycle_'+str(n)).items()))
    zippedList = list(zip(list1[1], list2[1]))
    data = pd.DataFrame(zippedList, columns=['Potential', 'Current'])
=======
    list1, list2 = (list(dict_cycle.get('cycle_'+str(number)).items()))
    zipped_list = list(zip(list1[1], list2[1]))
    data = pd.DataFrame(zipped_list, columns=['Potential', 'Current'])
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    return data


def plot_fig(dict_cycle, number):
    """For basic plotting of the cycle data

    Parameters
    __________
    dict: dictionary of dataframes for all the cycles
    n: number of cycles

    Saves the plot in a file called cycle.png
    """

    for i in range(number):
        print(i+1)
<<<<<<< HEAD
        df = data_frame(dict_cycle, i+1)
        plt.plot(df.Potential, df.Current, label="Cycle{}".format(i+1))

    # print(df.head())
=======
        data = data_frame(dict_cycle, i+1)
        plt.plot(data.Potential, data.Current, label="Cycle{}".format(i+1))

    print(data.head())
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    plt.xlabel('Voltage')
    plt.ylabel('Current')
    plt.legend()
    plt.savefig('cycle.png')
    print('executed')


# split forward and backward sweping data, to make it easier for processing.
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
<<<<<<< HEAD
    The output then can be used to ease the implementation
    of peak detection and baseline finding.
    """
    (assert type(vector) == pd.core.series.Series,
        "Input of the function should be pandas series")
    split = int(len(vector)/2)
=======
    The output then can be used to ease the implementation of peak detection and baseline finding.
    """
    assert isinstance(vector, pd.core.series.Series), "Input should be pandas series"
    split_top = int(len(vector)/2)
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    end = int(len(vector))
    vector1 = np.array(vector)[0:split]
    vector2 = np.array(vector)[split_top:end]
    return vector1, vector2


<<<<<<< HEAD
def critical_idx(x, y):  # Finds index where data set is no longer linear
    """
    This function takes x and y values callculate the derrivative
    of x and y, and calculate moving average of 5 and 15 points.
    Finds intercepts of different moving average curves and
    return the indexs of the first intercepts.
=======
def critical_idx(arr_x, arr_y): ## Finds index where data set is no longer linear
    """
    This function takes x and y values callculate the derrivative of x and y,
    and calculate moving average of 5 and 15 points. Finds intercepts of different
    moving average curves and return the indexs of the first intercepts.
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    ----------
    Parameters
    ----------
    x : Numpy array.
    y : Numpy array.
<<<<<<< HEAD
    Normally, for the use of this function, it expects
    numpy array that came out from split function.
    For example, output of split.df['potentials']
    could be input for this function as x.
    -------
    Returns
    -------
    This function returns 5th index of the intercepts
    of different moving average curves.
    User can change this function according to
    baseline branch method 2 to get various indexes.
    """
    (assert type(x) == np.ndarray,
     "Input of the function should be numpy array")
    (assert type(y) == np.ndarray,
     "Input of the function should be numpy array")
    if x.shape[0] != y.shape[0]:
        raise ValueError("x and y must have same first dimension, but "
                         "have shapes {} and {}".format(x.shape, y.shape))
    k = np.diff(y)/(np.diff(x))  # calculated slops of x and y
    # Calculate moving average for 10 and 15 points.
    # This two arbitrary number can be tuned to get better fitting.
    ave10 = []
    ave15 = []
    for i in range(len(k)-10):
        # The reason to minus 10 is to prevent j from running out of index.
        a = 0
        for j in range(0, 5):
            a = a + k[i+j]
        ave10.append(round(a/10, 5))
    # keeping 5 desimal points for more accuracy
    # This numbers affect how sensitive to noise.
    for i in range(len(k)-15):
        b = 0
        for j in range(0, 15):
            b = b + k[i+j]
        ave15.append(round(b/15, 5))
    ave10i = np.asarray(ave10)
    ave15i = np.asarray(ave15)
    # Find intercepts of different moving average curves
    # reshape into one row.
    idx = {np.argwhere(np.diff(np.sign(ave15i -
                               ave10i[:len(ave15i)]) != 0)).reshape(-1) + 0}
=======
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
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
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
<<<<<<< HEAD
    (assert type(vector) == np.ndarray,
     "Input of the function should be numpy array")
    a = 0
    for i in vector:
        a = a + i
    return [a, a/len(vector)]
=======
    assert isinstance(vector == np.ndarray), "Input should be numpy array"
    a_val = 0
    for i in vector:
        a_val = a_val + i
    return [a_val, a_val/len(vector)]
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be


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
    This function returns a number that is the sum
    of multiplicity of given two vector.
    """
<<<<<<< HEAD
    (assert type(vector_x) == np.ndarray,
     "Input of the function should be numpy array")
    (assert type(vector_y) == np.ndarray,
     "Input of the function should be numpy array")
    a = 0
    for x, y in zip(vector_x, vector_y):
        a = a + (x * y)
    return a


def linear_coeff(x, y):
    """
    This function returns the inclination coeffecient and
    y axis interception coeffecient m and b.
=======
    assert isinstance(vector_x == np.ndarray), "Input should be numpy array"
    assert isinstance(vector_y == np.ndarray), "Input should be numpy array"
    a_val = 0
    for vec_x, vec_y in zip(vector_x, vector_y):
        a_val = a_val + (vec_x * vec_y)
    return a_val


def linear_coeff(vec_x, vec_y):
    """
    This function returns the inclination coeffecient and y axis interception coeffecient m and b.
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
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
<<<<<<< HEAD
    m = {(multiplica(x, y) - sum_mean(x)[0] * sum_mean(y)[1]) /
         (multiplica(x, x) - sum_mean(x)[0] * sum_mean(x)[1])}
    b = sum_mean(y)[1] - m * sum_mean(x)[1]
    return m, b
=======
    m_val = ((multiplica(vec_x, vec_y) - sum_mean(vec_x)[0] * sum_mean(vec_y)[1])/
             (multiplica(vec_x, vec_x) - sum_mean(vec_x)[0] * sum_mean(vec_x)[1]))
    b_val = sum_mean(vec_y)[1] - m_val * sum_mean(vec_x)[1]
    return m_val, b_val
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be


def y_fitted_line(m_val, b_val, vec_x):
    """
<<<<<<< HEAD
    This function returns the fitted baseline constructed
    by coeffecient m and b and x values.
=======
    This function returns the fitted baseline constructed by coeffecient m and b and x values.
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
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
<<<<<<< HEAD
    x : Output of the split vector function. x value
    of the cyclic voltammetry data.
    y : Output of the split vector function. y value
    of the cyclic voltammetry data.
=======
    x : Output of the split vector function. x value of the cyclic voltammetry data.
    y : Output of the split vector function. y value of the cyclic voltammetry data.
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    -------
    Returns
    -------
    List of constructed y_labels.
    """
<<<<<<< HEAD
    assert type(x) == np.ndarray, "Input of the function should be numpy array"
    assert type(y) == np.ndarray, "Input of the function should be numpy array"
    idx = critical_idx(x, y) + 5
    # this is also arbitrary number we can play with.
    m, b = {linear_coeff(x[(idx - int(0.5 * idx)): (idx + int(0.5 * idx))],
                         y[(idx - int(0.5 * idx)): (idx + int(0.5 * idx))])}
    y_base = y_fitted_line(m, b, x)
=======
    assert isinstance(vec_x, np.ndarray), "Input of the function should be numpy array"
    assert isinstance(vec_y, np.ndarray), "Input of the function should be numpy array"
    idx = critical_idx(vec_x, vec_y) + 5 #this is also arbitrary number we can play with.
    m_val, b_val = (linear_coeff(vec_x[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))],
                                 vec_y[(idx - int(0.5 * idx)) : (idx + int(0.5 * idx))]))
    y_base = y_fitted_line(m_val, b_val, vec_x)
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
    return y_base


def peak_detection_fxn(data_y):
    """The function takes an input of the column containing the y variables in
    the dataframe, associated with the current. The function calls the split
    function, which splits the column into two arrays, one of the positive and
    one of the negative values. This is because cyclic voltammetry delivers
    negative peaks,but the peakutils function works better with positive peaks.
    The function also runs on the middle 80% of data to eliminate unnecessary
    noise and messy values associated with pseudo-peaks.The vectors are then
    imported into the peakutils. Indexes function to determine the significant
    peak for each array. The values are stored in a list, with the first index
    corresponding to the top peak and the second corresponding to the bottom
    peak.
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
    col_y1, col_y2 = split(data_y)  # removed main. head.

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

def peak_values(dataframe_x, dataframe_y):
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
    index = peak_detection_fxn(dataframe_y)
    potential1, potential2 = split(dataframe_x)
    current1, current2 = split(dataframe_y)
    peak_values = []
    peak_values.append(potential2[(index[0])])  # TOPX (bottom part of curve is
    # the first part of DataFrame)
    peak_values.append(current2[(index[0])])  # TOPY
    peak_values.append(potential1[(index[1])])  # BOTTOMX
    peak_values.append(current1[(index[1])])  # BOTTOMY
    peak_array = np.array(peak_values)
    return peak_array


def del_potential(dataframe_x, dataframe_y):
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
        Results: difference in peak potentials."""
    del_potentials = (peak_values(dataframe_x, dataframe_y)[0] -
                      peak_values(dataframe_x, dataframe_y)[2])
    return del_potentials


def half_wave_potential(dataframe_x, dataframe_y):
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
       Results : the half wave potential."""
    half_wave_pot = (del_potential(dataframe_x, dataframe_y))/2
    return half_wave_pot


def peak_heights(dataframe_x, dataframe_y):
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
    current_max = peak_values(dataframe_x, dataframe_y)[1]
    current_min = peak_values(dataframe_x, dataframe_y)[3]
    col_x1, col_x2 = split(dataframe_x)
    col_y1, col_y2 = split(dataframe_y)
    line_at_min = linear_background(col_x1, col_y1)[peak_detection_fxn(dataframe_y)[1]]
    line_at_max = linear_background(col_x2, col_y2)[peak_detection_fxn(dataframe_y)[0]]
    height_of_max = current_max - line_at_max
    height_of_min = abs(current_min - line_at_min)
    return [height_of_max, height_of_min]


def peak_ratio(dataframe_x, dataframe_y):
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
       Result : returns a the peak ratio."""
    ratio = (peak_heights(dataframe_x, dataframe_y)[0] /
             peak_heights(dataframe_x, dataframe_y)[1])
    return ratio


def data_analysis(data):
    """This function returns a dictionary consisting of
    the relevant values. This can be seen in the user
    interface (Dash) as well."""
    results_dict = {}

    # df = main.data_frame(dict_1,1)
    x_val = data['Potential']
    y_val = data['Current']
    # Peaks are here [list]
    peak_index = peak_detection_fxn(y_val)
    # Split x,y to get baselines
<<<<<<< HEAD
    x1, x2 = core.split(x)
    y1, y2 = core.split(y)
    y_base1 = core.linear_background(x1, y1)
    y_base2 = core.linear_background(x2, y2)
    # Calculations based on baseline and peak
    values = core.peak_values(x, y)
    Et = values[0]
    Eb = values[2]
    dE = core.del_potential(x, y)
    half_E = min(Et, Eb) + core.half_wave_potential(x, y)
    ia = core.peak_heights(x, y)[0]
    ic = core.peak_heights(x, y)[1]
    ratio_i = core.peak_ratio(x, y)
    results_dict['Peak Current Ratio'] = ratio_i
    results_dict['Ipc (A)'] = ic
    results_dict['Ipa (A)'] = ia
    results_dict['Epc (V)'] = Eb
    results_dict['Epa (V)'] = Et
    results_dict['∆E (V)'] = dE
    results_dict['Redox Potential (V)'] = half_E
    if dE > 0.3:
=======
    col_x1, col_x2 = split(x_val)
    col_y1, col_y2 = split(y_val)
    y_base1 = linear_background(col_x1, col_y1)
    y_base2 = linear_background(col_x2, col_y2)
    # Calculations based on baseline and peak
    values = peak_values(x_val, y_val)
    esub_t = values[0]
    esub_b = values[2]
    dof_e = del_potential(x_val, y_val)
    half_e = min(esub_t, esub_b) + half_wave_potential(x_val, y_val)
    ipa = peak_heights(x_val, y_val)[0]
    ipc = peak_heights(x_val, y_val)[1]
    ratio_i = peak_ratio(x_val, y_val)
    results_dict['Peak Current Ratio'] = ratio_i
    results_dict['Ipc (A)'] = ipc
    results_dict['Ipa (A)'] = ipa
    results_dict['Epc (V)'] = esub_b
    results_dict['Epa (V)'] = esub_t
    results_dict['∆E (V)'] = dof_e
    results_dict['Redox Potential (V)'] = half_e
    if dof_e > 0.3:
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
        results_dict['Reversible'] = 'No'
    else:
        results_dict['Reversible'] = 'Yes'

<<<<<<< HEAD
    if half_E > 0 and 'Yes' in results_dict.values():
        results_dict['Type'] = 'Catholyte'
    elif 'Yes' in results_dict.values():
        results_dict['Type'] = 'Anolyte'
    return results_dict, x1, x2, y1, y2, y_base1, y_base2, peak_index
    # return results_dict
=======
    if half_e > 0 and  'Yes' in results_dict.values():
        results_dict['Type'] = 'Catholyte'
    elif 'Yes' in results_dict.values():
        results_dict['Type'] = 'Anolyte'
    return results_dict, col_x1, col_x2, col_y1, col_y2, y_base1, y_base2, peak_index
    #return results_dict
>>>>>>> 69efa78d566312fbfc5e8d5b130e3e2bf7cbb2be
