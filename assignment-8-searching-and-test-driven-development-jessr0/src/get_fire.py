import sys
import fire_gdp

fire_file_name = sys.argv[1]

fire_year_col_name = sys.argv[2]
fire_savanna_col_name = sys.argv[3]
fire_forest_col_name = sys.argv[4]

gdp_file_name = sys.argv[5]

country = sys.argv[6]

out_file = sys.argv[7]

data = fire_gdp.get_fire_gdp_year_data(fire_file_name,
                                       gdp_file_name,
                                       country,
                                       fire_year_col_name,
                                       fire_savanna_col_name,
                                       fire_forest_col_name)

fires = data[0]
gdps = data[1]

with open(out_file, 'w') as file:
    for i in range(len(fires)):
        file.write('\t'.join([str(fires[i]), str(gdps[i])]) + '\n')
