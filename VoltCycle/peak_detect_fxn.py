"""This module consists of functions involved in peak detection.
It consists of two functions, split column, which splits each of
the y columns in half to be accesible for peak detections, and
peak_detection which return the indecies of the detected peaks in
a list to be used by the subsequent calculation functions."""

import peakutils
import numpy as np


def split_column(column):
    """This functions splits the columns into two arrays one of the
positive and one of the negative values."""
    first_half = int(len(column)/2)
    second_half = int(len(column))
    col_array = np.array(column)
    col1 = col_array[0:first_half]
    col2 = col_array[(first_half):second_half]
    return col1, col2



def peak_detection_fxn(data_y):
    """ peak_detection(dataframe['y column'])
    This function returns a list of the indecies of the y values of the
peaks detected in the dataset. The function takes an input of the column
containing the y variables in the dataframe. This column is then split
into two arrays, one of the positive and one of the negative values.
This is because cyclic voltammetry delivers negative peaks however the
peakutils function work better with positive peaks. The absolute values
of each of these vectors are then imported into the peakutils.indexes
function to determine the significant peak(s) for each array. The
value(s) are then saved as a list."""

    index_list = []

    col_y1, col_y2 = split_column(data_y)

    peak_top = peakutils.indexes(col_y2, thres=0.99, min_dist=0.001)
    peak_bottom = peakutils.indexes(abs(col_y1), thres=0.99, min_dist=0.001)
    len_top = len(peak_top)
    len_bot = len(peak_bottom)

    index_list.append([peak_top[int(len_top/2)], peak_bottom[int(len_bot/2)]])

    return index_list
