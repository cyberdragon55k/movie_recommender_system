import pickle
import streamlit as st
import requests
import pandas as pd
import time


# --- Function to Fetch Movie Posters with Error Handling ---
def fetch_poster(movie_id):
    """
    Fetches a movie poster from the TMDb API.
    Returns a placeholder URL if the API call fails or if no poster exists.
    """
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9aa2bf9527c8ca05ff862ffb54315309&language=en-US"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"

    except requests.exceptions.RequestException as e:
        print(f"API request failed for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750.png?text=API+Error"


# --- Function to Get Movie Recommendations ---
def recommend(movie):
    """
    Finds similar movies and fetches their names and posters.
    """
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_names = []
    recommended_movies_posters = []

    for i in movies_list:
        # Get the movie_id from the dataframe using the index
        movie_id = movies.iloc[i[0]].movie_id

        # Append the movie title and poster URL
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

        # Add a small delay to avoid overwhelming the API server
        time.sleep(0.1)

    # --- THIS LINE WAS MOVED ---
    # The return must be OUTSIDE the for loop to run after all movies are found.
    return recommended_movies_names, recommended_movies_posters


# --- Load Data ---
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Make sure 'movie_dict.pkl' and 'similarity.pkl' are in the correct directory.")
    st.stop()

# --- Streamlit User Interface ---
st.set_page_config(layout="wide")
st.title('Movie Recommender System 🎬')

selected_movie_name = st.selectbox(
    'Select a movie you like and we will recommend similar ones!',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner('Finding recommendations...'):
        names, posters = recommend(selected_movie_name)

        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(names[i])
                st.image(posters[i])