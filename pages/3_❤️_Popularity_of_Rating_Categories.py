import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------------------------------------------------

# Load the data file into DataFrame
netflix_data = pd.read_csv("netflix_clean_data.csv")

# -------------------------------------------------------------------------------------------------

st.title(":hearts: Popularity of Rating Categories among :red[Netflix] subscribers")

st.write(
    """Let's compare the number of contents released per rating for both the 
    types of contents (movies and TV shows) and plot a histogram to analyze 
    the distribution of movies and TV shows based on their ratings. This can 
    help us understand the popularity of different rating categories among 
    Netflix subscribers..
    """
)

# -------------------------------------------------------------------------------------------------
# Create subtabs
subtab_histogram, subtab_data = st.tabs(["**Histogram**", "**Data**"])

with subtab_histogram:
    st.subheader("Distribution of number of Movies and TV shows based on their ratings")
    # Normalize histograms by percent if checked
    norm = st.checkbox("Do you want to normalize data?", False)
    if norm:
        hnorm = "percent"
    else:
        hnorm = None
    fig_rating_vs_count_of_contents = px.histogram(
        netflix_data,
        x="rating",
        color="type",
        title="Distribution of number of Movies and TV shows based on their ratings",
        labels={"type": "Types of Content on Netflix"},
        color_discrete_map={"Movie": "DodgerBlue", "TV Show": "Red"},
        barmode="overlay",
        histnorm=hnorm,
    )
    fig_rating_vs_count_of_contents.update_layout(
        yaxis_title="Number of movies / TV Shows"
    )
    fig_rating_vs_count_of_contents.update_layout(xaxis_title="TV Ratings")
    st.plotly_chart(
        fig_rating_vs_count_of_contents, theme="streamlit", use_container_width=True
    )

with subtab_data:
    st.subheader("Data related to number of Movies and TV shows released per rating")
    netflix_rating_wise_distribution = netflix_data.pivot_table(
        index="rating", columns="type", aggfunc="count", values="show_id"
    )
    netflix_rating_wise_distribution = netflix_rating_wise_distribution.reset_index()
    netflix_rating_wise_distribution.columns = [
        "rating",
        "no_of_movies",
        "no_of_tv_shows",
    ]
    st.dataframe(netflix_rating_wise_distribution)

# -------------------------------------------------------------------------------------------------
# Conclusions
st.write(
    """Based on the data and the histogram above, **we can conclude the 
    following about the popularity of different rating categories 
    among Netflix subscribers**:
"""
)

list_of_conclusions = [
    {
        "title": "TV-MA (Mature Audience)",
        "description": """TV-MA rated content has the highest number 
        of both movies (2062) and TV shows (1145) available on Netflix. 
        This rating category is intended for mature audiences and indicates 
        that **Netflix has a significant amount of content targeting adult 
        viewers**.""",
    },
    {
        "title": "TV-14 (Parents Strongly Cautioned)",
        "description": """The TV-14 rating category is the second most 
        popular among Netflix subscribers, with 1427 movies and 733 TV 
        shows falling under this rating. This suggests that **there is a 
        substantial demand for content suitable for viewers aged 14 
        and above.**""",
    },
    {
        "title": "R-Rated Movies",
        "description": """Among movies specifically, the R rating category 
        is one of the most prevalent, with 797 movies available on Netflix. 
        The R rating indicates that the content may contain adult themes, 
        strong language, violence, or other mature content. This 
        suggests that **there is a significant audience for more mature 
        and adult-oriented movies on the platform.**""",
    },
    {
        "title": "TV-PG and TV-G",
        "description": """**TV-PG and TV-G ratings have a moderate presence 
        on Netflix**, with 540 movies and 323 TV shows falling under the 
        TV-PG category, and 126 movies and 94 TV shows classified as TV-G. 
        These ratings are suitable for general audiences and may appeal 
        to families and younger viewers.""",
    },
    {
        "title": "Limited Availability of Other Ratings",
        "description": """The plot indicates a limited number of movies 
        and TV shows in other rating categories such as G, NC-17, NR, 
        PG, and PG-13. This could suggest that Netflix focuses more on 
        content for mature audiences (TV-MA and TV-14) and may have a 
        relatively smaller selection of content for younger or 
        family-oriented audiences.""",
    },
]
for conclusion in list_of_conclusions:
    with st.expander(conclusion["title"]):
        st.write(conclusion["description"])

st.write(
    """Overall, the data suggests that Netflix subscribers have 
    a higher preference for content rated TV-MA and TV-14, indicating 
    a significant demand for mature and adult-oriented programming.
"""
)
