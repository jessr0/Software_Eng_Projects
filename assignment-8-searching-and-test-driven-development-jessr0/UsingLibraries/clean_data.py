import pandas as pd


def destroy_commas(x):
    if x is None:
        return None
    return float(x.replace(',', ''))


def load_data():
    df_A = pd.read_csv('../data/Agrofood_co2_emission.csv', sep=',')
    df_G = pd.read_csv('../data/IMF_GDP.csv', sep=',')

    df_G = df_G.replace('...', None)
    df_G = df_G.replace('-', None)
    df_G['Country'] = df_G['Country'].replace(
                                 'United States', 'United States of America')

    for col in df_G.columns:
        if col == 'Country':
            continue
        df_G[col] = df_G[col].apply(destroy_commas)

    return df_A, df_G


df_A, df_G = load_data()


def clean_and_melt_gdp(df_G):
    # Clean the DataFrame
    df_G_clean = df_G.copy()

    # Melting the GDP DataFrame
    df_G_melted = df_G_clean.melt(id_vars=['Country'],
                                  var_name='Year',
                                  value_name='GDP')

    # Convert year to integer for merging
    df_G_melted['Year'] = df_G_melted['Year'].astype(int)

    return df_G_melted


# Clean and melt the GDP data
df_G_melted = clean_and_melt_gdp(df_G)


def merge_gdp_and_agro(df_A, df_G_melted):
    # Rename the 'Area' column to 'Country' for a consistent merge
    df_A.rename(columns={'Area': 'Country'}, inplace=True)
    # Convert 'Year' in emissions to int if it's not already
    df_A['Year'] = df_A['Year'].astype(int)

    # Merge the emissions and GDP data on 'Country' and 'Year'
    merged_df = pd.merge(df_A,
                         df_G_melted,
                         on=['Country', 'Year'],
                         how='inner')

    return merged_df


# Merge the emissions and GDP data
merged_df = merge_gdp_and_agro(df_A, df_G_melted)


merged_df.to_csv('merged_agro_gdp.tsv', sep='\t', index=False)
