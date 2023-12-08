import unittest
from UsingLibraries import clean_data
import pandas as pd


class Testcleandata(unittest.TestCase):

    def test_destroy_commas(self):
        self.assertEqual(clean_data.destroy_commas('1,234'), 1234.0)
        self.assertEqual(clean_data.destroy_commas('1234'), 1234.0)
        self.assertEqual(clean_data.destroy_commas('1234.56'), 1234.56)
        self.assertIsNone(clean_data.destroy_commas(None))
        self.assertRaises(ValueError, clean_data.destroy_commas, '')

    def test_load_data(self):
        df_A, df_G = clean_data.load_data()
        self.assertIsNotNone(df_A)
        self.assertIsNotNone(df_G)
        self.assertFalse(df_A.empty)
        self.assertFalse(df_G.empty)

        self.assertIn('United States of America', df_G['Country'].values)

        for col in df_G.columns:
            if col == 'Country':
                continue

            def is_float_or_none(x):
                return isinstance(x, float) or x is None
            all_values_are_correct = df_G[col].apply(is_float_or_none).all()

            self.assertTrue(all_values_are_correct)

    def setUp(self):
        # Create sample data that resembles actual data
        self.sample_gdp_data = {
            'Country': ['A', 'B'],
            '2000': ['100', '200'],
            '2001': ['150', '250']
        }
        self.sample_agro_data = {
            'Area': ['A', 'B'],
            'Year': [2000, 2001],
            'Emission': [10, 20]
        }
        self.df_G = pd.DataFrame(self.sample_gdp_data)
        self.df_A = pd.DataFrame(self.sample_agro_data)

    # check if df melts as expected
    def test_clean_and_melt_gdp(self):
        melted = clean_data.clean_and_melt_gdp(self.df_G)
        self.assertEqual(melted.shape, (4, 3))
        self.assertListEqual(list(melted.columns), ['Country', 'Year', 'GDP'])

    # check if merged dataframes look as expected
    def test_merge_gdp_and_agro(self):
        df_G_melted = clean_data.clean_and_melt_gdp(self.df_G)
        merged = clean_data.merge_gdp_and_agro(self.df_A, df_G_melted)
        self.assertEqual(merged.shape, (2, 4))
        self.assertListEqual(list(merged.columns),
                             ['Country', 'Year', 'Emission', 'GDP'])
        self.assertEqual(merged.iloc[0]['GDP'], '100')
        self.assertEqual(merged.iloc[1]['GDP'], '250')
