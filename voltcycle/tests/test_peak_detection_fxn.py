"""This module contains the function that test the
peak_detection_fxn() function. It calls the core.py
file which contains the function to be tested."""

import numpy as np
from voltcycle import core

def test_peak_detection_fxn():
    """This function tests the peak_detection_fxn() function."""
    read_file = core.read_file('../data/10mM_2,7-AQDS_1M_KOH_25mVs_0.5step_2.txt')
    file_df = core.data_frame(read_file, 2)
    y_column = file_df['Current']
    df2 = core.peak_detection_fxn(y_column)

    # check that the output is a list
    assert isinstance(df2, list)

    # check that there are two outputs
    assert (len(df2)) == 2

    # check if the outputs are integer values
    for i in range(len(df2)):
        assert isinstance(df2[i], np.int32)
