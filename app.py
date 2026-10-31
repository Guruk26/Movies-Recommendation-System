# 🎬 Movie Recommendation System
# A lightweight Streamlit interface for finding movies with similar content.
# The app uses preprocessed movie data and a precomputed similarity matrix.

import streamlit as st
import nltk  # Natural-language toolkit; available for text-processing workflows.
import sklearn  # Machine-learning utilities used by the project's recommendation workflow.
import pandas as pd  # Tabular data handling for the movie dataset.
import pickle  # Loads the saved movie table.
import joblib  # Loads the saved similarity matrix efficiently.

# Give the app a clear title at the top of the page.
st.title("Movie Recommendation System")

# Load the preprocessed movie data saved during notebook development.
# The binary file contains the movie table used to look up titles and recommendation rows.
with open("movies.pickle",'rb') as m:
    movies=pickle.load(m)

# Load the precomputed pairwise similarity scores.
# Each row corresponds to a movie; each value indicates its similarity to another movie.
similarity=joblib.load("similarity.joblib")

# Collect the movie titles that will populate the selection dropdown.
movie_names=movies['title'].values

# 🎯 Recommendation engine: find the five most similar movies for a selected title.
def recommend(name_movie):
    # Locate the selected movie's row in the dataset.
    movie_index=movies[movies['title']==name_movie].index[0]

    # Fetch similarity scores between the selected movie and every movie in the dataset.
    recommendations=similarity[movie_index]

    # Sort movies from highest to lowest similarity.
    # The first result is skipped because it is normally the selected movie itself.
    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]

    # Translate the top matching row indexes into human-readable movie titles.
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    # Return the list for the Streamlit interface to display.
    return recommended_movies

# 🎞️ Let the user choose a movie from the available titles.
name_movie=st.selectbox("Enter the Movie Name",movie_names)

# Run the recommendation logic only when the user clicks the button.
if st.button("Recommend"):
    r=recommend(name_movie)
    st.write("## The Recommend Movies are :")

    # Show each recommended title as a separate result on the page.
    for i in r:
        st.write(i)
