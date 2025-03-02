import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import streamlit as st


class World_stats:
    def __init__(self,canc):
        self.canc = canc


    def world_death_rate(self,cancer_type):
        # df = self.canc.groupby(['Type of cancer','Year'])['Death'].sum().reset_index()
        # t_df = df[df['Type of cancer'] == cancer_type]
        # #plt.figure(figsize=(7,7))
        # sns.lineplot(data=t_df,x='Year',y='Death',color='red')
        # plt.title(f"World's Death rate over period, due to {cancer_type}")
        if cancer_type == "Overall":
            t_df = self.canc.groupby(['Type of cancer', 'Year'])['Death'].sum().reset_index()

        else:
            df = self.canc.groupby(['Type of cancer', 'Year'])['Death'].sum().reset_index()
            t_df = df[df['Type of cancer'] == cancer_type]

        # Create a figure explicitly
        #fig, ax = plt.subplots(figsize=(7, 5))
        fig = px.line(data_frame=t_df, x='Year', y='Death')
        plt.title(f"World's Death Rate Over Period Due to {cancer_type}")
        # ax.set_xlabel("Year")
        # ax.set_ylabel("Deaths")

        return fig

    def get_world_stats_by_year(self,year):
        # Return stats of a particular year

        df_1 = self.canc.groupby(['Year'])
        df_2 = self.canc.groupby(['Year'])
        df_3 = self.canc.groupby(['Year'])
        df_4 = self.canc.groupby(['Year'])

        if year == 'Overall':
            return df_1['Death'].mean(), df_2['Death'].median(), df_3['Death'].std(), df_4['Death'].max()

        else:
            df_1 = self.canc[(self.canc['Year'] == year)]['Death'].mean()
            df_2 = self.canc[(self.canc['Year'] == year)]['Death'].median()
            df_3 = self.canc[(self.canc['Year'] == year)]['Death'].std()
            df_4 = self.canc[(self.canc['Year'] == year)]['Death'].max()

            return df_1, df_2, df_3, df_4





    def cancer_year_stats(self,cancer_type,year,stats='sum'):
        '''Return how many people died due to particular cancer in the particular year in the world'''
        if stats == 'sum':
            df = self.canc.groupby(['Type of cancer','Year'])['Death'].sum().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')

        elif stats == 'mean':
            df = self.canc.groupby(['Type of cancer','Year'])['Death'].mean().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')

        elif stats == 'median':
            df = self.canc.groupby(['Type of cancer','Year'])['Death'].median().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')

        elif stats == 'std':
            df = self.canc.groupby(['Type of cancer','Year'])['Death'].std().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')

        elif stats == 'max':
            df = self.canc.groupby(['Type of cancer','Year'])['Death'].max().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')

        else:
            df = self.canc.groupby(['Type of cancer','Year'])['Death'].min().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')

        # self.cancer = t_df.values[0][0]
        # self.stats = t_df.values[0][1]
        return t_df



    def cancer_overall_stats(self,cancer_type,stats='sum'):

        '''Return how many people died due to particular cancer in the particular year in the world'''
        if stats == 'sum':
            df = self.canc.groupby(['Type of cancer'])['Death'].sum().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type)]

        elif stats == 'mean':
            df = self.canc.groupby(['Type of cancer'])['Death'].mean().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type)]

        elif stats == 'median':
            df = self.canc.groupby(['Type of cancer'])['Death'].median().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type)]

        elif stats == 'std':
            df = self.canc.groupby(['Type of cancer'])['Death'].std().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type)]

        elif stats == 'max':
            df = self.canc.groupby(['Type of cancer'])['Death'].max().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type)]

        else:
            df = self.canc.groupby(['Type of cancer'])['Death'].min().reset_index()

            t_df = df[(df['Type of cancer'] == cancer_type)]

        self.cancer = t_df.values[0][0]
        self.stats = t_df.values[0][1]
        return t_df


    def compare_stats_with_countries(self,country,cancer_type,year,stats='sum'):
        '''Compare no. of people died due to particular cancer with particular country and world in specific year'''

        if stats == 'sum':
            df = self.canc.groupby(['Entity','Type of cancer','Year'])['Death'].sum().reset_index()

        elif stats == 'mean':
            df = self.canc.groupby(['Entity','Type of cancer','Year'])['Death'].mean().reset_index()
        elif stats == 'median':
            df = self.canc.groupby(['Entity','Type of cancer','Year'])['Death'].median().reset_index()
        # elif stats == 'std':
        #     df = self.canc.groupby(['Entity','Type of cancer','Year'])['Death'].std().reset_index()
        elif stats == 'max':
            df = self.canc.groupby(['Entity','Type of cancer','Year'])['Death'].max().reset_index()
        else:
            df = self.canc.groupby(['Entity','Type of cancer','Year'])['Death'].sum().reset_index()


        t_df = df[(df['Entity'] == country) & (df['Type of cancer'] == cancer_type) & (df['Year'] == year)].set_index('Year')
        country_ = self.cancer_year_stats(cancer_type,year,stats)
        key = [country,'World']
        l = np.array([t_df['Death'].unique(),country_['Death'].values]).ravel()
        #plt.pie(l,labels=key,autopct='%.0f%%')
        fg= px.pie(data_frame=t_df, names=key, values=l)


        return fg

    # def compare_with_countries(self,country,cancer_type):
    #     '''Compare no. of people died due to particular cancer with particular country and world till 2019'''
    #     df = self.canc.groupby(['Entity','Type of cancer'])['Death'].sum().reset_index()

    #     t_df = df[(df['Entity'] == country) & (df['Type of cancer'] == cancer_type)]
    #     death_in_world = self.canc[self.canc['Type of cancer'] == cancer_type]['Death'].sum()
    #     key = [country,'World']
    #     l = np.array([t_df['Death'].values[0],death_in_world]).ravel()
    #     plt.pie(l,labels=key,autopct='%.0f%%')

