import numpy as np
import pandas as pd


def peak_values(data, index):
    """Outputs potentials of given peaks in cyclic voltammetry data.

       Parameters
       ----------
       data : should be in the form of a list or numpy array

       index : Peak indexes must be integer(s) in the form of a list
         or numpy array

       Returns
       -------
       Result : numpy array of potentials at peaks."""
    values_list = []
    for i in index:
        values_list.append(data[i])
    values_array = np.array(values_list)
    return values_array


def del_potential(data1, data2, index1, index2):
    """Outputs the absolute difference in potentials between anodic and
       cathodic peaks in cyclic voltammetry data.

       Parameters
       ----------
       data1 : Potential data must be in the form of a list or numpy array.

       data2 : Potential data must be in the form of a list or numpy array.

       index1 : Peak indexes must be integer(s) in the form of a list or
        numpy array. Be careful when subtracting multiple peaks from multiple
        peaks. Array shapes must be compatible for subtraction. i. e.
        index1 = [6], index2 = [4, 5] will work and data2[4] and data2[5]
        will each be subtracted from data1[6]; an array with shape (1,) can
        be paired with arrays of differents shapes. index1 = [2, 3] and
        index2 = [3, 4, 6] will not work. Index arrays or lists of the same
        shape/length will work. For example, index1 = [3, 676] and
        index2 = [6, 784] will result in data2[6] being subtracted from
        data1[3] and data2[784] being subtracted from data1[676].

       index2 : integer(s) in the form of a list or numpy array. See above
        entry for index1 if needed.

       Returns
       -------
       Results : difference in peak potentials in the form of a numpy array """
    del_potential = (peak_values(data1, index1) -
                     peak_values(data2, index2))
    return del_potential


def half_wave_potential(data1, data2, index1, index2):
    """Outputs the half wave potential(redox potential) from cyclic
       voltammetry data.

       Parameters
       ----------
       data1 : Potential data must be in the form of a list or numpy array.

       data2 : Potential data must be in the form of a list or numpy array.

       index1 : Peak indexes must be integer(s) in the form of a list or
        numpy array. Be careful when subtracting multiple peaks from
        multiple peaks. Array shapes must be compatible for subtraction.
        i. e. index1 = [6], index2 = [4, 5] will work and data2[4] and
        data2[5] will each be subtracted from data1[6]; an array with
        shape (1,) can be paired with arrays of differents shapes.
        index1 = [2, 3] and index2 = [3, 4, 6] will not work. Index
        arrays or lists of the same shape/length will work. For
        example, index1 = [3, 676] and index2 = [6, 784] will result
        in data2[6] being subtracted from data1[3] and data2[784]
        being subtracted from data1[676]. Each value of the output
        array will be divided by 2.

       index2 : integer(s) in the form of a list or numpy array.
        See above entry for index1 if needed.

       Returns
       -------
       Results : the half wave potential in the form of a
         floating point number."""
    half_wave_potential = (del_potential(data1, data2, index1, index2))/2
    return half_wave_potential
