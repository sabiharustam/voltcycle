## 1. Upload, read, and plot cyclic voltammetry data.

	* Implement a GUI (using Dash) that asks users to upload CV data.
		* User uploads data in the form of a .txt file, or some other common variation (e.g. .DTA).
		* Should have the ability to upload multiple files/datasets.
		* Data files should be displayed in some type of list.   
	* Read file(s) into a dataframe.
		* Must be able to extract only the necessary data columns from the .txt files.
		* Needs to be able to distinguish between multiple cycles in the same file.
		* Check for empty cells and replace with average of previous and next value + send a warning.
	* User should be able to select data/cycles to plot and/or run through data analysis.
		* Multiple plots should be able to be shown in an organized and visually pleasing manor.
		* Options within the GUI for plot colors, markers, ticks, etc.      
	* User can choose to offset the potential scale based on the reference electrode used.
		* This is either done through a drop down menu of reference electrodes or manual setting.

## 2. Analysis of CV data 

	* Find all peaks in the CV curve.
	* Assess the chemical reversibiltiy of the system.
		* If only one peak is found, the system is deemed as chemically "irreversible', and analysis does not continue.
		* If two corresponding oxidation/reduction (positive, negative) peaks are found, the system is deemed as chemically        "reversible" and analysis continues.
		* If three or more peaks are found, advises the user that more external analysis is required.
	* Assess the electrochemical reversibility of the system.
		* Find the distance between the two peak potentials (delta Ep).
		* Use the delta Ep as a performance ranking metric (shorter delta Ep = faster electron transfer).
		* Based on theoretical peak distance, 57mV/# of electrons), suggest how many electron transfers are involved.        
		* If the delta Ep is greater than 300mV, system is deemed as electrochemically "irreversible" and analysis stops.      
	* Calculate the redox potential of the system.
		* Redox potential is the half way point between the peak potentials.
		* If the redox potential is negative, classify the material as an "Anolyte".
		* If the redox Potential is positive, classify the material as a "Catholyte".
	* Calculate the ratio of the anodic(oxidation) and cathodic(reduction) peak current heights (ipA/ipC).        
		* Need to establish a baseline from which to calculate the peak heights.
		* Use the ipA/ipC as a performance metric for chemical reversiblity (ipA/ipC = 1 is ideal scenario). 

## 3. Visualization of results

	* Implement a GUI (using Dash) that displays the initial plots from part 1 along with the results of the analysis in a table. 
		* Must be able to call the results and place directly into the table, which may be challenging.
	* Table will include columns for:
		* filename 
		* CV plot 
		* Chemical reversibility (yes/no) 
		* delta Ep (return "electrochemically irreversible" if delta Ep >300mV)
		* redox potential
		* anolyte/catholyte classification
		* ipA/ipC
		* performance ranking. 
	* Possible interactive feature to see the results of the analysis directly on the CV plot.
	* Overall, visualization should be well organized and visually pleasing, so that the results could be used for possible       ML/data science techniques correlating the materials physical properties (structure, etc.) to their performance                   characteristics. 
    
   