import unittest
import sys
sys.path.append('../src')
import fire_gdp
from fire_gdp import HashTable
import random

class TestFiregdp(unittest.TestCase):

    def test_remove_commas(self):
        self.assertEqual(fire_gdp.remove_commas('2,000'), '2000')
        self.assertEqual(fire_gdp.remove_commas('2,000,000'), '2000000')

    def test_get_data_open_file(self):
        fire_file_name = '../data/Agrofood_co2_emission.csv'
        gdp_file_name = '../data/IMF_GDP.csv'
        dne_file_name = '../data/none.txt'
        empty_file_name = '../data/empty.txt'
        self.assertEqual(fire_gdp.get_data(empty_file_name), [])
        self.assertRaises(FileNotFoundError, fire_gdp.get_data, dne_file_name)

    def test_get_data_query_lines(self):
        fire_file_name = '../data/Agrofood_co2_emission.csv'
        gdp_file_name = '../data/IMF_GDP.csv'

        target_country = 'Albania'
        column_name_fire = 'Area'
        column_name_gdp = '\ufeffCountry'
        fake_column = 'notrealcol'

        data_country = fire_gdp.get_data(fire_file_name, query_value=target_country, query_column=column_name_fire)
        data_length = len(data_country)
        self.assertEqual(data_length, 31)
        for row_hash_table in data_country:
            self.assertEqual(row_hash_table.retrieve('Area'), target_country)

        # Test with the gdp_file_name
        gdp_data = fire_gdp.get_data(gdp_file_name, query_value=target_country, query_column=column_name_gdp)
        self.assertEqual(len(gdp_data), 1)
        self.assertEqual(gdp_data[0].retrieve('\ufeffCountry'), target_country)

        # Test with an empty file

        empty_file_name = '../data/empty.txt'
        data_country_empty = fire_gdp.get_data(empty_file_name, query_value=target_country, query_column=fake_column)
        data_length_empty = len(data_country_empty)
        self.assertEqual(data_length_empty, 0)

        # Test for querying a non-existent column name
        self.assertRaises(KeyError,
                      fire_gdp.get_data,
                      fire_file_name,
                      query_value=target_country,
                      query_column=fake_column)

    def test_get_fire_gdp_year_data(self):
        fire_file_name = '../data/Agrofood_co2_emission.csv'
        gdp_file_name = '../data/IMF_GDP.csv'


        country = 'Zimbabwe'
        fire_year_col_name = 'Year'
        fire_savanna_col_name = 'Savanna fires'
        fire_forest_col_name = 'Forest fires'
        
        data = fire_gdp.get_fire_gdp_year_data(fire_file_name,
                                           gdp_file_name,
                                           country,
                                           fire_year_col_name,
                                           fire_savanna_col_name,
                                           fire_forest_col_name)

        fire = data[0]
        gdp = data[1]
        year = data[2]

        self.assertEqual(2043.3344 + 185.0667, fire[0])
        self.assertEqual(10144.00, gdp[0])
        self.assertEqual(1990, year[0])

    def test_insert_and_retrieve(self):
        ht = HashTable()
        ht.insert("key1", "value1")
        assert ht.retrieve("key1") == "value1"

    def test_collision_handling(self):
        ht = HashTable()
        # Insert two keys that would lead to a collision
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")  # Assuming key1 and key2 hash to the same index
        assert ht.retrieve("key2") == "value2"

    def test_nonexistent_key(self):
        ht = HashTable()
        assert ht.retrieve("nonexistent") is None

if __name__ == '__main__':
    unittest.main()
