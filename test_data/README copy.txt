Dataset: A 24-hour dynamic population distribution dataset based on mobile phone data from Helsinki Metropolitan Area, Finland
===============================================================================================================================

Authors: Claudia Bergroth, Olle Järv, Henrikki Tenkanen, Matti Manninen & Tuuli Toivonen

In this dataset, we present temporally dynamic population distribution data from the Helsinki Metropolitan Area, Finland, at the level of 250 m by 250 m statistical grid cells. Three hourly population distribution datasets were provided for regular workdays (Mon – Thu), Saturdays and Sundays. The data were based on aggregated mobile phone data collected by the biggest mobile network operator in Finland. Mobile phone data are assigned to statistical grid cells using an advanced dasymetric interpolation method based on ancillary data about land cover, buildings and a time use survey. The data were validated by comparing population register data from Statistics Finland for night-time hours and a daytime workplace registry. The resulting 24-hour population data can be used to reveal the temporal dynamics of the city and examine population variations relevant to for instance spatial accessibility analyses, crisis management and planning. 


Organization of data
--------------------

The dataset is stored as a single Zipfile *Helsinki_dynpop_matrix.zip* which contains following files:

1. *HMA_Dynamic_population_24H_workdays.csv* represents the dynamic population for average workday in the study area.
2. *HMA_Dynamic_population_24H_sat.csv* represents the dynamic population for average saturday in the study area.
3. *HMA_Dynamic_population_24H_sun.csv* represents the dynamic population for average sunday in the study area.
4. *target_zones_grid250m_EPSG3067.geojson* represents the statistical grid in ETRS89/ETRS-TM35FIN projection that can be used to visualize the data on a map using e.g. QGIS.


Column names
~~~~~~~~~~~~

 - `YKR_ID` : a unique identifier for each statistical grid cell (n=13,231). The identifier is compatible with the statistical YKR grid cell data by Statistics Finland and Finnish Environment Institute. 

 - `H0, H1 ... H23` : Each field represents the proportional distribution of the total population in the study area between grid cells during a one-hour period. In total, 24 fields are formatted as “Hx”, where x stands for the hour of the day (values ranging from 0-23). For example, H0 stands for the first hour of the day: 00:00 - 00:59. The sum of all cell values for each field equals to 100 (i.e. 100% of total population for each one-hour period).

In order to visualize the data on a map, the result tables can be joined with the *target_zones_grid250m_EPSG3067.geojson* data. The data can be joined by using the field ‘YKR_ID’ as a common key between the datasets.


License
-------

Creative Commons Attribution 4.0 International.


Related datasets
----------------

Tenkanen, Henrikki, & Toivonen, Tuuli. (2019). Helsinki Region Travel Time Matrix [Data set]. Zenodo. http://doi.org/10.5281/zenodo.3247564
