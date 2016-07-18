# Fieldkites

A research project exploring the relationship between seasonal water use and crop yield,
acknowledging the temporal distribution of water use throughout the growing season.

To use this repository such that it requires the least number of modifications, please install Aquacrop and the Plug-in in the C directory:

C:\FAO\AquaCrop
C:\FAO\ACsaV50

In the current version, all the files that are spatially-specific, are a within the location's directory in DATA:
For example, for cell 435: C:\FAO\AquaCrop\DATA\435
In here, I have the .CRO and .SOL files, along with the .ETO, .PLU, .TMP, .CLI, .SW0 daily for the years 1950-2010.
I have also copied the appropriate .CO2 file into each location's DATA subdirectory.

At this time then, you must populate the DATA folder with subdirectories for each location of interest, and with each subdirectory the appropriate folders.

I have found it beneficial to create year-specific files from these multi-year files, and have created the generate_CLI program to facilitate this.
This may be unnecessary, but for now I feel it is appropriate.
If all the folders and subdirectories are prepared as noted, then the generation of these year-specific files will happen autmoatically when running master.
