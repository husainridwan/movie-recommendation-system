import streamlit as st
import pandas as pd
import difflib 
import joblib
import requests

st.title("Movie Recommendation System")

movie_dict = joblib.load(open('movie_dict.pkl', 'rb'))
similarity = joblib.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movie_dict)
option = st.selectbox('Enter/Select the movie you would like recommendations for?', movies['Title'].values)

def get_index():
    matches = difflib.get_close_matches(option, movies['Title'])
    close_match = matches[0]
    movie_index = movies[movies['Title'] == close_match].index.values[0]
    return movie_index

def poster(id):
    response = requests.get("https://www.omdbapi.com/?i=tt" + str(id) + "&apikey=2c4448a0")
    data = response.json()
    return data['Poster']

def recommend(movie):
    similar_movie = sorted(list(enumerate(similarity[get_index()])), reverse=True, key=lambda x: x[1])[1:5]
    recommended_movies = []
    posters = []
    for i in similar_movie:
        id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].Title)
        posters.append(poster(id))
    return recommended_movies, posters

st.write('These movies are similar to ', option)
if st.button('Recommend movies'):
    names, posters = recommend(option)
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    for i in range(4):
        with col1:
            st.caption(names[i])
            st.image(posters[i], use_column_width='always')