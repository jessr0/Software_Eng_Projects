test - e ssshtest || wget - q https: // raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_all_args python3 src/get_fire.py data/Agrofood_co2_emission.csv Year 'Savanna fires' 'Forest fires' \
   data/IMF_GDP.csv \
   Albania \
   src/Albania_fire_gdp.txt
assert_no_stderr    
assert_exit_code 0

run test_missing_args python3 src/get_fire.py data/Agrofood_co2_emission.csv Year 'Savanna fires' 'Forest fires' \
   data/IMF_GDP.csv \
   src/Albania_fire_gdp.txt
assert_stderr
assert_no_stdout
assert_exit_code 1

run test_albania_output python3 src/scatter.py src/Albania_fire_gdp.txt Albania_fire_gdp.png Albania Fires GDP
assert_equal $file_name $( ls $Albania_fire_gdp.png )
assert_no_stderr
assert_exit_code 0

run test_zimbabwe_output python3 src/scatter.py src/Zimbabwe_fire_gdp.txt Zimbabwe_fire_gdp.png Zimbabwe Fires GDP
assert_equal $file_name $( ls $Zimbabwe_fire_gdp.png )
assert_no_stderr
assert_exit_code 0

run test_angola_output python3 src/scatter.py src/Angola_fire_gdp.txt Angola_fire_gdp.png Angola Fires GDP
assert_equal $file_name $( ls $Angola_fire_gdp.png )
assert_no_stderr
assert_exit_code 0
