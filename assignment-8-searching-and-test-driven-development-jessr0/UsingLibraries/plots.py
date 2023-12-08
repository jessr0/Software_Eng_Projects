import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def grab_data():
    filepath = 'merged_agro_gdp.tsv'
    try:
        df_m = pd.read_csv(filepath, sep='\t')
        print("File loaded successfully")
        return df_m
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"File {filepath} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"File {filepath} is not in TSV format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


df_m = grab_data()


def subset_data_by_country(df_m):
    mex_df = df_m[df_m['Country'] == 'Mexico']
    can_df = df_m[df_m['Country'] == 'Canada']
    gua_df = df_m[df_m['Country'] == 'Guatemala']
    usa_df = df_m[df_m['Country'] == 'United States of America']

    return mex_df, can_df, gua_df, usa_df


mex_df, can_df, gua_df, usa_df = subset_data_by_country(df_m)


def make_multiplot_figure(mex_df, can_df, gua_df, usa_df):

    fig, axes = plt.subplots(2, 2,
                             width_ratios=[1, 1],
                             height_ratios=[2, 2])
    fig.set_size_inches(10, 10)

    # top left plot
    axes[0, 0].plot(mex_df['Year'],
                    mex_df['Average Temperature °C'],
                    label='Mexico')
    axes[0, 0].plot(can_df['Year'],
                    can_df['Average Temperature °C'],
                    label='Canada')
    axes[0, 0].plot(gua_df['Year'],
                    gua_df['Average Temperature °C'],
                    label='Guatemala')
    axes[0, 0].plot(usa_df['Year'],
                    usa_df['Average Temperature °C'],
                    label='United States of America')
    axes[0, 0].set_title('A', loc='left')
    axes[0, 0].spines[['right', 'top']].set_visible(False)
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Average Temperature Change °C')
    axes[0, 0].legend(loc='upper left', fontsize='6')

    # top right plot
    axes[0, 1].scatter(mex_df['Year'],
                       mex_df['total_emission'],
                       label='Mexico')
    axes[0, 1].scatter(can_df['Year'],
                       can_df['total_emission'],
                       label='Canada')
    axes[0, 1].scatter(gua_df['Year'],
                       gua_df['total_emission'],
                       label='Guatemala')
    axes[0, 1].scatter(usa_df['Year'],
                       usa_df['total_emission'],
                       label='United States of America')
    axes[0, 1].set_title('B', loc='left')
    axes[0, 1].spines[['right', 'top']].set_visible(False)
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Total Emissions')
    axes[0, 1].legend(loc='upper left', fontsize='6')

    # bottom left plot

    years_combined = pd.concat([mex_df['Year'],
                                can_df['Year'],
                                gua_df['Year'],
                                usa_df['Year']])

    # Create a colormap based on the combined 'Year' data
    colormap = plt.cm.viridis

    # Normalize the year data to the colormap
    norm = plt.Normalize(years_combined.min(), years_combined.max())

    scatters = []
    scatters.append(axes[1, 0].scatter(mex_df['GDP'],
                                       mex_df['total_emission'],
                                       c=colormap(norm(mex_df['Year'].values)),
                                       label='Mexico'))
    scatters.append(axes[1, 0].scatter(can_df['GDP'],
                                       can_df['total_emission'],
                                       c=colormap(norm(can_df['Year'].values)),
                                       label='Canada'))
    scatters.append(axes[1, 0].scatter(gua_df['GDP'],
                                       gua_df['total_emission'],
                                       c=colormap(norm(gua_df['Year'].values)),
                                       label='Guatemala'))
    scatters.append(axes[1, 0].scatter(usa_df['GDP'],
                                       usa_df['total_emission'],
                                       c=colormap(norm(usa_df['Year'].values)),
                                       label='United States of America'))

    # Set other properties of the plot
    axes[1, 0].set_title('C', loc='left')
    axes[1, 0].spines[['right', 'top']].set_visible(False)
    axes[1, 0].set_xlabel('GDP')
    axes[1, 0].set_ylabel('Total Emissions')

    # Create a colorbar with the combined scatter
    cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm,
                        cmap=colormap),
                        ax=axes[1, 0])
    cbar.set_label('Year')

    # bottom right plot
    axes[1, 1].plot(mex_df['Year'],
                    mex_df['Forestland'],
                    label='Mexico')
    axes[1, 1].plot(can_df['Year'],
                    can_df['Forestland'],
                    label='Canada')
    axes[1, 1].plot(gua_df['Year'],
                    gua_df['Forestland'],
                    label='Guatemala')
    axes[1, 1].plot(usa_df['Year'],
                    usa_df['Forestland'],
                    label='United States of America')
    axes[1, 1].set_title('D', loc='left')
    axes[1, 1].spines[['right', 'top']].set_visible(False)
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Forests')
    axes[1, 1].legend(loc='upper left', fontsize='5')

    plt.savefig('Figure_1.png', dpi=300)
    plt.tight_layout()
    plt.show()


make_multiplot_figure(mex_df, can_df, gua_df, usa_df)
