import streamlit as st
import pandas as pd
import numpy as np
import preprocessor as sp
import helper as hp
import world as wd
import country as ct
df = pd.read_csv('total-cancer-deaths-by-type.csv')

options = st.sidebar.radio(
    'Select an Options',
    ('Tally','World-Wise','Country-Wise')
)

st.logo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv5ZyXFsSTqcrgPBIfJY8OKdZXx-2e2J9TFQ&s',size='large')


df = sp.preprocessor(df)
if options == 'Tally':
    st.sidebar.header('World stats')

    st.title("Cancer Tally")

    years,cancer,country = hp.get_year_cancer(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_cancer = st.sidebar.selectbox("Select Cancer Type",cancer)
    selected_country = st.sidebar.selectbox("Select Country", country)

    # t_df = hp.overall(df, selected_year, selected_cancer,selected_country)

    #if selected_year == 'Ovearll':
    t_df = hp.overall(df, selected_year, selected_cancer, selected_country)
    st.dataframe(t_df)


if options == 'World-Wise':

    user_menu = ['Get Statistics and Graph','Specific Cancer Statistics']

    worlds = wd.World_stats(df)
    menus = st.sidebar.selectbox("Select one of among",user_menu)


    if menus == 'Get Statistics and Graph':
        st.title('Statistics By Year')

        years, cancer, country = hp.get_year_cancers(df)

        Selected_year = st.sidebar.selectbox("Select Year", years)
        Selected_Cancer = st.sidebar.selectbox("Select Cancer Type", cancer)

        world_fig = worlds.world_death_rate(Selected_Cancer)

        mean,median,std,maxi = worlds.get_world_stats_by_year(Selected_year)


        col1, col2 = st.columns(2)
        with col1:
            st.header("Mean")
            st.subheader(np.round(mean,3))
        with col2:
            st.header("Median")
            st.subheader(median)

        col3, col4 = st.columns(2)
        with col3:
            st.header("STD")
            st.subheader(np.round(std,3))

        with col4 :
            st.header('Maximum')
            st.subheader(maxi)

        st.header(f'Death Over The Year Due to {Selected_Cancer}')
        st.plotly_chart(world_fig)


    if menus == 'Specific Cancer Statistics':
        st.title('Specific Cancer Statistics')

        years, cancer, country = hp.get_year_cancers(df)
        stats = ["sum","mean","median","max","std"]

        Selected_Year = st.sidebar.selectbox("Selected Year",years)
        Selected_Cancer = st.sidebar.selectbox("Selected Cancer",cancer)
        Selected_stats = st.sidebar.selectbox("selected Statistics",stats)
        Selected_country = st.sidebar.selectbox("Selected Country",country)

        cancer_stats = worlds.cancer_year_stats(Selected_Cancer,Selected_Year,Selected_stats)

        st.table(cancer_stats)

        fg = worlds.compare_stats_with_countries(Selected_country,Selected_Cancer,Selected_Year,Selected_stats)
        st.plotly_chart(fg)


if options == "Country-Wise":
    # st.title("Hello Everyone")
    country = ct.country_stats(df)

    user_menu = ['Get Statistics and Graph',"Compare with different country"]

    menus = st.sidebar.selectbox("Select one of among", user_menu)

    if menus == 'Get Statistics and Graph':
        st.title("Country-Wise Statistics")

        years, cancer, countries = hp.get_year_cancers(df)
        stats = ["sum", "mean", "median", "max", "std"]

        Selected_Year = st.sidebar.selectbox("Selected Year", years)
        Selected_Cancer = st.sidebar.selectbox("Selected Cancer", cancer)
        #Selected_stats = st.sidebar.selectbox("selected Statistics", stats)
        Selected_country = st.sidebar.selectbox("Selected Country", countries)

        fig,mean,median,std,maxi = country.death_over_period(Selected_country,Selected_Cancer,Selected_Year)

        col1, col2 = st.columns(2)
        with col1:
            st.header("Mean")
            st.subheader(np.round(mean, 3))
        with col2:
            st.header("Median")
            st.subheader(median)

        col3, col4 = st.columns(2)
        with col3:
            st.header("STD")
            st.subheader(np.round(std, 3))

        with col4:
            st.header('Maximum')
            st.subheader(maxi)

        st.title(f"Graph of {Selected_Cancer} over the year of {Selected_country}")
        st.plotly_chart(fig)



    if menus == "Compare with different country":
        years, cancer, countries = hp.get_year_cancers(df)


        Selected_Year = st.sidebar.selectbox("Selected Year", years)
        Selected_Cancer = st.sidebar.selectbox("Selected Cancer", cancer)
        Selected_country1 = st.sidebar.selectbox("Selected 1st Country", countries)
        Selected_country2 = st.sidebar.selectbox("Selected 2nd Country", countries)

        pie,fig,t_df = country.compare_countries(Selected_country1,Selected_country2,Selected_Cancer,Selected_Year)
        st.table(t_df)

        st.subheader(f"Cancer Deaths in {Selected_Year}")
        st.plotly_chart(pie)

        st.subheader(f"Cancer Deaths Over Years: {Selected_country1} vs {Selected_country2}")
        st.plotly_chart(fig)

