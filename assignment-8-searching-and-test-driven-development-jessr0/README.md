[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WSoIsN1S)
# tdd_searching
Searching with Test Driven Development

Version 1.0

I was curious about the relationship between total fire and GDP in different countries across all years listed. To acquire this, I used fires_gdp.py to search Agrofood_co2_emissions.csv and IMF_GDP.csv by country, indexed by year. This is performed by get_fire.py, which can be ran manually in the src directory using the following prompt:

wget -P ../data/ Agrofood_co2_emission.csv  "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"
wget -P ../data/ IMF_GDP.csv  "https://docs.google.com/uc?export=download&id=1tuoQ9UTW_XRKgBOBaTLtGXh8h0ytKvFp"

python get_fire.py \
    ../data/Agrofood_co2_emission.csv Year "Savanna fires" "Forest fires" \
    ../data/IMF_GDP.csv \
    [country] \
    [country]_fire_gdp.txt 

or automatically by running the snakefile found in the workflows directory, like so:

snakemake -c1

The snakefile will produce outputs in the workflows directory, while running the command manually will do so in the src directory. Following the production of .txt files, scatter.py is used to plot fires against GDP for each year in the datasets. scatter.py can be run manually from the src directory using the following prompt:

python scatter.py country_fire_gdp.txt country_fire_gdp.png Country Fires GDP

or by running the snakefile using the prompt displayed above (Countries and be changed by altering the COUNTRY variable within the snakefile).

I looked at data from three countries: Albania, Zimbabwe, and Angola using the methods listed above. In Albania, the number of fires is low overall, regardless of yearly GDP. This is likely a function of Albania's climate, which may receive sufficient rainfall to suppress both savanna and forest fires. In Zimbabwe, GDP is consistenly very low, and the number of fires is quite high. The amount of fires in this country may be a side effect of its low GDP, but this is impossible to conclude without additional information. In Angola, there is minimal correlation between fires and GDP, and a high amount of variation between datapoints. Copies of all plots can be found in the Figures folder.

This data seeks to provide information about wildfires in relation to a country's GDP, presumably to draw conclusions about international CO2 emissions on a country to country basis. While informative, more information is needed to draw major conclusions.

Version 2.0

The previous version used searching and indexing functions to to query Agrofood_co2_emissions.csv and IMF_GDP.csv for information indexed by year. This version performs an identical role, but does so through the use of a hash table. The hash table and corresponding functions are contained in fire_gdp.py in the src directory. Each column header functions as the key in the table, while value in each dataset is assigned a value. Values are assigned using a prime number multiplier of 31 and an addition of 7. This helps to ensure that all values are unique and nonzero, and that collisions are minimized. The other functions in fire_gdp.py have been altered to use this table. 

The original purpose of these scripts were to produce meaningful data visualizations about the relaationship between fires and GDP by year for three countries: Albania, Zimbabwe, and Angola. The updated hash table structure identically replicates these visualizations (see figures_fromsearch folder for reference to data from previous method), suggesting that this data structure functions identically to the search/index structure used in version 1.0. Copies of these figures can be found here. 

As before these scripts can be run manually, or using the snakefile that is now found in the main directory. Instructions for manual use are identical to those in version 1.0, while the snakefile can be run from the main directory using the command snakemake -c1. 
