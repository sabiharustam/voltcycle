# Voltcycle  <img align="center" src="images/Logo.png" width="150"> 
## Package for Cyclic Voltammetry Visualization and Analysis
This package can be used to take cyclic voltammetry data, clean and plot the data, find and fit peaks to obtain peak locations. It also creates baseline and based on peak location, calculates the peak current and voltage. Finally use those descriptors to classify a battery material as either electrochemically reversable or not, also to determine if it is anolyte or catholyte. Additionally, there is a GUI based visualization app that can be used to upload the users data, choose the plotting style and color. This package could be expanded upon to be able to handle different formats of data. For a more specific overview of the project, please see the usecase under docs. 

### Software Dependencies 
- Python3 
- For python packages see requirements.txt

## Organization of the project
``` 
Rawdata/
Voltcycle/ 
    Trialcodes/
        testdata/
        README.md
        __init__.py
        cv_trial.py
        file_read.py
				test.txt
				trial.ipynb
    __init__.py
    FINAL.py 
    PLOT.py
    GUI.py 
    README.md
docs/ 
    Technology_review.pptx
    over_view.md
    usecases.md
LICENSE
README.md
requirements.txt(FOR DEPENDENCIES)
setup.py(if we have final installable)
```
