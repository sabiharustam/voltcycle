import numpy as np
import pandas as pd


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
    index = peak_detection(DataFrame_y)
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
    line_at_min = linear_background(x1, y1)[peak_detection(DataFrame_y)[1]]
    line_at_max = linear_background(x2, y2)[peak_detection(DataFrame_y)[0]]
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
       Result : returns a floating point number, the peak ratio
       """
    ratio = (peak_heights(DataFrame_x, DataFrame_y)[0] /
             peak_heights(DataFrame_x, DataFrame_y)[1])
    return ratio
