import streamlit as st
import pandas as pd

# -------------------------------------------------------------------------------------------------
# Constants
DEFAULT_NUMBER_OF_ROWS = 10
DEFAULT_NUMBER_OF_COLUMNS = 5

# Load the data file into DataFrame
netflix_data = pd.read_csv("netflix_clean_data.csv")

# -------------------------------------------------------------------------------------------------
# Functions


# Function to set dark theme for Dataframe
def set_df_styles(results: pd.DataFrame, bg_color: str, font_color: str):
    return results.style.set_properties(
        **{"background-color": bg_color, "color": font_color}
    )


# Function to select number of rows and list of columns to filter Dataframe
def get_attributes_to_filter_df(results: pd.DataFrame, key: str) -> tuple:
    no_of_rows_to_show = st.slider(
        "Select number of table rows to display",
        0,
        len(results) - 1,
        DEFAULT_NUMBER_OF_ROWS,
        key=key + "_select_rows",
    )

    columns_to_show = st.multiselect(
        "Select the columns to display",
        [
            "all",
            "show_id",
            "type",
            "title",
            "director",
            "cast",
            "country",
            "date_added",
            "year_added",
            "release_year",
            "rating",
            "duration",
            "listed_in",
            "description",
        ],
        default="all",
        key=key + "_select_columns",
    )

    is_dark_theme = st.checkbox(
        "Want Dataframe in Dark Theme?", False, key=key + "_df_style"
    )
    return no_of_rows_to_show, columns_to_show, is_dark_theme


# Function to filter Dataframe based on no of rows and list of columns selected
@st.cache_data
def get_filtered_df(
    results: pd.DataFrame, no_of_rows_to_show: int, columns_to_show: list
) -> pd.DataFrame:
    if "all" in columns_to_show:
        filtered_df = results.loc[0:no_of_rows_to_show, :]
    else:
        filtered_df = results.loc[0:no_of_rows_to_show, columns_to_show]

    return filtered_df


# -------------------------------------------------------------------------------------------------
st.title("Data from :red[Netflix] (as of mid-2021)")

st.write(
    """This dataset has been taken from 
    [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and 
    consists of listings of all the movies and tv shows available on Netflix. 
    This dataset was last updated in 2021. It has **13 columns**. 
    Here are the **column descriptions**:"""
)

# Print structure of the Dataset
columns_dict = [
    {"Column Name": "show_id", "Column Value": "Unique ID for every Movie / TV show"},
    {"Column Name": "type", "Column Value": "Identifier - A Movie or TV Show"},
    {"Column Name": "title", "Column Value": "Title of the Movie / TV show"},
    {"Column Name": "director", "Column Value": "Director of the Movie"},
    {"Column Name": "cast", "Column Value": "Actors involved in the movie / TV show"},
    {
        "Column Name": "country",
        "Column Value": "Country where the movie / TV show was produced",
    },
    {
        "Column Name": "date_added",
        "Column Value": "Date the movie / TV show was added on Netflix",
    },
    {
        "Column Name": "year_added",
        "Column Value": "Year the movie / TV show was added on Netflix",
    },
    {
        "Column Name": "release_year",
        "Column Value": "Actual Release year of the move / TV show",
    },
    {"Column Name": "rating", "Column Value": "TV Rating of the movie / TV show"},
    {
        "Column Name": "duration",
        "Column Value": "Total Duration - in minutes or number of seasons",
    },
    {"Column Name": "listed_in", "Column Value": "Genre of the movie / TV show"},
    {"Column Name": "description", "Column Value": "The summary description"},
]

st.table(pd.DataFrame(columns_dict))

st.write(
    """In order to peek into the data, you can select the number 
    of rows and the list of columns using the slider and the 
    multiselect menu given below:"""
)
no_of_rows_to_show, columns_to_show, is_dark_theme = get_attributes_to_filter_df(
    netflix_data, key="netflix_data"
)
filtered_df = get_filtered_df(netflix_data, no_of_rows_to_show, columns_to_show)
if is_dark_theme:
    filtered_df = set_df_styles(filtered_df, "black", "white")
st.dataframe(filtered_df)
