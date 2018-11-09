import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import folium

#directory of excel file being used
dir = 'C:/Users/MitchTallman/Desktop/Python Tutorials/'

#reading in the excel file
df_can = pd.read_excel(
    dir+'Canada.xlsx',
    sheet_name = 'Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
  
#creating list of years with loops  
year = 1980
length = (2013 - 1980) + 1
year_list = []
while len(year_list) < length:
    year_list.append(year)
    year = year + 1
    
#creating list of years more simply
years = list(map(int, range(1980, 2014)))
    
#makes country name index row, and creates sum row for immigration numbers
df_canada = df_can.set_index('OdName')
df_canada['Total'] = df_canada[year_list].sum(axis=1)

def create_top5():
    df_canada.sort_values(['Total'], ascending = False, axis = 0, inplace = True)
    df_top5 = df_canada.head()
    df_top5 = df_top5[years].transpose()
    return df_top5

def create_line_plot():
    df_top5= create_top5()
    df_top5.plot(kind='area')
    plt.title('Immmigration Trend of Top 5 Countries')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')
    plt.show()
    
def create_histogram():
    count, bin_edges = np.histogram(df_canada[2013])
    df_canada[2013].plot(kind = 'hist', xticks = bin_edges)
    plt.title('Historgram of Immigration in 2013')
    plt.ylabel('Number of Countries')
    plt.xlabel('Number of Immigrants')
    plt.show()
    
def create_bar_chart():
    df_iceland = df_canada.loc['Iceland', years]
    df_iceland.plot(kind = 'bar')
    plt.title('Iceland Immigration')
    plt.xlabel('year')
    plt.ylabel('Number of Immigrants')
    plt.show()
    
def create_pie_chart():
    df_continents = df_canada.groupby('AreaName', axis = 0).sum()
    df_continents['Total'].plot(kind = 'pie')
    plt.title('Imigration by Continent')
    print (df_continents)
    plt.show()
    
def create_box_plot():
    df_japan = df_canada.loc[['Japan'], years].transpose()
    df_japan.plot(kind='box')
    plt.title('Box Plot of Japan Immigrants')
    plt.ylabel('Number of Immigrants')
    plt.show()
    
def create_scatter_plot():
    df_tot = pd.DataFrame(df_can[years].sum(axis=0))
    # change the years to type int (useful for regression later on)
    df_tot.index = map(int, df_tot.index)
    # reset the index to put in back in as a column in the df_tot dataframe
    df_tot.reset_index(inplace = True)
    # rename columns
    df_tot.columns = ['year', 'total']
    
    df_tot.plot(kind='scatter', x='year', y='total')
    plt.title('Total Imigrant Population')
    plt.xlabel('Year')
    plt.ylabel('Number of Immigrants')
    print(df_tot.head())
    print(type(df_tot))
    plt.show()

def create_folium_map():
    canada_map = folium.Map(
        location = [56.130, -106.35],
        zoom_start = 4)
        
    ontario = folium.map.FeatureGroup()
    
    ontario.add_child(
        folium.features.CircleMarker(
        [51.25, -85.32],
        radius = 5,
        color = 'red',
        fill_color = 'Red'))
        
    canada_map.add_child(ontario)
    
    folium.Marker([51.25, -85.32],
        popup = 'Ontario').add_to(candaa_map)
        
    return canada_map
    
create_folium_map()