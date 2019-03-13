import numpy as np
import pandas as pd


import calculations


def test_peak_values():
    """This function tests peak_values() function."""
    potentials = [0.500, 0.499, 0.498, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    def peak_detection(Dataframe_y):
        list = [0, 1]
        return list

    def split(vector):
        split = int(len(vector)/2)
        end = int(len(vector))
        vector1 = np.array(vector)[0:split]
        vector2 = np.array(vector)[split:end]
        return vector1, vector2

    assert type(calculations.peak_values(potentials_d, currents_d)) == np.ndarray, "output is not an array"
    assert calculations.peak_values(potentials_d, currents_d)[0] == 0.498, "array value incorrect for data"
    assert calculations.peak_values(potentials_d, currents_d)[2] == 0.499, "array value incorrect for data"
    assert calculations.peak_values(potentials_d, currents_d)[1] == 8.256, "array value incorrect for data"
    assert calculations.peak_values(potentials_d, currents_d)[3] == 6.998, "array value incorrect for data"
    return


def test_del_potential():
    """This function tests del_potential() function."""
    potentials = [0.167, 0.251, 0.500, 0.497]
    assert type(calculations.del_potential(potentials, potentials, [1], [0])) == np.ndarray, "output data type not an array."
    np.testing.assert_almost_equal(calculations.del_potential(potentials, potentials, [1], [0]), (0.251-0.167), decimal=3), "output values incorrect."
    np.testing.assert_almost_equal(calculations.del_potential(potentials, potentials, [2, 3], [0, 1])[0], (0.500-0.167), decimal=3), "output values incorrect."
    np.testing.assert_almost_equal(calculations.del_potential(potentials, potentials, [2, 3], [0, 1])[1], (0.497-0.251), decimal=3), "output values incorrect."
    assert (del_potential(potentials, potentials, [2, 3], [0, 1])).shape == (2,), "output array has incorrect shape."
    return


def test_half_wave_potential():
    """This function tests half_potentials() function."""
    potentials = [0.167, 0.251, 0.500, 0.497]
    assert type(calculations.half_wave_potential(potentials, potentials, [0], [1])) == np.ndarray, "output data type not an array"
    np.testing.assert_almost_equal(calculations.half_wave_potential(potentials, potentials, [1], [0]), ((0.251-0.167)/2), decimal=3), "output array values incorrect."
    np.testing.assert_almost_equal(calculations.half_wave_potential(potentials, potentials, [2, 3], [0, 1])[0], ((0.500-0.167)/2), decimal=3), "output array values incorrect"
    np.testing.assert_almost_equal(calculations.half_wave_potential(potentials, potentials, [2, 3], [0, 1])[1], ((0.497-0.252)/2), decimal=3), "output array values incorrect."
    assert calculations.half_wave_potential(potentials, potentials, [2, 3], [0, 1]).shape == (2,)
    return
