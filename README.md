<div align="center">
  <a href="https://netflix-content-trend-analysis.onrender.com/" target="_blank">
    <img src="https://raw.githubusercontent.com/5hraddha/netflix-movies-tvshows-analysis/main/notebooks/netflix-logo.png" width=400 alt="netflix logo" />
  </a>
  <h1 align="center">Content Trend Analysis</h1>
</div>

## Introduction

**Netflix Inc.** is an American media company based in Los Gatos, California. Founded in 1997 by Reed Hastings and Marc Randolph in Scotts Valley, California, it operates the **over-the-top subscription video on-demand service** Netflix brand, which includes **original films and television series commissioned or acquired by the company**, and third-party content licensed from other distributors.

They have over 8000 movies or TV shows available on their platform, as of mid-2021, they have over 200M subscribers globally. This dataset has been taken from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and consists of listings of all the movies and tv shows available on Netflix. This dataset was last updated in 2021.

The dataset consists of 12 columns:

1. `show_id`: Unique ID for every Movie / TV show
2. `type`: Identifier - A Movie or TV Show
3. `title`: Title of the Movie / TV show
4. `director`: Director of the Movie
5. `cast`: Actors involved in the movie / TV show
6. `country`: Country where the movie / TV show was produced
7. `date_added`: Date it was added on Netflix
8. `release_year`: Actual Release year of the move / TV show
9. `rating`: TV Rating of the movie / TV show
10. `duration`: Total Duration - in minutes or number of seasons
11. `listed_in`: Genre of the movie / TV show
12. `description`: The summary description

## Project Goal

The project goal is to explore the Netflix dataset to gain insights into the overall content trend, popularity of rating categories, library growth, and duration changes over time:

1. **Overall Trend of Content**: To analyze the release year and number of content released and uncover any patterns or changes in the types of content being added to the platform over time.

2. **Popularity of Rating Categories**: To examine the popularity of different rating categories among Netflix subscribers and get insights into the preferences and viewing habits of the audience in relation to the content's rating.

3. **Growth and Expansion of the Library**: To assess the growth and expansion of Netflix's library over time. By examining variables such as date added, we could determine the rate at which new content was being added to the platform.

4. **Duration and Release Year Analysis**: To investigate the relationship between the duration (in minutes or number of seasons) and the release year of the content and to identify any patterns or changes in the length of movies or TV shows over time.

## Steps to run the Web App locally

1. Clone the Github Repository:

```shell
git clone https://github.com/5hraddha/netflix-movies-tvshows-analysis.git
```

2. Make sure that you are in the root directory of the cloned repository - `netflix-movies-tvshows-analysis`. Install all the libraries by running:

```shell
pip install -r requirements.txt
```

3. Run the interactive web app locally by running:

```shell
streamlit run Home.py
```

4. Navigate to `http://0.0.0.0:10000` in the web browser to see the web app.

## Recorded Demo

## Live Web App

[Visit Here](https://netflix-content-trend-analysis.onrender.com/)
