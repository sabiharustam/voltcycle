import numpy as np
import pandas as pd


from functions import calculations


def peak_detection(Dataframe_y):
    list = [0, 1]
    return list


def split(vector):
    split = int(len(vector)/2)
    end = int(len(vector))
    vector1 = np.array(vector)[0:split]
    vector2 = np.array(vector)[split:end]
    return vector1, vector2


def linear_background(x, y):
    fake_line_list = [1, 2, 3, 4]
    fake_line_array = np.array(fake_line_list)
    return fake_line_array


def test_peak_values():
    """This function tests peak_values() function."""
    potentials = [0.500, 0.499, 0.498, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert type(calculations.peak_values(potentials_d, currents_d)) == np.ndarray, "output is not an array"
    assert calculations.peak_values(potentials_d, currents_d)[0] == 0.498, "array value incorrect for data"
    assert calculations.peak_values(potentials_d, currents_d)[2] == 0.499, "array value incorrect for data"
    assert calculations.peak_values(potentials_d, currents_d)[1] == 8.256, "array value incorrect for data"
    assert calculations.peak_values(potentials_d, currents_d)[3] == 6.998, "array value incorrect for data"
    return


def test_del_potential():
    """This function tests the del_potential function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert type(calculations.del_potential(potentials_d, currents_d)) == np.ndarray, "output is not an array"
    assert calculations.del_potential(potentials_d, currents_d).shape == (1,), "output shape incorrect"
    assert calculations.del_potential(potentials_d, currents_d).size == 1, "array size incorrect"
    np.testing.assert_almost_equal(calculations.del_potential(potentials_d, currents_d), 0.001, decimal=3), "value incorrect for data"
    return


def test_half_wave_potential():
    """This function tests half_wave_potential() function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert type(calculations.half_wave_potential(potentials_d, currents_d)) == np.ndarray, "output is not an array"
    assert calculations.half_wave_potential(potentials_d, currents_d).size == 1, "out not correct size"
    np.testing.assert_almost_equal(calculations.half_wave_potential(potentials_d, currents_d), 0.0005, decimal=4), "value incorrect for data"
    return


def test_peak_heights():
    """This function tests peak_heights() function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert type(calculations.peak_heights(potentials_d, currents_d)) == list, "output is not a list"
    assert len(calculations.peak_heights(potentials_d, currents_d)) == 2, "output list is not the correct length"
    np.testing.assert_almost_equal(calculations.peak_heights(potentials_d, currents_d)[0], 7.256, decimal=3), "max peak height incorrect for data"
    np.testing.assert_almost_equal(calculations.peak_heights(potentials_d, currents_d)[1], 4.998, decimal=3), "min peak height incorrect for data"
    return


def test_peak_ratio():
    """This function tests peak_ratio() function."""
    potentials = [0.500, 0.498, 0.499, 0.497]
    currents = [7.040, 6.998, 8.256, 8.286]
    potentials_d = pd.DataFrame(potentials)
    currents_d = pd.DataFrame(currents)

    assert type(calculations.peak_ratio(potentials_d, currents_d)) == np.ndarray, "output is not an array"
    assert len(calculations.peak_ratio(potentials_d, currents_d)) == 1, "output list is not the correct length"
    np.testing.assert_almost_equal(calculations.peak_ratio(potentials_d, currents_d), 1.451, decimal=3), "max peak height incorrect for data"
    return
