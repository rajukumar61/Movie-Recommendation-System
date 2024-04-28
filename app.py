import streamlit as st
import pickle
import requests

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Load movie data and similarity scores
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Set page title and icon
st.set_page_config(page_title="Cinemate", page_icon="🎬")

# Create a beautiful navbar
st.markdown(
    """
    <style>
        .navbar {
            background-color: #2f4f4f;
            padding: 10px 0;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .navbar-text {
            font-size: 24px;
            color: #ffffff;
            text-align: center;
            margin-bottom: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display navbar and title
st.markdown(
    "<div class='navbar'><p class='navbar-text'>Welcome to Cinemate : A Movie Recommender System</p></div>",
    unsafe_allow_html=True
)

# carausal

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)

# Movie selection dropdown
select_value = st.selectbox("Select a movie from the dropdown", movies_list)

# Slider to select number of recommendations
num_recommendations = st.slider("Select number of recommendations", min_value=1, max_value=10, value=5)

# Recommendation function
def recommend(movie, num_recommendations):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:num_recommendations+1]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

# Display recommendations when button is clicked
if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(select_value, num_recommendations)
    cols = st.columns(num_recommendations)
    for i in range(num_recommendations):
        with cols[i]:
            st.text(movie_name[i])
            st.image(movie_poster[i])
