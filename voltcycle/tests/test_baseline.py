"""This module tests the baseline function."""
# import functions and modules
import numpy as np
import file_read
import baseline

#Test functions:
def test_split():
    """
    This function tests the split function.
    The output of the function has to be np.array.
    Split function splits the length of input vector
    in two. So, len of output should equal to half len
    of input.
    """
    dict_1 = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    data = file_read.data_frame(dict_1, 1)
    vec_x = data.Potential
    a_val, b_val = baseline.split(vec_x)
    assert isinstance(a_val == np.ndarray), "The output type is incorrect."
    assert isinstance(b_val == np.ndarray), "The output type is incorrect."
    #assert len(a)  int(len(x)/2), "The output should be "
    (np.testing.assert_almost_equal(len(a_val), (len(vec_x)/2), decimal=0),
     "Output length is incorrect")
    (np.testing.assert_almost_equal(len(b_val), (len(vec_x)/2), decimal=0),
     "Output length is incorrect")
    return "Test of split function passed!"


def test_critical_idx():
    """
    Critical_idx returns idx of the index of the intercepts of different moving average curves.
    Test the output if it is a single index.
    Test if the output is integer.
    Test if the index exist in original input.
    """
    dict_1 = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    data = file_read.data_frame(dict_1, 1)
    col_x1, col_x2 = baseline.split(data.Potential)
    col_y1, col_y2 = baseline.split(data.Current)
    idx = baseline.critical_idx(col_x1, col_y1)
    assert isinstance(idx == np.int64), ("Output should be integer, but"
                                         "Function is returning {}".format(type(idx)))
    assert idx.shape == (), "This function should return single idx"
    assert 0 < idx < len(col_x1), "Output index is out of order"
    return "Test of critical_idx function passed!"


def test_sum_mean():
    """
    Target function returns the mean and sum of the given vector.
    Expect output to be a list, with length 2.
    Can also test if the mean is correctly calculated.
    """
    dict_1 = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    data = file_read.data_frame(dict_1, 1)
    col_x1, col_x2 = baseline.split(data.Potential)
    a_val = baseline.sum_mean(col_x1)
    assert isinstance(a_val == list), ("Output should be list object,"
                                       " but fuction is returning{}".format(type(a_val)))
    assert len(a_val) == 2, ("length of output should be 2,"
                             "but, function is returning a list with length{}".format(len(a_val)))
    (np.testing.assert_almost_equal(a_val[1], np.mean(col_x1), decimal=3),
     "Mean is calculated incorrectly")
    return "Test of sum_mean function passed!"

def test_multiplica():
    """
    Target function returns the sum of the multilica of two given vector.
    Expect output as np.float object.
    """
    dict_1 = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    data = file_read.data_frame(dict_1, 1)
    col_x1, col_x2 = baseline.split(data.Potential)
    col_y1, col_y2 = baseline.split(data.Current)
    a_val = baseline.multiplica(col_x1, col_y1)
    assert isinstance(a_val == np.float64), ("Output should be float object,"
                                             " but fuction is returning{}".format(type(a_val)))
    b_val = np.multiply(col_x1, col_y1).sum()
    (np.testing.assert_almost_equal(a_val, b_val, decimal=3),
     "Calculation is incorrect")
    return "Test Passed for multiplica function!"


def test_linear_coeff():
    """
    Target function returns the inclination coeffecient
    and y axis interception coeffecient m and b.
    T
    """
    x_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    m_val, b_val = baseline.linear_coeff(x_arr, y_arr)
    assert m_val == 1, "Inclination coeffecient is incorrect"
    assert b_val == 0, "Interception is incorrect"
    return "Test passed for linear_coeff function!"

def test_y_fitted_line():
    """
    Target function returns the fitted baseline y.
    Should exam if the output is correct shape,
    correct type, and correct value.
    """
    x_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    m_val = 1
    b_val = 0
    y_val = baseline.y_fitted_line(m_val, b_val, x_arr)
    if len(y_val) != len(x_arr):
        raise ValueError("Output must have same length as input x,"
                         "but have lenth {}".format(len(y_val)))
    assert isinstance(y_val == list), "Output should be list object"
    if np.all(y_val != x_arr):
        raise ValueError("Fitted line y values are calculated incorrectly")
    return "Test passed for y_fitted_line function!"

def test_linear_background():
    """
    Target function is wrapping function which returns
    linear fitted line.Should exam if the output is
    correct shape, correct type, and correct value.
    """
    dict_1 = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    data = file_read.data_frame(dict_1, 1)
    col_x1, col_x2 = baseline.split(data.Potential)
    col_y1, col_y2 = baseline.split(data.Current)
    y_fit = baseline.linear_background(col_x1, col_y1)
    assert isinstance(y_fit == list), "Output should be list object"
    if len(y_fit) != len(col_x1):
        raise ValueError("Output must have same length as input x,"
                         "but have lenth {}".format(len(y_fit)))
    if len(y_fit) != len(col_y1):
        raise ValueError("Output must have same length as input y,"
                         "but have lenth {}".format(len(y_fit)))
    return "Test passed for linear_background function!"
