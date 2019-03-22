"""This module tests the calculation functions."""
import numpy as np
import pandas as pd
from voltcycle import calculations


def test_peak_values():
    """This function tests peak_values() function."""
    potentials = [0.500, 0.499, 0.498, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert (isinstance(calculations.peak_values(potentials_d, currents_d),
            np.ndarray), "output is not an array")
    assert (calculations.peak_values(potentials_d, currents_d)[0]
            == 0.498, "array value incorrect for data")
    assert (calculations.peak_values(potentials_d, currents_d)[2]
            == 0.499, "array value incorrect for data")
    assert (calculations.peak_values(potentials_d, currents_d)[1]
            == 8.256, "array value incorrect for data")
    assert (calculations.peak_values(potentials_d, currents_d)[3]
            == 6.998, "array value incorrect for data")


def test_del_potential():
    """This function tests the del_potential function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert (isinstance(calculations.del_potential(potentials_d, currents_d)
                        == np.ndarray), "output is not an array")
    assert (calculations.del_potential(potentials_d, currents_d).shape
                        == (1, 1), "output shape incorrect")
    assert (calculations.del_potential(potentials_d, currents_d).size 
                        == 1, "array size incorrect")
    (np.testing.assert_almost_equal(calculations.del_potential(potentials_d, currents_d),
				    0.001, decimal=3), "value incorrect for data")


def test_half_wave_potential():
    """This function tests half_wave_potential() function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert (isinstance(calculations.half_wave_potential(potentials_d, currents_d)
            == np.ndarray), "output is not an array")
    assert (calculations.half_wave_potential(potentials_d, currents_d).size
            == 1, "out not correct size")
    (np.testing.assert_almost_equal(calculations.half_wave_potential(potentials_d, currents_d),
                                    0.0005, decimal=4), "value incorrect for data")


def test_peak_heights():
    """This function tests peak_heights() function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert (isinstance(calculations.peak_heights(potentials_d, currents_d),
            list), "output is not a list")
    assert (len(calculations.peak_heights(potentials_d, currents_d))
            == 2, "output list is not the correct length")
    np.testing.assert_almost_equal(calculations.peak_heights(potentials_d, currents_d)[0],              7.256, decimal=3, err_msg="max peak height incorrect for data")
    np.testing.assert_almost_equal(calculations.peak_heights(potentials_d, currents_d)[1],              4.998, decimal=3, err_msg="min peak height incorrect for data")


def test_peak_ratio():
    """This function tests peak_ratio() function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert (isinstance(calculations.peak_ratio(potentials_d, currents_d))
            == np.ndarray, "output is not an array")
    assert (len(calculations.peak_ratio(potentials_d, currents_d))
            == 1, "output list is not the correct length")
    np.testing.assert_almost_equal(calculations.peak_ratio(potentials_d, currents_d),
            1.451, decimal=3, err_msg="max peak height incorrect for data")
