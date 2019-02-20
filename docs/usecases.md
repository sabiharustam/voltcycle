 This is to put in use cases for cyclic voltammetry project.

1.	Input your own CV data, select and visualize representative 
cycles to get nice plots. Components:
•	GUI asking to load users CV data, data type from a dropdown menu 
(text, excel, other txt files), reference from a dropdown menu 
(dictionary)
•	read file into dataframe using pd.read_csv, pd.read_excel
•	Check for empty cells and replace with average of previous and 
next value + send a warning
•	Manipulation in shifting the data (to measure with reference to 
the reference)
o	Input and offset (convert to standard hydrogen electrode)
•	Return to user number of cycles found, ask which representative 
cycles to display (if it detects multiple cycles, dropdown to ask user 
how many to run).
•	plot cv data for selected cycles, show user in a nice formatted 
plot.
•	Smoothen plots

2.	Assessing reversibility in your cv data (freedom for user to 
select what peaks to look for).
Components:
•	GUI to plot data from a particular dataset (demo)
•	Interface for selecting cycle number to plot
•	Link from user inputted cycle number to appropriate plot in the 
dataset.
o	Multiple ways – input multiple datasets and chose which ones to 
plot (from that, which cycle from which particular set)
•	Find peaks
o	Function based on the number of peaks found, returns number of 
peaks
o	If more than 2 peaks, says you need to continue analysis (to 
compare peaks)
o	Find if any are pairs (therefore reversible), returns numbers of 
pairs
•	Define baselines
o	From the baseline, measure heights of the peaks (Ipa, Ipc)
o	Tangent line slope of curve (minimum prior to the peak)
o	Measure difference between peak potentials (Epa, Epc – position 
from x axis)
o	Return the halfway point (redox potential)
o	Return ratio of Ipa to Ipc (the close it is to 1, the better it 
will rank)
o	Rank ratios

3.	Output table consisting of ID and pass/fail (based on 
reversibility) and generates cv plots of reversible data.

