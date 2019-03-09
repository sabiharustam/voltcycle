import numpy as np
import pandas as pd


def peak_potentials(data, index, potential_column_name):
    """Outputs potentials of given peaks in cyclic voltammetry data.

       Parameters
       ----------
       data : Must be in the form of a pandas DataFrame

       index : integer(s) in the form of a list or numpy array

       potential_column_name : the name of the column of the DataFrame
         which contains potentials from cyclic voltammogram. If a string,
         must be input with single or double quotation marks

       Returns
       -------
       Result : numpy array of potentials at peaks."""
    series = data.iloc[index][potential_column_name]
    potentials_array = (series).values
    return potentials_array


def del_potential(data, index, potential_column_name):
    """Outputs the difference in potentials between anodic and cathodic peaks
       in cyclic voltammetry data.

       Parameters
       ----------
       data : Must be in the form of a pandas DataFrame

       index : integer(s) in the form of a list or numpy array

       potential_column_name : the name of the column of the DataFrame
         which contains potentials from cyclic voltammogram. If a string,
         must be input with single or double quotation marks.

       Returns
       -------
       Results : difference in the form of a floating point number. """
    del_potential = (
        peak_potentials(data, index, potential_column_name)[1] -
        peak_potentials(data, index, potential_column_name)[0]
    )
    return del_potential


def half_wave_potential(data, index, potential_column_name):
    """Outputs the half wave potential(redox potential) from cyclic
       voltammetry data.

       Parameters
       ----------
       data : Must be in the form of a pandas DataFrame

       index : integer(s) in the form of a list or numpy array

       potential_column_name : the name of the column of the DataFrame
         which contains potentials from cyclic voltammogram. If a string,
         must be input with single or double quotation marks

       Returns
       -------
       Results : the half wave potential in the form of a
         floating point number."""
    half_wave_potential = (del_potential(data, index, potential_column_name))/2
    return half_wave_potential
