import streamlit as st
import pandas as pd
import requests
import pickle



movie_list = pickle.load(open('movie_dict.pkl','rb'))
movie_list=pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2708a68dac6ce0de710228bab1a799e1&language=en-US".format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w185/' + data['poster_path']

def recommend(movie):
    movie_index = movie_list[movie_list['title']==movie].index[0]
    distance = similarity[movie_index]
    movies = sorted(enumerate(distance),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    recommend_posters=[]
    for i in movies:
        movie_id=movie_list.iloc[i[0]].id
        recommend_movies.append(movie_list.iloc[i[0]]['title'])

        recommend_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_posters



st.title('Movie Recommender')


selected_movie = st.selectbox(
    'Select Movie',
    movie_list['title'].values)



if st.button('Recommend'):
    movies,poster = recommend(selected_movie)
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text(movies[0])
        st.image(poster[0])
    with col2:
        st.text(movies[1])
        st.image(poster[1])
    with col3:
        st.text(movies[2])
        st.image(poster[2])
    with col4:
        st.text(movies[3])
        st.image(poster[3])
    with col5:
        st.text(movies[4])
        st.image(poster[4])
