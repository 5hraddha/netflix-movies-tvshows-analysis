# Import Libraries
import streamlit as st

# -------------------------------------------------------------------------------------------------
# Page Configuration
st.set_page_config(
    page_title="Netflix Content Trend Analysisl", page_icon=":bar_chart:", layout="wide"
)

# -------------------------------------------------------------------------------------------------
# Page Title
header_col_1, header_col_2, header_col_3 = st.columns([1, 2, 1])
with header_col_1:
    st.write(" ")
with header_col_2:
    st.image("./notebooks/netflix-logo.png", use_column_width=True)
with header_col_3:
    st.write(" ")

st.markdown(
    "<h1 style='text-align:center;'>Content Trend Analysis</h1>", unsafe_allow_html=True
)

# -------------------------------------------------------------------------------------------------
# Introduction about the web app
st.header("Introduction")
st.write(
    """**Netflix Inc.** is an American media company based in Los Gatos,
      California. Founded in 1997 by Reed Hastings and Marc Randolph 
      in Scotts Valley, California, it operates the **over-the-top 
      subscription video on-demand service** Netflix brand, which 
      includes **original films and television series commissioned 
      or acquired by the company**, and third-party content licensed
        from other distributors."""
)
st.write(
    """They have over 8000 movies or TV shows available on their 
    platform, as of mid-2021, they have over 200M subscribers globally. 
    This dataset has been taken from 
    [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and 
    consists of listings of all the movies and tv shows available on Netflix. 
    This dataset was last updated in 2021."""
)

# -------------------------------------------------------------------------------------------------
# Project Goal
st.divider()
st.header("Project Goals")
st.write(
    """The project goal is to explore the Netflix dataset to gain 
insights into the overall content trend, popularity of rating categories, 
library growth, and duration changes over time:
"""
)
list_of_project_goals = [
    """**Overall Trend of Content**: To analyze the release year and number of 
    content released and uncover any patterns or changes in the types of content 
    being added to the platform over time.""",
    """**Popularity of Rating Categories**: To examine the popularity of different 
    rating categories among Netflix subscribers and get insights into the preferences 
    and viewing habits of the audience in relation to the content's rating.""",
    """**Growth and Expansion of the Library**: To assess the growth and expansion 
    of Netflix's library over time. By examining variables such as date added, we 
    could determine the rate at which new content was being added to the platform""",
    """**Duration and Release Year Analysis**: To investigate the relationship between 
    the duration (in minutes or number of seasons) and the release year of the content 
    and to identify any patterns or changes in the length of movies or TV shows over time.""",
]

for item in list_of_project_goals:
    st.markdown("- " + item)

# -------------------------------------------------------------------------------------------------
# Contact Details
st.divider()
c1, c2, c3, c4 = st.columns(4)
with c2:
    st.info("**LinkedIn: [@5hraddha](https://www.linkedin.com/in/5hraddha)**", icon="💡")
with c3:
    st.info("**GitHub: [@5hraddha](https://github.com/5hraddha)**", icon="💻")
