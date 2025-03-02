import numpy as np
import pandas as pd
import streamlit as st


def get_year_cancer(canc):
    cancer = canc['Type of cancer'].unique().tolist()
    year = canc['Year'].unique().tolist()
    country = canc['Entity'].unique().tolist()
    country.sort()
    year.sort()
    cancer.sort()

    year.insert(0, 'Overall')
    cancer.insert(0, 'Overall')
    country.insert(0, 'Overall')

    return year, cancer, country

def get_year_cancers(canc):
    cancer = canc['Type of cancer'].unique().tolist()
    year = canc['Year'].unique().tolist()
    country = canc['Entity'].unique().tolist()
    country.sort()
    year.sort()
    cancer.sort()

    return year, cancer, country


def overall(canc, year, cancer_type, country):
    if (year == 'Overall') & (cancer_type == 'Overall') & (country == 'Overall'):
        # st.subheader('Cancer Tally From Year 1990-2019')
        return canc[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year != 'Overall') & (cancer_type == 'Overall') & (country == 'Overall'):
        temp_df = canc[canc['Year'] == year]
        # st.subheader(f"Cancer Tally Of Year {year}.")
        # st.write(f"This table contains year {year} , all countries and all type of cancer data.")
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year == 'Overall') & (cancer_type != 'Overall') & (country == 'Overall'):
        temp_df = canc[canc['Type of cancer'] == cancer_type]
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year == 'Overall') & (cancer_type == 'Overall') & (country != 'Overall'):
        temp_df = canc[canc['Entity'] == country]
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year != 'Overall') & (cancer_type != 'Overall') & (country == 'Overall'):
        temp_df = canc[(canc['Type of cancer'] == cancer_type) & (canc['Year'] == year)]
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year == 'Overall') & (cancer_type != 'Overall') & (country != 'Overall'):
        temp_df = canc[(canc['Type of cancer'] == cancer_type) & (canc['Entity'] == country)]
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year != 'Overall') & (cancer_type == 'Overall') & (country != 'Overall'):
        temp_df = canc[(canc['Year'] == year) & (canc['Entity'] == country)]
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')

    if (year != 'Overall') & (cancer_type != 'Overall') & (country != 'Overall'):
        temp_df = canc[(canc['Year'] == year) & (canc['Type of cancer'] == cancer_type) & (canc['Entity'] == country)]
        return temp_df[['Entity', 'Year', 'Type of cancer', 'Death']].set_index('Year')




def get_counties(df):
    country = df['Entity'].unique().tolist()
    country.sort()
    return country