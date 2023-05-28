import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------------------------------------------------
# Constants
DEFAULT_NUMBER_OF_ROWS = 10
DEFAULT_NUMBER_OF_COLUMNS = 5

# Load the data file into DataFrame
netflix_data = pd.read_csv('netflix_clean_data.csv')

# -------------------------------------------------------------------------------------------------
# Functions

def set_styles(results):
    return (
        results.style
        .set_properties(**{"background-color": "MistyRose", "color": "black"})
    )

# Function to select number of rows and columns
def select_rows_and_columns_from_df(results: pd.DataFrame, key: str):
    no_of_rows_to_show = st.slider(
        "Select number of table rows to display",
        0,
        len(results) - 1,
        DEFAULT_NUMBER_OF_ROWS,
        key=key + 'select_rows',
    )

    columns_to_show = st.multiselect(
        'Select the columns to display',
        ['all', 'show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'year_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
        default='all')

    style = st.checkbox("Style dataframe?", False, key=key + 'table_style')
    return no_of_rows_to_show, columns_to_show, style

@st.cache_data
def _filter_df_results(results, no_of_rows_to_show, columns_to_show) -> pd.DataFrame:
    if 'all' in columns_to_show:
        return results.loc[0:no_of_rows_to_show, :]
    return results.loc[0:no_of_rows_to_show, columns_to_show]


def filter_df_results(results, number_of_rows, number_of_columns, style) -> pd.DataFrame:
    filter_table = _filter_df_results(results, number_of_rows, number_of_columns)
    if style:
        filter_table = set_styles(filter_table)
    return filter_table

# -------------------------------------------------------------------------------------------------
# Set page title
st.title(':red[Netflix] Content Trend Analysis')

# Introduction about the web app
st.write('**Netflix Inc.** is an American media company based in Los Gatos, California. Founded in 1997 by Reed Hastings and Marc Randolph in Scotts Valley, California, it operates the **over-the-top subscription video on-demand service** Netflix brand, which includes **original films and television series commissioned or acquired by the company**, and third-party content licensed from other distributors.')
st.write('They have over 8000 movies or TV shows available on their platform, as of mid-2021, they have over 200M subscribers globally. This dataset has been taken from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and consists of listings of all the movies and tv shows available on Netflix. This dataset was last updated in 2021. ')

# -------------------------------------------------------------------------------------------------
# Set heading # 1
st.header('Data from Netflix (as of mid-2021)')

st.write('The data has **13 columns**. Here are the column description:')
# Print structure of the Dataset
columns_dict = [
    {'Column Name': 'show_id', 'Column Value': 'Unique ID for every Movie / TV show'},
    {'Column Name': 'type', 'Column Value': 'Identifier - A Movie or TV Show'},
    {'Column Name': 'title', 'Column Value': 'Title of the Movie / TV show'},
    {'Column Name': 'director', 'Column Value': 'Director of the Movie'},
    {'Column Name': 'cast', 'Column Value': 'Actors involved in the movie / TV show'},
    {'Column Name': 'country', 'Column Value': 'Country where the movie / TV show was produced'},
    {'Column Name': 'date_added', 'Column Value': 'Date the movie / TV show was added on Netflix'},
    {'Column Name': 'year_added', 'Column Value': 'Year the movie / TV show was added on Netflix'},
    {'Column Name': 'release_year', 'Column Value': 'Actual Release year of the move / TV show'},
    {'Column Name': 'rating', 'Column Value': 'TV Rating of the movie / TV show'},
    {'Column Name': 'duration', 'Column Value': 'Total Duration - in minutes or number of seasons'},
    {'Column Name': 'listed_in', 'Column Value': 'Genre of the movie / TV show'},
    {'Column Name': 'description', 'Column Value': 'The summary description'},
]

st.table(pd.DataFrame(columns_dict))

no_of_rows_to_show, columns_to_show, style = select_rows_and_columns_from_df(netflix_data, key="netflix_data")
filter_table = filter_df_results(netflix_data, no_of_rows_to_show, columns_to_show, style)
st.dataframe(filter_table)

# -------------------------------------------------------------------------------------------------
# Set heading # 2
st.header(':tv: Overall trend of content available on Netflix')

# -------------------------------------------------------------------------------------------------
# Set heading # 3
st.header(':tv: Popularity of different rating categories among Netflix subscribers')

# -------------------------------------------------------------------------------------------------
# Set heading # 4
st.header(":tv: Growth and expansion of the platform's library")

# -------------------------------------------------------------------------------------------------
# Set heading # 5
st.header(":tv: Duration against the release year to check for any patterns in the length of content over time")
