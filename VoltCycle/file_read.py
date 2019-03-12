import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import rcParams

def read_cycle(data):
    """This function reads a segment of datafile (corresponding a cycle)
    and generates a dataframe with columns 'Potential' and 'Current'

    Parameters
    __________
    data: segment of data file

    Returns
    _______
    A dataframe with potential and current columns  
    """     

    current = []
    potential = []
    for i in data[3:]:
        current.append(float(i.split("\t")[4]))
        potential.append(float(i.split("\t")[3]))
    zippedList = list(zip(potential, current))
    df = pd.DataFrame(zippedList, columns = ['Potential' , 'Current'])
    return df


def read_file(file):
    """This function reads the raw data file, gets the scanrate and stepsize
    and then reads the lines according to cycle number. Once it reads the data
    for one cycle, it calls read_cycle function to denerate a dataframe. It 
    does the same thing for all the cycles and finally returns a dictionary,
    the keys of which are the cycle numbers and the values are the 
    corresponding dataframes.

    Parameters
    __________
    file: raw data file

    Returns:
    ________
    dict_of_df: dictionary of dataframes with keys = cycle numbers and
    values = dataframes for each cycle
    n_cycle: number of cycles in the raw file  
    """   
    dict_of_df = {} 
    h = 0
    l = 0
    n_cycle = 0
    #a = []
    with open(file, 'rt') as f:
        print(file + ' Opened')
        for line in f:
            record = 0
            if not (h and l):
                if line.startswith('SCANRATE'):
                    scan_rate = float(line.split()[2])
                    h = 1
                if line.startswith('STEPSIZE'):
                    step_size = float(line.split()[2])
                    l = 1
            if line.startswith('CURVE'):
                n_cycle += 1
                if n_cycle > 1:
                    number = n_cycle - 1
                    df = read_cycle(a)
                    key_name = 'cycle_' + str(number)
                    #key_name = number
                    dict_of_df[key_name] = copy.deepcopy(df)
                a = []
            if n_cycle:
                a.append(line)
    return dict_of_df, number


#df = pd.DataFrame(list(dict1['df_1'].items()))
#list1, list2 = list(dict1['df_1'].items())
#list1, list2 = list(dict1.get('df_'+str(1)))

def data_frame(dict_cycle, n):
    """Reads the dictionary of dataframes and returns dataframes for each cycle

    Parameters
    __________
    dict_cycle: Dictionary of dataframes
    n: cycle number

    Returns:
    _______
    Dataframe correcponding to the cycle number 
    """
    list1, list2 = (list(dict_cycle.get('cycle_'+str(n)).items()))
    zippedList = list(zip(list1[1], list2[1]))
    data  = pd.DataFrame(zippedList, columns = ['Potential' , 'Current'])
    return data
    

def plot_fig(dict_cycle, n):
    """For basic plotting of the cycle data
  
    Parameters
    __________
    dict: dictionary of dataframes for all the cycles
    n: number of cycles

    Saves the plot in a file called cycle.png 
    """

    for i in range(n):
        print(i+1)
        df = data_frame(dict_cycle, i+1)
        plt.plot(df.Potential, df.Current, label = "Cycle{}".format(i+1))
        
    print(df.head())
    plt.xlabel('Voltage')
    plt.ylabel('Current')
    plt.legend()
    plt.savefig('cycle.png')
    print('executed')


#dict_cycle, n_cycle  = read_file('test.txt')
#rcParams.update({'figure.autolayout': True})
#plot(dict_cycle, n_cycle)
