import numpy as np
import pandas as pd


import calculations


def test_peak_values():
    """This function tests get_peak_potentials() function."""
    potentials = [0.167, 0.251, 0.500]
    currents = [-46.370, 33.153, 7.040]
    index = [0, 1]
    assert type(calculations.peak_values(potentials, index)) == np.ndarray, "output is not an array"
    assert calculations.peak_values(potentials, index)[0] == 0.167, "array value incorrect for data"
    assert calculations.peak_values(potentials, index)[1] == 0.251, "array value incorrect for data"
    assert calculations.peak_values(currents, index)[0] == -46.370, "array value incorrect for data"
    assert calculations.peak_values(currents, index)[1] == 33.153, "array value incorrect for data"
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
