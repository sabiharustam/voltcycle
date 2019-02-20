 This is to put in use cases for cyclic voltammetry project.

## 1. Input your own cyclic voltammetry (CV) data, select, and visualize user specified datasets 

	* GUI asks users to load CV data
		* User selects data type from a dropdown menu (text, excel, other txt files),
		* User selects reference electrode from a dropdown menu (dictionary)
	* Read file into dataframe using pd.read_csv, pd.read_excel
	* Check for empty cells and replace with average of previous and next value + send a warning
	* User can choose to offset data with different reference electrode, input new reference
	* Data is adjusted to reflect new reference electrode
	* Data files can be for one cycle for one system/compound but they could also be multiple cycles for one
	 system. The program either needs to detect this and display a number of cycles found, or the user needs
	 specify this for the program. 
	* Data files should be displayed in some type of list
	* User should be able to select data to plot and/or run through data analysis
	* plot CV data for selected cycles/files

## 2. Assessing reversibility in your CV data (with freedom for user to select what peaks to look for/override automation)

	* GUI to plot data from a particular dataset(for demo)
	* Smoothen plots
	* Find Peaks
		* If 2 or more peaks, continue. A pair of peaks indicates a reversible reaction (needed for battery)
		* If 3 or more, ask for user to select peaks for analysis
	* Define baselines
		* This function may be based on tangents of curve near the recognized peaks
	* From the baseline, measure heights of peaks (Ipa, Ipc, current)
	* Measure difference between peak potentials (Epa, Epc, voltage)
	* Return the halfway point (E1/2, redox potential)
	* Return ratio of Ipa to Ipc (the closer it is to 1, the higher the material will rank)
	* Rank ratios, and/or produce a score we define based on these parameters and rank by this score

## 3. Return results of analysis/visualize

	* Output a table with ID, reversibility parameters, and some type of pass/fail score
	* Maybe data table is color-coded with red, yellow, green to see higher scores vs failing easily 
	* User should have option to see plots at this point too. Maybe click on ID in table to see plot
