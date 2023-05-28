import streamlit as st
import pandas as pd
import plotly.express as px

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
# Set page title
st.title(":red[Netflix] Content Trend Analysis")

# Introduction about the web app
st.write(
    "**Netflix Inc.** is an American media company based in Los Gatos, California. Founded in 1997 by Reed Hastings and Marc Randolph in Scotts Valley, California, it operates the **over-the-top subscription video on-demand service** Netflix brand, which includes **original films and television series commissioned or acquired by the company**, and third-party content licensed from other distributors."
)
st.write(
    "They have over 8000 movies or TV shows available on their platform, as of mid-2021, they have over 200M subscribers globally. This dataset has been taken from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and consists of listings of all the movies and tv shows available on Netflix. This dataset was last updated in 2021. "
)

# -------------------------------------------------------------------------------------------------
# Set heading # 1
st.header("Data from Netflix (as of mid-2021)")

st.write("The data has **13 columns**. Here are the column description:")
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

no_of_rows_to_show, columns_to_show, is_dark_theme = get_attributes_to_filter_df(
    netflix_data, key="netflix_data"
)
filtered_df = get_filtered_df(netflix_data, no_of_rows_to_show, columns_to_show)
if is_dark_theme:
    filtered_df = set_df_styles(filtered_df, "black", "white")
st.dataframe(filtered_df)

# -------------------------------------------------------------------------------------------------
# Set heading # 2
st.header(":tv: Overall trend of content available on Netflix")
fig_release_year_vs_count_of_contents = px.histogram(
    netflix_data,
    x="release_year",
    color="type",
    title="Distribution of number of Movies and TV shows based on their year of release",
    labels={"type": "Types of Content on Netflix"},
    color_discrete_map={"Movie": "DodgerBlue", "TV Show": "Red"},
    barmode="overlay",
)
fig_release_year_vs_count_of_contents.update_layout(yaxis_title="Number of Releases")
fig_release_year_vs_count_of_contents.update_layout(xaxis_title="Year of Release")
st.plotly_chart(
    fig_release_year_vs_count_of_contents, theme="streamlit", use_container_width=True
)

# -------------------------------------------------------------------------------------------------
# Set heading # 3
st.header(":tv: Popularity of different rating categories among Netflix subscribers")
fig_rating_vs_count_of_contents = px.histogram(
    netflix_data,
    x="rating",
    color="type",
    title="Distribution of number of Movies and TV shows based on their ratings",
    labels={"type": "Types of Content on Netflix"},
    color_discrete_map={"Movie": "DodgerBlue", "TV Show": "Red"},
    barmode="overlay",
)
fig_rating_vs_count_of_contents.update_layout(yaxis_title="Number of movies / TV Shows")
fig_rating_vs_count_of_contents.update_layout(xaxis_title="TV Ratings")
st.plotly_chart(
    fig_rating_vs_count_of_contents, theme="streamlit", use_container_width=True
)
# -------------------------------------------------------------------------------------------------
# Set heading # 4
st.header(":tv: Growth and expansion of the platform's library")
fig_year_added_vs_count_of_contents = px.histogram(
    netflix_data,
    x="year_added",
    color="type",
    title="Frequency of content additions to Netflix over time",
    labels={"type": "Types of Content on Netflix"},
    color_discrete_map={"Movie": "DodgerBlue", "TV Show": "Red"},
    barmode="overlay",
)
fig_year_added_vs_count_of_contents.update_layout(
    yaxis_title="Number of Movies / TV Show"
)
fig_year_added_vs_count_of_contents.update_layout(xaxis_title="Year added to Netflix")
st.plotly_chart(
    fig_year_added_vs_count_of_contents, theme="streamlit", use_container_width=True
)

# -------------------------------------------------------------------------------------------------
# Set heading # 5
st.header(":tv: Patterns in the duration of contents over time")

# Divide the dataframe - netflix_data into two - netflix_movies and netflix_tv_shows
netflix_movies = netflix_data[netflix_data["type"] == "Movie"]
netflix_movies = netflix_movies.reset_index(drop=True)

netflix_tv_shows = netflix_data[netflix_data["type"] == "TV Show"]
netflix_tv_shows = netflix_tv_shows.reset_index(drop=True)

# Clean up the duration column in both the dataframes - netflix_movies and netflix_tv_shows
netflix_movies["duration"] = netflix_movies["duration"].str.replace(" min", "")
netflix_movies["duration"] = netflix_movies["duration"].astype(int)

netflix_tv_shows["duration"] = netflix_tv_shows["duration"].str.replace(" Season", "")
netflix_tv_shows["duration"] = netflix_tv_shows["duration"].str.replace("s", "")
netflix_tv_shows["duration"] = netflix_tv_shows["duration"].astype(int)

# Plot a scatterplot for movies on Netflix - release_year on x-axis and duration on y-axis
fig_scatter_movies = px.scatter(
    netflix_movies,
    x="release_year",
    y="duration",
    title="Distribution of duration of movies against the year of release",
    height=800,
)
fig_scatter_movies.update_layout(yaxis_title="Duration (in mins)")
fig_scatter_movies.update_layout(xaxis_title="Year of Release")
st.plotly_chart(fig_scatter_movies, theme="streamlit", use_container_width=True)

# Plot a scatterplot for movies on Netflix - release_year on x-axis and duration on y-axis
fig_scatter_tv_shows = px.scatter(
    netflix_tv_shows,
    x="release_year",
    y="duration",
    title="Distribution of duration of TV shows against the year of release",
    height=800,
)
fig_scatter_tv_shows.update_layout(yaxis_title="Duration (no of seasons)")
fig_scatter_tv_shows.update_layout(xaxis_title="Year of Release")
st.plotly_chart(fig_scatter_tv_shows, theme="streamlit", use_container_width=True)
