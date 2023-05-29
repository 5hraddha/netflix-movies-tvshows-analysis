import streamlit as st
import pandas as pd
from plotly import express as px

# -------------------------------------------------------------------------------------------------

# Load the data file into DataFrame
netflix_data = pd.read_csv("netflix_clean_data.csv")

# -------------------------------------------------------------------------------------------------

st.title(":seedling: Growth and Expansion of the :red[Netflix]'s library")

st.write(
    """Let's compare the number of contents added to Netflix per year for both 
    the types of contents (movies and TV shows) and plot a histogram to 
    visualize the frequency of content additions to Netflix over time. 
    This can provide us insights into the growth and expansion of the 
    platform's library.
    """
)

# -------------------------------------------------------------------------------------------------
# Create subtabs
subtab_histogram, subtab_data = st.tabs(["**Histogram**", "**Data**"])

with subtab_histogram:
    st.subheader(
        "Distribution of number of Movies and TV shows added to Netflix per year"
    )
    # Normalize histograms by percent if checked
    norm = st.checkbox("Do you want to normalize data?", False)
    if norm:
        hnorm = "percent"
    else:
        hnorm = None
    fig_year_added_vs_count_of_contents = px.histogram(
        netflix_data,
        x="year_added",
        color="type",
        title="Frequency of content additions to Netflix over time",
        labels={"type": "Types of Content on Netflix"},
        color_discrete_map={"Movie": "DodgerBlue", "TV Show": "Red"},
        barmode="overlay",
        histnorm=hnorm,
    )
    fig_year_added_vs_count_of_contents.update_layout(
        yaxis_title="Number of Movies / TV Show"
    )
    fig_year_added_vs_count_of_contents.update_layout(
        xaxis_title="Year added to Netflix"
    )
    st.plotly_chart(
        fig_year_added_vs_count_of_contents, theme="streamlit", use_container_width=True
    )

with subtab_data:
    st.subheader(
        "Data related to number of Movies and TV shows added to Netflix per year"
    )
    netflix_added_year_wise_distribution = netflix_data.pivot_table(
        index="year_added", columns="type", aggfunc="count", values="show_id"
    )
    netflix_added_year_wise_distribution = (
        netflix_added_year_wise_distribution.reset_index()
    )
    netflix_added_year_wise_distribution.columns = [
        "year_added",
        "no_of_movies",
        "no_of_tv_shows",
    ]
    st.dataframe(netflix_added_year_wise_distribution)

# -------------------------------------------------------------------------------------------------
# Conclusions
st.write(
    """Based on the data above and histogram, we can gain the following 
    insights into the growth and expansion of Netflix's library over time::
"""
)

list_of_conclusions = [
    {
        "title": "Steady Growth",
        "description": """The number of content additions to Netflix 
        has shown a consistent upward trend from 2008 to 2021, indicating 
        the platform's continuous expansion. The number of movies and TV 
        shows added per year has generally increased over time.""",
    },
    {
        "title": "Accelerated Growth in Recent Years",
        "description": """The most substantial growth in content additions 
        occurred in the years 2016 to 2021. During this period, there was 
        a significant surge in both movie and TV show additions, with 
        notable spikes in 2017, 2018, and 2019.""",
    },
    {
        "title": "Shift towards TV Shows",
        "description": """While the number of movie additions has remained 
        relatively consistent over the years, there has been a notable 
        increase in TV show additions. This indicates a strategic shift 
        by Netflix towards expanding its TV show library, possibly in 
        response to the growing popularity of binge-watching and 
        serialized content.""",
    },
    {
        "title": "High Growth in 2017-2019",
        "description": """The years 2017, 2018, and 2019 witnessed remarkable 
        growth in content additions, with the highest number of movies and TV 
        shows added during this period. This could be attributed to Netflix's 
        aggressive content acquisition and production strategies, including 
        the release of original series and licensing deals with various 
        studios.""",
    },
    {
        "title": "Slight Decrease in 2020-2021",
        "description": """The years 2020 and 2021 saw a slight decrease 
        in the number of content additions compared to the peak years 
        of 2017-2019.""",
    },
]
for conclusion in list_of_conclusions:
    with st.expander(conclusion["title"]):
        st.write(conclusion["description"])

st.write(
    """Overall, the data suggests that Netflix has experienced significant 
    growth and expansion in its content library over the years, with a 
    focus on increasing the number of TV shows. The platform has 
    continuously added new movies and TV shows, contributing to its vast 
    collection and offering diverse options to its subscribers.
"""
)
