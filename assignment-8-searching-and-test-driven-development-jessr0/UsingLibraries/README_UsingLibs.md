Version 6.0

Climate change is real but Uncle John doesn't believe us. To remedy this, I created a four panel plot (see UsingLbraries/data) that clearly visualizes emissions data from the United States, Canada, Mexico, and Guatemala.

<img width="890" alt="HW_9_Figure_1" src="https://github.com/cu-swe4s-fall-2023/assignment-8-searching-and-test-driven-development-jessr0/assets/108949769/c47cf9cf-d86c-462b-a1b0-21926bf2b825">


In Figure 1A, we see that the yearly average temperature change has increased for all countries between 1990-2020, suggesting a gradually warming climate.

Figure 1B shows that total emissions for all countries but Guatemala have also increased between 1990-2020. This suggests that there may be correlation between emissions and temperature increases, but this cannot be definitively concluded without supplemental data.

Figure 1C shows the relationship between total emissions and the GDP of each nation colorcoded by year.
While not divided by country, the overall skew of the data suggests that total emissions are positively correlated with GDP between 1990 and 2020. 

Figure 1D displays the relationship between change in forestland over time per country. Overall, the change in amount of forested land in all countries has either stayed consistent or decreased in the last decade. (Though the rate of deforestation in the United States has technically decreased, it is still a net negative.) Since forests play a mjor role in the removal of greenhouse gases from the atmoshphere, this correlates well with the data displayed in plots 1A-C. 

Overall these plots provide compelling evidence for climate change and associated phenomena in North America. Additional information that would support this assertion would be data about total population and vehicle ownership per year from each country, as car exhaust likely plays a major role in total emissions. 

Figure 1 can be produced by running the snakemake file found in UsingLibraries, like so:

snakemake -c1

This will produce a .tsv file that contains a merged form of Agrofood_co2_emissions.csv and IMF_GDP.csv called merged_agro_gdp.tsv. These files can be found in the data file of the repo or can be downloaded using the information found in the README.md in the assignment-8 repo. This snakemake file also produces Figure 1.png, which contains Figures 1A-1D as described above.

Functional tests for these figures are included in the previous versions functional test folder, found in the maindirectory's test folder in file test_get_fire.sh to make CI/CD more efficient. Unit tests for clean_data.py are found in test_clean_data.py in the UsingLibraries folder. 
