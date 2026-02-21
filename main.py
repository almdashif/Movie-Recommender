import streamlit as st
import pickle
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎬 Movie Recommender System")

@st.cache_resource
def load_data():
    movies = pickle.load(open('models/movies.pkl','rb'))
    similarity = pickle.load(open('models/similarity.pkl','rb'))
    return movies, similarity

movies, similarity = load_data()

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {"api_key": API_KEY}
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    except Exception as e:
        print("API Error:", e)

    return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie_title):
    index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recs = []

    for i in movie_list:
        m_data = movies.iloc[i[0]]

        recs.append({
            "title": m_data['title'],
            "year": int(m_data['year']) if pd.notna(m_data['year']) else "N/A",
            "poster": fetch_poster(m_data['movie_id'])
        })

    return recs

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Show Recommendations"):
    data = recommend(selected_movie)

    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            st.image(data[idx]['poster'], width=250)
            st.markdown(f"**{data[idx]['title']}**")
            st.caption(f"Year: {data[idx]['year']}")