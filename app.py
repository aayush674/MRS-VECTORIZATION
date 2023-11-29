import streamlit as st
import pickle

st.title("Movie Recommender System")

year_values = st.slider("Select Range of Release Year", 1950, 2020, (2000, 2020))

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    recommended_movies = []

    c = 0
    for i in movies_lists:
        mov_year=int(movies.iloc[i[0]].year_of_release)
        if((mov_year >= year_values[0]) & (mov_year <= year_values[1])):
            recommended_movies.append(movies.iloc[i[0]].title)
            c = c + 1
        if c == 10:
            return recommended_movies


xs = pickle.load(open('x.pkl', 'rb'))
movies = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('sim.pkl', 'rb'))
selected_movie = st.selectbox(
    'Movies', xs
)

if st.button('Recommend'):
    names = recommend(selected_movie)

    col1, col2 = st.columns(2)
    with col1:
        st.text(names[0])
    with col2:
        st.text(names[1])

    col1, col2 = st.columns(2)
    with col1:
        st.text(names[2])
    with col2:
        st.text(names[3])

    col1, col2 = st.columns(2)
    with col1:
        st.text(names[4])
    with col2:
        st.text(names[5])

    col1, col2 = st.columns(2)
    with col1:
        st.text(names[6])
    with col2:
        st.text(names[7])

    col1, col2 = st.columns(2)
    with col1:
        st.text(names[8])
    with col2:
        st.text(names[9])
