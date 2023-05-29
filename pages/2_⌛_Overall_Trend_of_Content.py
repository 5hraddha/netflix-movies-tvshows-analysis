import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------------------------------------------------

# Load the data file into DataFrame
netflix_data = pd.read_csv("netflix_clean_data.csv")

# -------------------------------------------------------------------------------------------------

st.title(":hourglass_flowing_sand: Overall Trend of Content available on :red[Netflix]")

st.write(
    """Let's compare the number of contents released per year for both the types
    of content (movies and TV shows) and create a histogram to visualize the 
    distribution of movies and TV shows based on their release year. This will 
    help us understand the overall trend of content available on Netflix and 
    identify any patterns or changes over time.
"""
)

# -------------------------------------------------------------------------------------------------
# Create subtabs
subtab_histogram, subtab_data = st.tabs(["**Histogram**", "**Data**"])

with subtab_histogram:
    st.subheader(
        "Distribution of number of Movies and TV shows based on their year of release"
    )
    # Normalize histograms by percent if checked
    norm = st.checkbox("Do you want to normalize data?", False)
    if norm:
        hnorm = "percent"
    else:
        hnorm = None

    fig_release_year_vs_count_of_contents = px.histogram(
        netflix_data,
        x="release_year",
        color="type",
        labels={"type": "Types of Content on Netflix"},
        color_discrete_map={"Movie": "DodgerBlue", "TV Show": "Red"},
        barmode="overlay",
        histnorm=hnorm,
    )
    fig_release_year_vs_count_of_contents.update_layout(
        yaxis_title="Number of Releases"
    )
    fig_release_year_vs_count_of_contents.update_layout(xaxis_title="Year of Release")
    st.plotly_chart(
        fig_release_year_vs_count_of_contents,
        theme="streamlit",
        use_container_width=True,
    )

with subtab_data:
    st.subheader("Data related to number of Movies and TV shows released per year")
    netflix_year_wise_distribution = netflix_data.pivot_table(
        index="release_year", columns="type", aggfunc="count", values="show_id"
    )
    netflix_year_wise_distribution = netflix_year_wise_distribution.reset_index()
    netflix_year_wise_distribution.columns = [
        "release_year",
        "no_of_movies",
        "no_of_tv_shows",
    ]
    st.dataframe(netflix_year_wise_distribution)

# -------------------------------------------------------------------------------------------------
# Conclusions
st.write(
    """Based on the data above and the insights from the histogram, **we can 
    make several observations about the overall trend of content available on 
    Netflix and identify some patterns or changes over time**:
"""
)
list_of_conclusions = [
    {
        "title": "Increase in Content",
        "description": """The number of movies and TV shows available 
        on Netflix has shown a significant increase over the years. The early 
        years (1925-1967) had a relatively smaller number of releases, but 
        from the early 2000s onwards, there has been a substantial growth in 
        the content offerings.""",
    },
    {
        "title": "Shifting Focus to TV Shows",
        "description": """Initially, Netflix primarily focused 
        on movies, as seen in the early years of the dataset where there were 
        more movies than TV shows. However, starting from around 2013, 
        the number of TV shows being added to Netflix started to increase 
        rapidly.""",
    },
    {
        "title": "Steady Growth of the content library",
        "description": """From the early 2000s to 2017, there was a consistent 
        growth in both movie and TV show releases. The number of additions per 
        year gradually increased, reflecting Netflix's expansion and efforts to 
        diversify its content library.""",
    },
    {
        "title": "Plateauing of Movie Releases",
        "description": """While the number of TV show releases has 
        continued to rise, the number of movies added to Netflix seems to have 
        plateaued since around 2017. This suggests that Netflix has been 
        focusing more on original TV show productions and acquiring TV show 
        licenses, possibly due to their popularity and binge-watching nature.""",
    },
    {
        "title": "Impact of the COVID-19 Pandemic",
        "description": """Looking at the years 2020 and 2021, 
        there is a slight decrease in the number of movie releases compared to 
        previous years. This could be attributed to the disruption caused by 
        the COVID-19 pandemic, which may have affected the production and 
        release schedules of movies.""",
    },
    {
        "title": "Maximum number of movies and TV shows released",
        "description": """The maximum number of TV Shows were released in the 
        year 2020 - 436 shows and the maximum number of movies were released 
        in the years 2017 and 2018 - 767 movies.""",
    },
]

for conclusion in list_of_conclusions:
    with st.expander(conclusion["title"]):
        st.write(conclusion["description"])

st.write(
    """Overall, the data and plot indicates **a significant shift in the 
    content available on Netflix over time, with a emphasis on TV shows 
    and a consistent growth in the number of offerings**. Understanding 
    these trends can help Netflix make informed decisions about their content 
    acquisition and production strategies and cater to the evolving 
    preferences of their global subscriber base.
"""
)
