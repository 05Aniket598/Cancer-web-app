import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

class country_stats:
    def __init__(self,df):
        self.df = df


    def death_over_period(self,country_name,cancer_type,year):
        if cancer_type == "Overall":
            t_df = self.df.groupby(['Entity','Type of cancer', 'Year'])['Death'].sum().reset_index()

        else:
            df = self.df.groupby(['Entity','Type of cancer', 'Year'])['Death'].sum().reset_index()
            t_df = df[(df['Entity'] == country_name)&(df['Type of cancer'] == cancer_type)]

        df_1 = self.df[(self.df['Type of cancer'] == cancer_type) & (self.df['Entity'] == country_name) & (self.df['Year'] == year)]['Death'].mean()
        df_2 = self.df[(self.df['Type of cancer'] == cancer_type) & (self.df['Entity'] == country_name) & (self.df['Year'] == year)]['Death'].median()
        df_3 = self.df[(self.df['Type of cancer'] == cancer_type) & (self.df['Entity'] == country_name) & (self.df['Year'] == year)]['Death'].std()
        df_4 = self.df[(self.df['Type of cancer'] == cancer_type) & (self.df['Entity'] == country_name)]['Death'].max()


        fig = px.line(data_frame=t_df, x='Year', y='Death')
        plt.title(f"World's Death Rate Over Period Due to {cancer_type}")
        return fig , df_1 , df_2 , df_3,df_4

    def get_country_stats_by_year(self,year,country):
        # Return stats of a particular year

        df_1 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].mean()
        df_2 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].median()
        df_3 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].std()
        df_4 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].max()

        if (year == 'Overall') :
            return df_1['Death'].mean(), df_2['Death'].median(), df_3['Death'].std(), df_4['Death'].max()

        else:
            df_1 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].mean()
            df_2 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].median()
            df_3 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].std()
            df_4 = self.df[(self.df['Year'] == year)&(self.df['Entity'] == country)]['Death'].max()

            return df_1, df_2, df_3, df_4

    def compare_countries(self, country1, country2, cancer, year):
        # Grouping data by country, cancer type, and year
        df = self.df.groupby(['Entity', 'Type of cancer', 'Year'])['Death'].sum().reset_index()

        # Filtering for the selected year (Pie Chart Data)
        t_df1 = df[(df['Entity'] == country1) & (df['Type of cancer'] == cancer) & (df['Year'] == year)]
        t_df2 = df[(df['Entity'] == country2) & (df['Type of cancer'] == cancer) & (df['Year'] == year)]

        # Combine data for pie chart
        t_df = pd.concat([t_df1, t_df2])
        key = [country1, country2]
        l = np.array([t_df1['Death'].values[0], t_df2['Death'].values[0]]).ravel()
        pie_fig = px.pie(data_frame=t_df, values=l, names=key)

        # Filtering data for bar chart (Deaths over multiple years)
        bar_df = df[(df['Entity'].isin([country1, country2])) & (df['Type of cancer'] == cancer)]

        # Create the bar chart using Plotly Express

        bar_fig = px.bar(
            bar_df, x="Year", y="Death", color="Entity", barmode="group",
            labels={"Death": "Number of Deaths", "Year": "Year"},
            text_auto=True  # Display numbers on bars
        )

        return pie_fig, bar_fig, t_df.set_index('Year')