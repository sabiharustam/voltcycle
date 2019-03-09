import peakutils
import numpy as np

"""This module consists of functions involved in peak detection.
It consists of three functions, split column, which splits each of
the y columns in half to be accesible for peak detections,
peak_detection which return the indecies of the detected peaks and
interpolation, which enhances the resolution of the peaks and returns
the x values in an array."""


def split_column(column):
    """This functions splits the columns into two arrays one of the
positive and one of the negative values."""
    first_half = int(len(column)/2)
    second_half = int(len(column))
    col_array = np.array(column)
    col1 = col_array[0:first_half]
    col2 = col_array[(first_half+1):second_half]
    return col1, col2


def peak_detection(data_y):
    """ peak_detection(dataframe['y column'])
    This function returns a list of the indecies of the y values of the
peaks detected in the dataset.
    The function takes an input of the column containing the y variables
in the dataframe.
    This column is then split into two arrays, one of the positive and
one of the negative values.
    This is because cyclic voltammetry delivers negative peaks however
the peakutils function work better with positive peaks.
    The absolute values of each of these vectors are then imported into
the peakutils.indexes
    function to determine the significant peak(s) for each array. The
value(s) are then saved as a list."""

    index_list = []

    col_y1, col_y2 = split_column(data_y)

    peak_top = peakutils.indexes(abs(col_y1), thres=0.5, min_dist=0.001)
    peak_bottom = peakutils.indexes(abs(col_y2), thres=0.5, min_dist=0.001)
    index_list.append([peak_top[0], peak_bottom[0]])

    return index_list


def interpolation(data_x, data_y):
    """interpolation(dataframe['x column'], dataframe['y column'])
    This function returns a list of the fitted values of the peals in
the dataset.
    It calls the peak_detection function and type casts the outputs to
numpy ndarrays
    (as that is what the peakutils.interpolation function takes in).
    The function also typecasts the x and y value columns to numpy
ndarrays.
    The function then uses the peakutils.interpolation function to
enhance the resolution of the peak values.
    This gives more precise numbers. The function returns a list."""

    x_data = np.array(data_x)
    y_data = np.array(data_y)

    index = peak_detection(data_y)[0]
    index = np.asarray(index)

    smooth_index = []
    smooth = peakutils.interpolate(x_data, y_data, ind=index)
    smooth_index.append(list(smooth))

    return smooth_index
