import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------------------------------------------------

# Load the data file into DataFrame
netflix_data = pd.read_csv("netflix_clean_data.csv")

# -------------------------------------------------------------------------------------------------
st.title(":calendar: Duration and Release Year Analysis")

st.write(
    """Let's analyze the duration (in minutes for movies or number 
    of seasons for TV shows) against the release year can reveal 
    any patterns or changes in the length of content over time.
    """
)

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
    title="Distribution of duration of Movies against the year of release",
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

# -------------------------------------------------------------------------------------------------
# Conclusions
st.write("""With the scatter plots above, we can conclude below things:""")
list_of_conclusions = [
    """There is a trend towards shorter and medium length movies.""",
    """There are a few really long length movies released lately too.""",
    """There is a trend towards longer TV Shows.""",
]

for item in list_of_conclusions:
    st.markdown("- " + item)
