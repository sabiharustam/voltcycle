import numpy as np
import pandas as pd

def peak_potentials(data, index, potential_column_name):
    """This function returns the peak potentials. Data input should be a DataFrame. Index must be an integer or integers
    input in the form of a list or a numpy array. potential_column_name input should be surrounded by single or double 
    quotation marks."""
    series = data.iloc[index][potential_column_name]
    potentials_array = (series).values
    return potentials_array

def del_potential(data, index, potential_column_name):
    del_potential = (peak_potentials(data, index, potential_column_name)[1] - peak_potentials(data, index, potential_column_name)[0])
    return del_potential

def half_wave_potential(data, index, potential_column_name):
    """This function returns the half wave potential. Data input should be a DataFrame. Index must be an integer or integers
    input in the form of a list of a numpy array. potential_column_name input should be surrounded by single or double 
    quotation marks."""
    half_wave_potential = (del_potential(data, index, potential_column_name))/2
    return half_wave_potential
