# import functions and modules
import file_read
import baseline
import numpy as np
import pandas as pd

#Test functions:
def test_split():
    """
    This function tests the split function.
    The output of the function has to be np.array.
    Split function splits the length of input vector
    in two. So, len of output should equal to half len
    of input.
    """
    dict_1,n_cycle = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    df = file_read.data_frame(dict_1, 1)
    x = df.Potential
    a,b = baseline.split(x)
    assert type(a) == np.ndarray, "The output type is incorrect."
    assert type(b) == np.ndarray, "The output type is incorrect."
    #assert len(a)  int(len(x)/2), "The output should be "
    np.testing.assert_almost_equal(len(a),(len(x)/2), decimal=0), "Output length is incorrect"
    np.testing.assert_almost_equal(len(b),(len(x)/2), decimal=0), "Output length is incorrect"
    return "Test of split function passed!"


def test_critical_idx():
    """
    Critical_idx returns idx of the index of the intercepts of different moving average curves.
    Test the output if it is a single index.
    Test if the output is integer.
    Test if the index exist in original input.
    """
    dict_1,n_cycle = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    df = file_read.data_frame(dict_1, 1)
    x1,x2 = baseline.split(df.Potential)
    y1,y2 = baseline.split(df.Current)
    idx = baseline.critical_idx(x1,y1)
    assert type(idx) == np.int64, ("Output should be integer, but"
                                   "Function is returning {}".format(type(idx)))
    assert idx.shape == (), "This function should return single idx"
    assert 0 < idx <len(x1), "Output index is out of order"
    return "Test of critical_idx function passed!"


def test_sum_mean():
    """
    Target function returns the mean and sum of the given vector.
    Expect output to be a list, with length 2.
    Can also test if the mean is correctly calculated.
    """
    dict_1,n_cycle = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    df = file_read.data_frame(dict_1, 1)
    x1,x2 = baseline.split(df.Potential)
    y1,y2 = baseline.split(df.Current)
    a = baseline.sum_mean(x1)
    assert type(a) == list, ("Output should be list object,"
                                                " but fuction is returning{}".format(type(a)))
    assert len(a) == 2, ("length of output should be 2,"
                        "but, function is returning a list with length{}".format(len(a)))
    np.testing.assert_almost_equal(a[1],np.mean(x1), decimal=3), "Mean is calculated incorrectly"
    return "Test of sum_mean function passed!"

def test_multiplica():
    """
    Target function returns the sum of the multilica of two given vector.
    Expect output as np.float object.
    """
    dict_1,n_cycle = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    df = file_read.data_frame(dict_1, 1)
    x1,x2 = baseline.split(df.Potential)
    y1,y2 = baseline.split(df.Current)
    a = baseline.multiplica(x1,y1)
    assert type(a) == np.float64, ("Output should be float object,"
                                   " but fuction is returning{}".format(type(a)))
    b = np.multiply(x1,y1).sum()
    (np.testing.assert_almost_equal(a,b, decimal=3),
     "Calculation is incorrect")
    return "Test Passed for multiplica function!"


def test_linear_coeff():
    """
    Target function returns the inclination coeffecient
    and y axis interception coeffecient m and b.
    T
    """
    x = np.array([1,2,3,4,5,6,7,8,9])
    y = np.array([1,2,3,4,5,6,7,8,9])
    m,b = baseline.linear_coeff(x,y)
    assert m == 1, "Inclination coeffecient is incorrect"
    assert b == 0, "Interception is incorrect"
    return "Test passed for linear_coeff function!"

def test_y_fitted_line():
    """
    Target function returns the fitted baseline y.
    Should exam if the output is correct shape,
    correct type, and correct value.
    """
    x = np.array([1,2,3,4,5,6,7,8,9])
    m = 1
    b = 0
    y = baseline.y_fitted_line(m,b,x)
    if len(y) != len(x):
        raise ValueError("Output must have same length as input x,"
                         "but have lenth {}".format(len(y)))
    assert type(y) == list, "Output should be list object"
    if np.all(y != x):
        raise ValueError("Fitted line y values are calculated incorrectly")
    return "Test passed for y_fitted_line function!"

def test_linear_background():
    """
    Target function is wrapping function which returns
    linear fitted line.Should exam if the output is
    correct shape, correct type, and correct value.
    """
    dict_1,n_cycle = file_read.read_file('../../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    df = file_read.data_frame(dict_1, 1)
    x1,x2 = baseline.split(df.Potential)
    y1,y2 = baseline.split(df.Current)
    y_fit = baseline.linear_background(x1,y1)
    assert type(y_fit) == list, "Output should be list object"
    if len(y_fit) != len(x1):
        raise ValueError("Output must have same length as input x,"
                         "but have lenth {}".format(len(y_fit)))
    if len(y_fit) != len(y1):
        raise ValueError("Output must have same length as input y,"
                         "but have lenth {}".format(len(y_fit))) 
    return "Test passed for linear_background function!"