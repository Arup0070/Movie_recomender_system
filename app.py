import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2e9b20f2108f10fa65a2d92ba24789dc&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original"+ data['poster_path']
def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommend_movies_posters=[]

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        #fetch poster
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_posters


similarity = pickle.load((open("similarity.pkl", "rb")))

movies_dict = pickle.load((open("movie_dict.pkl", "rb")))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    "Please Write the name of your favourite movie.",
    movies["title"].values

)
if st.button("Recommend"):
    names,posers = recommend(selected_movie_name)
    col1 , col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posers[0])
    with col2:
        st.text(names[1])
        st.image(posers[1])
    with col3:
        st.text(names[2])
        st.image(posers[2])
    with col4:
        st.text(names[3])
        st.image(posers[3])
    with col5:
        st.text(names[0])
        st.image(posers[0])