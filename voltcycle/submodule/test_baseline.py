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
    Test if the index exist in original input.
    
    """